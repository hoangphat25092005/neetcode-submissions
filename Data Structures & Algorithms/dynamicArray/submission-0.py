class DynamicArray:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("The capacity must be greater than zero")

        self.capacity = capacity
        self.size = 0
        self.arr = [None] * capacity

    def get(self, i: int) -> int:
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")

        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")

        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        if self.size == 0:
            raise IndexError("Cannot pop from an empty array")

        self.size -= 1
        value = self.arr[self.size]
        self.arr[self.size] = None

        return value

    def resize(self) -> None:
        self.arr.extend([None] * self.capacity)
        self.capacity *= 2

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity