class Message:
    __startTime = 0.0
    __exit_time = 0.0

    def __init__(self, start_time=0.0, exit_time=0.0):
        self.__start_time = start_time
        self.__exit_time = exit_time

    @property
    def start_time(self):
        return self.__start_time

    @property
    def exit_time(self):
        return self.__exit_time

    @start_time.setter
    def start_time(self, start_time):
        self.__start_time = start_time

    @exit_time.setter
    def exit_time(self, exit_time):
        self.__exit_time = exit_time

    def print(self):
        print(f"st= {self.__start_time}\tex= {self.__exit_time}")

    def get_delta(self):
        return self.__exit_time - self.__start_time

    def get_delta11(self):
        return self.__start_time - self.__exit_time


if __name__ == '__main__':
    x = Message()
    y = Message(10, 20)
    z = Message(100)
    x.start_time = 100
    # print(x.start_time)
    # print(x.start_time, x.exit_time)
    # print(y.start_time, y.exit_time)
    # print(z.start_time, z.exit_time)
    x.print()
    y.print()
    z.print()
