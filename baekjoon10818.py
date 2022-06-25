import sys

input = sys.stdin.readline
n = int(input());
list = input().split()
min = int(list[0])
max = int(list[0])
for i in list:
  if(int(i)<min):
    min = int(i)

  if(int(i)>max):
    max = int(i)

print(min, max)