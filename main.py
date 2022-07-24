class Stack:
    def __init__(self,my_list):
        self.stack = my_list

    def is_empty(self):
        return len(self.stack) == 0

    def push(self,elem):
        self.stack.insert(0, elem)

    def pop(self):
        return self.stack.pop(0)

    def peek(self):
        return self.stack[0]

    def size(self):
        return len(self.stack)

# 2 Используя стек из задания 1 необходимо решить задачу на проверку сбалансированности скобок

l = Stack([i for i in input('Введите последовательность скобок: ')])
k = Stack([])

open_dict = {
     '(': ')',
     '[': ']',
     '{': '}'
     }
close_dict = {
     ')': '(',
     ']': '[',
     '}': '{'
     }

for i in l.stack:
    flag = 'Cбалансированно'
    if l.stack[0] in close_dict:
        flag = 'Несбалансированно'
        break
    elif i in open_dict:
        k.push(i)
    else:
        if k.stack[0] == close_dict[i]:
            k.pop()
        else:
            flag = 'Несбалансированно'
            break

if not k.is_empty():
    flag = 'Несбалансированно'

print(flag)





















# l = Stack([1,2,3])
# print(l.isEmpty())
# print(l.stack)
# print(l.__dict__)
# l.push(10)
# print(l.stack)
# print(l.pop())
# print(l.stack)
# print(l.peek())
# print(l.size())




