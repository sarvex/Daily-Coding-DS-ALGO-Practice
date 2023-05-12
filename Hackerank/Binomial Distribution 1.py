# Enter your code here. Read input from STDIN. Print output to STDOUT
def factorial(n):
    return 1 if n in [0, 1] else n*factorial(n-1)
    
def nCr(n,r):
    return factorial(n)/(factorial(r) * factorial(n-r))

arr=map(float,input().split())
p=arr[0]/sum(arr)
q=arr[1]/sum(arr)
sum1=0
for i in range(3,7):
    temp=nCr(6,i)
    temp1=(p**i)*(q**(6-i))
    sum1+= temp*temp1
print (round(sum1,3))
