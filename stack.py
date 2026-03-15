class Stack:
    def __init__(self):
        self._data = []
        self._size = 0

    def push(self, value: int):
        self._data.append(value)
        self._size += 1

    def pop(self):
        if self.is_empty():
            return None
        self._size -= 1
        return self._data.pop()


    def peek(self):
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self):
        if self._size == 0:
            return True
        else:
            return False

    def size(self):
        return self._size

    def clear(self):
        self._size -= self.size()
        self._data = []

    def to_list(self):
        return self._data[::-1]

