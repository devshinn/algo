num = input()
result = int(num[0])
for i in range(1, len(num)):
    if(int(num[i]) <= 0 or result <= 1):
        result += int(num[i])
    else:
        result *= int(num[i])
print('val: ', result)
