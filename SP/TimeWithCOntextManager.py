import time


class TimeWithContextManager:

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed_time = time.time() - self.start_time
        print("Elapsed time: {:.2f} seconds".format(elapsed_time))


# using with context manager

with TimeWithContextManager() as tm:
    time.sleep(5)

if __name__ == '__main__':
    with TimeWithContextManager() as tm:
        time.sleep(3)
