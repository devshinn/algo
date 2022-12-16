from bisect import bisect_left, bisect_right


def binary_search(array, target, start, end):
    if start > end:
        return None

    if array[end] == target:
        return end
    if array[start] == target:
        return start
    mid = (start+end) // 2
    if(array[mid] == target):
        return mid
    elif(array[mid] > target):
        return binary_search(array, target, start, mid-1)

    else:
        return binary_search(array, target, mid+1, end)


n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if(result == None):
    print('존재하지않는 타겟입니다.')
else:
    print(result+1)

print('bisect_left: ', bisect_left(array, 14))
print(array)
print('bisect_left: ', bisect_right(array, 14))
