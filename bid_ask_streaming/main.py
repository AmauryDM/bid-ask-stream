from bid_ask_streaming.manager import Manager


def main():
    streaming_items = 20
    sliding_window = 3
    manager = Manager(streaming_items, sliding_window)
    manager.manage_streaming()


if __name__ == "__main__":
    main()
