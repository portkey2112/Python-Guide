# Program to show a sample of what Generators can do.

class Testing:
    def __init__(self, s):
        self.s = s

    def __next__(self):
        self.main()

    def main(self):
        for it in range(0, 10):
            yield "{0}--{1}".format(self.s, it)


if __name__ == '__main__':
    obj = Testing("me")
    x = obj.main()
    for i in range(0, 15):
        print(x.__next__())
