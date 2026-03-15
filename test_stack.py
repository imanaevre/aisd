from stack import *

def test_push():
    s = Stack()
    s.push(5)
    assert s.size() == 1
    assert s.peek() == 5


def test_pop():
    s = Stack()
    s.push(10)
    s.push(20)
    assert s.pop() == 20
    assert s.pop() == 10
    assert s.pop() is None


def test_peek():
    s = Stack()
    assert s.peek() is None
    s.push(7)
    assert s.peek() == 7
    assert s.size() == 1


def test_is_empty():
    s = Stack()
    assert s.is_empty() is True
    s.push(1)
    assert s.is_empty() is False


def test_size():
    s = Stack()
    assert s.size() == 0
    s.push(1)
    s.push(2)
    assert s.size() == 2


def test_clear():
    s = Stack()
    s.push(1)
    s.push(2)
    s.clear()
    assert s.size() == 0
    assert s.is_empty() is True


def test_to_list():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.to_list() == [3, 2, 1]


test_push()
test_pop()
test_peek()
test_is_empty()
test_size()
test_clear()
test_to_list()

print("Все тесты пройдены успешно!")