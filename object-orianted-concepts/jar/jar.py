class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._size = 0
        self._capacity = capacity

    def __str__(self):
        txt = ""
        for _ in range(self._size):
            txt += "🍪"
        return txt.strip()

    # checks if size is higher than capacity and then adds to jar
    def deposit(self, n):
        if n > self._capacity or n < 0 or self._size + n > self._capacity:
            raise ValueError
        self._size += n

    # checks if n cookies is higher than self and then withdraw from jar
    def withdraw(self, n):
        if n > self._size:
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar(10)
    jar.deposit(12)

if __name__ == "__main__":
    main()