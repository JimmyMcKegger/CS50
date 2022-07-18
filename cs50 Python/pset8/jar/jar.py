class Jar:

    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        else:
            self._capacity = capacity
            self._size = 0

    def __str__(self):
        cookie = "\U0001f36A"
        return self._size * cookie

    def deposit(self, n):
        if self._size + n <= self._capacity:
            self._size += n
        else:
            raise ValueError

    def withdraw(self, n):
        if self._size - n >= 0:
            self._size -= n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity
    @property
    def size(self):
        return self._size

def main():
    cap = input("Capacity: ")
    jar = Jar(int(cap))
    jar.deposit(5)
    print(jar)

if __name__ == "__main__":
    main()
