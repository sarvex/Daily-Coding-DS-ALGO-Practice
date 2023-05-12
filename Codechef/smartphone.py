num = int(input())
suy = [int(input()) for _ in range(num)]
suy.sort()

for i in range(num):
    suy[i] = suy[i]*(num-i)

print(max(suy))
