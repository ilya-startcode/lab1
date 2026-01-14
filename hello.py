#!/usr/bin/env python
# intentionally dirty python code
# works in: python3 / python / pypy

import sys, os

# бесполезные переменные
a = None
b = 0
c = ""

def f(x=None):
    if x is None:
        pass
    else:
        return x
    return None

# "грязная" сборка строки
msg = ""
for i in ["H","e","l","l","o"," ","a","p","p","s","e","c"," ","w","o","r","l","d"]:
    msg = msg + i

# бессмысленные операции
if b == 0:
    c = msg
else:
    c = f(msg)

try:
    raise Exception("noise")
except Exception as e:
    _ = str(e)

print(c)
