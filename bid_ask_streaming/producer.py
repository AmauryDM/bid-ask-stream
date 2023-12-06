import threading
import time

import bid_ask_streaming.utils as constants
from bid_ask_streaming.pricer import Pricer
from bid_ask_streaming.utils import timer


class Producer(threading.Thread):
    def __init__(self, streaming):
        super().__init__()
        self.streaming = streaming

    @timer
    def run(self):
        capacity = constants.CAPACITY
        buffer = constants.buffer
        in_index = constants.in_index
        mutex = constants.mutex
        empty = constants.empty
        full = constants.full

        items_produced = 0
        counter = 0

        while items_produced < self.streaming:
            empty.acquire()
            mutex.acquire()

            pricer = Pricer(35)
            bid_ask = pricer.get_bid_ask()

            counter += 1
            buffer[in_index] = bid_ask
            in_index = (in_index + 1) % capacity

            mutex.release()
            full.release()

            time.sleep(1)

            items_produced += 1
