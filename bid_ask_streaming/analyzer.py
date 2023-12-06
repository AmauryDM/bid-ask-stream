from bid_ask_streaming.utils import timer


class Analyzer:
    def __init__(self, window):
        self.window = window

    @timer
    def get_metrics(self, data):
        mean, std, autocorr = None, None, None
        if len(data) >= self.window:
            mean = data.tail(self.window).mean()
            std = data.tail(self.window).std()
            autocorr = data.tail(self.window).autocorr()
        return mean, std, autocorr
