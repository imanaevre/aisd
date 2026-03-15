from stack import *

def main():
    stack = Stack()

    print("Добавляем элементы")
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Содержимое стека:", stack.to_list())

    print("peek():", stack.peek())

    print("pop():", stack.pop())
    print("pop():", stack.pop())
    print("pop():", stack.pop())

    print("pop() из пустого:", stack.pop())

    print("Пуст ли стек:", stack.is_empty())

    print('Добавляем элементы')
    stack.push(100)
    stack.push(200)

    print("Размер стека:", stack.size())

    stack.clear()
    print("После clear():", stack.to_list())

if __name__ == "__main__":
    main()