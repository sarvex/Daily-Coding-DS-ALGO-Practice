def fact(n):
    return n if (n == 1) else n*fact(n-1)


test = int(input())
for _ in range (0,test):
    val = int(input())
    print(fact(val))


##Example Test Case
# Sample input:
# 4
# 1
# 2
# 5
# 3
# Sample output:
#
# 1
# 2
# 120
# 6
