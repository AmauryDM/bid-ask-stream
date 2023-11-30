from bid_ask_streaming.consumer import Consumer
from bid_ask_streaming.producer import Producer


class Manager:
    def __init__(self, streaming, window):
        self.streaming = streaming
        self.window = window

    def manage_streaming(self):
        # Creating Threads
        producer = Producer(self.streaming)
        consumer = Consumer(self.streaming, self.window)

        # Starting Threads
        consumer.start()
        producer.start()

        # Waiting for threads to complete
        producer.join()
        consumer.join()
