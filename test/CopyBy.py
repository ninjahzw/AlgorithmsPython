"""
almost same as Java
"""

__author__ = 'Zhaowei'

def reassign(list):
    list = [0, 1]
def append(list):
    list.append(1)
list = [0]
reassign(list)
# append(list)
print list

def reassign1(a):
    a += 2

a = 1
reassign1(a)
print a
