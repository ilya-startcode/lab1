#!/usr/bin/env python
# dirty python hello appsec world
# works in python3 / python / pypy
#добавили этот комментарий для конфликта

import sys, os

# бесполезные переменные
x = None
y = 1
z = ""

def useless(a=None):
    if a:
        return a
    return None

# запрос имени (грязно)
try:
    name = input("Enter your name: ")
except Exception:
    name = "anonymous"

if name is None or name == "":
    name = "anonymous"

# грязная сборка строки
parts = [
    "H","e","l","l","o"," ",
    "a","p","p","s","e","c"," ",
    "w","o","r","l","d"," ",
    "f","r","o","m"," ",
    "@", name
]

msg = ""
for p in parts:
    msg = msg + str(p)

# бессмысленная логика
if y == 1:
    z = msg
else:
    z = useless(msg)

try:
    raise RuntimeError("noise")
except RuntimeError:
    pass

print(z)
