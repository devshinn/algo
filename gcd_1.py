
import math


def get_gcd(arr):
    g = [0]
    for i in range(1, len(arr)):
        g.append(math.gcd(arr[i-1], arr[i]))
        print(g)
    return g


def solution(arrayA, arrayB):
    answer = [0]
    a = get_gcd(arrayA)
    b = get_gcd(arrayB)
    for num in arrayB:
        if(num % a == 0):
            break
        else:
            answer.append(a)
    for num in arrayA:
        if(num % b == 0):
            break
        else:
            answer.append(b)

    return max(answer)


get_gcd([6, 9, 15])
