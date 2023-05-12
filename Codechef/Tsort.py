vin = int(input())
suy = [int(input()) for _ in range(vin)]
suy.sort(reverse=False)
for nums in suy:
    print(nums)
