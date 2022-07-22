# import timeit
# import cProfile
#
#
# def f(n):
#     if n < 2:
#         return n
#     return f(n - 1) + f(n - 2)
#
#
# def t(n):
#     if n < 2:
#         return n
#     pp = 0
#     p = 1
#     for i in range(n - 1):
#         pp, p = p, pp + p
#     return p
#
#
# print(cProfile.run('t(10)'))
#
# print(f(5))
# print(t(5))
#
# print(timeit.timeit('f(5)', 'from __main__ import f'))
# print(timeit.timeit('t(5)', 'from __main__ import t'))


# from math import pi
#
#
# class Cylinder:
#     @staticmethod
#     def make_area(d, h):
#         circle = pi * d ** 2 / 4
#         side = pi * d * h
#         return round(circle * 2 + side, 2)
#
#     def __init__(self, diameter, high):
#         self.dia = diameter
#         self.h = high
#         self.area = self.make_area(diameter, high)
#
#
# a = Cylinder(1, 2)
# # print(a.area)
#
# print(a.make_area(2, 2))

import collections

# counter = collections.Counter()
#
# for i in ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'a']:
#     counter[i] += 1
#
# print(counter)
#
# c = collections.Counter(a=4, b=3, c=2)
# print(list(c.elements()))
# print(list(counter.elements()))

# a = collections.Counter('alsdfhgglakjdlgkjal').most_common(1)
#
# print(a)

# a = collections.Counter(a=4, b=3, c=2)
# b = collections.Counter(a=1, b=2, c=3)
# a.subtract(b)
# b.subtract(a)
# print(a)
# print(b)
# print(sum(a.values()))
# print(list(a))
# print(set(a))
# print(dict(a))
# print(a.most_common()[:-2:-1])

# a = collections.deque('abcdef')
# print(a)

# a.append('x')
# print(a)
#
# a.appendleft('x')
# print(a)
#
# a.extend('abcd')
# print(a)

# a.rotate(2)
# print(a)
#
# a.rotate(-2)
# print(a)
#
# a.rotate(-2)
# print(a)

# d = collections.OrderedDict({'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2})
# print(d)
#
# d.popitem(last=False)
#
# print(d)
#
# d.move_to_end('apple', last=True)
#
# print(d)


# class Node:
#     def __init__(self, value=None, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right
#
#     def __repr__(self):
#         return f'Node[{self.value:^5}]'
#
#
# class Tree:
#     def __init__(self):
#         self.root = None
# # функция для добавления узла
#
#     def new_node(self, value):
#         return Node(0, None, None)
#
#     # функция для вычисления высоты дерева
#     def height(self, node):
#         if node is None:
#             return 0
#         else:
#             left_height = self.height(node.left)
#             right_height = self.height(node.right)
#             if left_height > right_height:
#                 return left_height + 1
#             else :
#                 return right_height + 1
#
#     # функция для распечатки элементов на определенном уровне дерева
#     def print_given_level(self, root, level):
#         if root is None:
#             return
#         if level == 1 :
#             print(root, end='')
#         elif level > 1 :
#             self.print_given_level(root.left, level - 1)
#         self.print_given_level(root.right, level - 1)
#
#     # функция для распечатки дерева
#     def print_level_order(self, root):
#         h = self.height(root)
#         i = 1
#         while i <= h:
#             self.print_given_level(self.root, i)
#             print()
#             i += 1
#
#     # функция для вычисления ширины дерева
#     def get_max_width(self, root):
#         max_wdth = 0
#         i = 1
#         h = self.height(root)
#         while i <= h :
#             width = self.get_width(root, i)
#             if width > max_wdth:
#                 max_wdth = width
#             i += 1
#         return max_wdth
#
#     def get_width(self, root, level):
#         if root is None:
#             return 0
#         if level == 1:
#             return 1
#         elif level > 1:
#             return self.get_width(root.left, level - 1) + self.get_width(root.right, level - 1)
#         self.get_width(root.right, level - 1)
#
#
# t = Tree()
# t.root = t.new_node(8)
# t.root.left = t.new_node(4)
# t.root.right = t.new_node(12)
# t.root.left.left = t.new_node(2)
# t.root.left.right = t.new_node(6)
# t.root.right.left = t.new_node(10)
# t.root.right.right = t.new_node(14)
# t.root.left.left.left = t.new_node(0)
# t.root.left.left.right = t.new_node(3)
# t.root.left.right.left = t.new_node(5)
# t.root.left.right.right = t.new_node(7)
# t.root.right.left.left = t.new_node(9)
# t.root.right.left.right = t.new_node(11)
# t.root.right.right.left = t.new_node(13)
# t.root.right.right.right = t.new_node(15)
# t.print_level_order(t.root)
# print(f'высота: {t.height(t.root)}')
# print(f'ширина: {t.get_max_width(t.root)}')

# import hashlib

# print(hashlib.sha1(b"Hello, Bob!").hexdigest())
# print(hashlib.sha1(b"Secret" + b"Hello, Bob").hexdigest())
# s = hashlib.sha1(b"Hello, Bob").hexdigest()
# print(hashlib.sha1(b"Secret" + bytes(s.encode('utf-8'))).hexdigest())


# def is_eq_str(a, b):
#     ha = hashlib.sha1(a.encode('utf-8')).hexdigest()
#     hb = hashlib.sha1(b.encode('utf-8')).hexdigest()
#     print(ha)
#     print(hb)
#     return ha == hb
#
#
# print(is_eq_str('asd', 'dsa'))

p = 'asdasdasd'

unique_substrings = list(set([p[i:j+1+i] for i in range(len(p)) for j in range(len(p))]))

substrings = {p[i:j] for i in range(len(p)) for j in range(i + 1, len(p) + 1)}

print(unique_substrings)

print(substrings)

result = set()
for i in range(len(p)):
    for j in range(i + 1, len(p) + 1):
        result.add(p[i:j])
result.remove(p)
result = list(result)
print(len(result))
