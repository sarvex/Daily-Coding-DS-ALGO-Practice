suy = int(input())

for _ in range(suy):
    a = input()
    b = a[:len(a) // 2]
    c = a[(len(a) // 2) :] if (len(a)%2==0) else a[(len(a) // 2) + 1:]
    if (sorted(b) == sorted(c)):
        print("YES")
    else:
        print("NO")
