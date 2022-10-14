class QueueFIFO:
    data = []
    flag = True

    def put(self, elem):
        self.data += [elem]
        return 'done'

    def get(self):
        el = None
        el = self.data[0]
        self.data = self.data[1:]
        return el

    def len(self):
        res = len(self.data)
        # for _ in self.data:
        #     res += 1
        return res

    def get_without_deleting(self, index=0):
        return self.data[index]

    def check_last_added(self):
        return self.data[-1]

    def first(self):
        if self.len():
            return self.data[0]

    def empty(self):
        if len(self.data) > 0:
            return False
        else:
            return True

    def print_all_message(self):
        for i in self.data:
            print(i.print())
            print('\n')

    def clear(self):
        self.data = []
        return 'done'


if __name__ == "__main__":
    q = QueueFIFO()
    buf = 0.0
    for i in range(10):
        q.put(buf)
        buf += 1.5

    print(q.check_last_added())
    print(q.get_without_deleting())
    print(q.get())
    print("after print")
    while not q.empty():
        print(q.get())
