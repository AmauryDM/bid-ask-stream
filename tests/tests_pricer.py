import random

from bid_ask_streaming.pricer import Pricer


class TestsPricer:
    def test_get_prices(self):
        origin = 10
        pricer = Pricer(origin)
        bid_price, ask_price = pricer.get_prices()
        assert bid_price is not None
        assert ask_price is not None

    def test_correct_prices(self):
        random.seed(42)
        origin = 10
        pricer = Pricer(origin)
        bid_price, ask_price = pricer.get_prices()
        assert bid_price == 11.39
        assert ask_price == 11.41

    def test_get_bis_ask(self):
        origin = 10
        pricer = Pricer(origin)
        bid, ask = pricer.get_bid_ask()
        assert bid is not None
        assert ask is not None

    def test_correct_bid_ask(self):
        random.seed(42)
        origin = 10
        pricer = Pricer(origin)
        bid, ask = pricer.get_bid_ask()
        assert (bid[:-1] == ["11.39", "0"]).all()
        assert (ask[:-1] == ["11.41", "1"]).all()
