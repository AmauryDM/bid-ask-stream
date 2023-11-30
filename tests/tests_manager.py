from bid_ask_streaming.manager import Manager


class TestManager:
    def test_produce_consume(self):
        streaming = 1
        window = 1
        manager = Manager(streaming, window)
        print(manager.manage_streaming())
