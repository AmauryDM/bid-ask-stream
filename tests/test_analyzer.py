import pandas as pd

from bid_ask_streaming.analyzer import Analyzer


class TestAnalyzer:
    def test_get_no_metrics(self):
        data = pd.Series([10, 11])
        window = 3
        analyzer = Analyzer(window)
        mean, std, autocorr = analyzer.get_metrics(data)
        assert mean is None
        assert std is None
        assert autocorr is None

    def test_get_metrics(self):
        data = pd.Series([10, 11, 12])
        window = 3
        analyzer = Analyzer(window)
        mean, std, autocorr = analyzer.get_metrics(data)
        assert mean is not None
        assert std is not None
        assert autocorr is not None

    def test_get_correct_metrics(self):
        data = pd.Series([10, 11, 12])
        window = 3
        analyzer = Analyzer(window)
        mean, std, autocorr = analyzer.get_metrics(data)
        assert mean == 11.0
        assert std == 1.0
        assert autocorr == 0.9999999999999999
