# Program to print fibonacci numbers
# using the concept of Generators in Python

class Fibonacci:
    def __init__(self, limit):
        self.limit = limit

    def generator(self):
            a = 0
            b = 1
            it = 1
            while it <= self.limit:
                c = a + b
                a = b
                b = c
                yield c
                it += 1
            raise StopIteration


if __name__ == '__main__':
    obj = Fibonacci(5).generator()
    try:
        while True:
            print(obj.__next__())
    except StopIteration:
        print("Done")
