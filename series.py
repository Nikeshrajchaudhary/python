'''n = int(input("enter n: "))

print(", ".join([str(n) for n in range(1, n, 4)]))'''

i =1
count = 1
while (True):
    print(i, end=' ')
    i +=4
    count = count + 1
    if count==21:
        break