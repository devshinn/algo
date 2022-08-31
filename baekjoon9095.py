import sys
T = int(sys.stdin.readline())
result=0
count = 0
def rec(n):
	if(n == 1): return 1
	if(n == 2): return 2
	if(n == 3): return 4
	return (rec(n-1)+rec(n-2)+rec(n-3))


for _ in range(T):
	n = int(sys.stdin.readline())
	print(rec(n))