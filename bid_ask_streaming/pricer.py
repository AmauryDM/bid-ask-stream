import random
from datetime import datetime

import numpy as np

from bid_ask_streaming.utils import timer


class Pricer:
    def __init__(self, origin):
        self.origin = origin

    def get_prices(self):
        brownian = random.uniform(-5, 5)
        bid_price = self.origin + brownian
        ask = random.uniform(0, 0.5)
        ask_price = bid_price + ask
        return round(bid_price, 2), round(ask_price, 2)

    @timer
    def get_bid_ask(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        bid_price, ask_price = self.get_prices()
        bid = np.array([bid_price, 0, timestamp])
        ask = np.array([ask_price, 1, timestamp])
        return bid, ask
