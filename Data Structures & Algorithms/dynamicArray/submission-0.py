class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = dict()
        self.capacity = capacity
        self.size = 0

        for i in range(self.capacity):
            self.array[i] = None

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        idx = self.getSize()
        self.checkSize()
        self.set(idx, n)
        self.size += 1

    def popback(self) -> int:
        if self.size == 0: return
        idx = self.size - 1
        temp = self.array.get(idx)
        del self.array[idx]
        self.size -= 1
        return temp
 
    def resize(self) -> None:
        curr_capacity = self.capacity
        new_capacity = curr_capacity * 2
        for i in range(curr_capacity, new_capacity):
            self.array[i] = None
        self.capacity = new_capacity

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity

    def checkSize(self) -> None:
        if self.getSize() + 1 > self.getCapacity():
            self.resize()
