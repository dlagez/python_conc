# @Time      :2021/1/9 20:57
# @Author    :RocZhang(dlage)
import os
with open('pi_digits.txt') as f:
    contents = f.read()
    print(contents)

with open('Python编程入门到实践/文件和异常/pi_digits.txt') as f:
    contents = f.read()
    print(contents.rstrip())
# 3.1415926535
# 8979323846
# 2643383279
# copy

with open('Python编程入门到实践/文件和异常/pi_digits.txt') as f:
    for line in f:
        print(line.rstrip())
# 3.1415926535
# 8979323846
# 2643383279
# copy

filename = 'Python编程入门到实践/文件和异常/pi_digits.txt'
with open(filename) as f:
    lines = f.readlines()
for line in lines:
    print(line.rstrip())

filename = 'Python编程入门到实践/文件和异常/pi_digits.txt'
with open(filename) as f:
    lines = f.readlines()
pi_strings = ''
for line in lines:
    pi_strings +=line.rstrip()
    print(line.rstrip())

print(pi_strings)
print(len(pi_strings))


filename = 'Python编程入门到实践/文件和异常/pi_digits.txt'
with open(filename) as f:
    lines = f.readlines()
pi_strings = ''
for line in lines:
    pi_strings += line.strip()

print(pi_strings[:52] + '...')
print(len(pi_strings))


filename = 'programming.txt'
with open(filename, 'w') as f:
    f.write("I love programming.")