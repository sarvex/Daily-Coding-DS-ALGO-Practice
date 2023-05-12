def subsetSum(A, n, sum):

    if sum == 0:
        return True

    if n < 0 or sum < 0:
        return False

    if include := subsetSum(A, n - 1, sum - A[n]):
        return True

    return subsetSum(A, n - 1, sum)


def partition(A):
 
    total = sum(A)
 
    return (total & 1) == 0 and subsetSum(A, len(A) - 1, total/2)
 
 
if __name__ == '__main__':
 
    A = [7, 3, 1, 5, 4, 8]
 
    print(partition(A))
