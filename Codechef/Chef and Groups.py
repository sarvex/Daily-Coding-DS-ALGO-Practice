#Problem Link: https://www.codechef.com/MARCH21C/problems/GROUPS

t = int(input())
for _ in range(t):
    s = input()
    s = f'0{s}0'
    c = s.count('01')
    print(c)
