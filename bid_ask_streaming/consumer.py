import threading
import time

import pandas as pd

import bid_ask_streaming.constants as constants
from bid_ask_streaming.analyzer import Analyzer


class Consumer(threading.Thread):
    def __init__(self, streaming, window):
        super().__init__()
        self.streaming = streaming
        self.window = window

    def run(self):
        capacity = constants.CAPACITY
        buffer = constants.buffer
        out_index = constants.out_index
        mutex = constants.mutex
        empty = constants.empty
        full = constants.full

        items_consumed = 0

        data = pd.DataFrame(columns=["price", "bid/ask", "timestamp"])
        metrics = pd.DataFrame(columns=["mean", "std", "autocorr"])

        while items_consumed < self.streaming:
            full.acquire()
            mutex.acquire()

            item = buffer[out_index]
            out_index = (out_index + 1) % capacity
            data = pd.concat(
                [
                    data,
                    pd.DataFrame(item, columns=["price", "bid/ask", "timestamp"]),
                ]
            )
            ask_data = data[data["bid/ask"] == "1"]

            analyzer = Analyzer(self.window)
            mean, std, autocorr = analyzer.get_metrics(ask_data["price"].astype(float))

            if mean and std and autocorr:
                metrics = pd.concat(
                    [
                        metrics,
                        pd.DataFrame(
                            [[mean, std, autocorr]], columns=["mean", "std", "autocorr"]
                        ),
                    ]
                )

            mutex.release()
            empty.release()

            time.sleep(2.5)

            items_consumed += 1

        print(metrics.reset_index(drop=True))
        return metrics
