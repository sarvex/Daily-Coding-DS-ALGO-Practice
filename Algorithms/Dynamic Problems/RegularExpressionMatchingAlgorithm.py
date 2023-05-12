#program to match the string with pattern using modular algorithm
def reGexMatch(s,p):
    #lookuptable
    #initalize the 2D array dp with None/null of size length of pattern+1 & string+1.
    #inorder to tranverse the 2D array two iterative variables required i & j.
    dp = [[None for _ in range(len(s)+1)] for _ in range(len(p)+1)]
    for i in range(len(dp)):
        for j in range(len(dp[0])):
          #the very first index is always True because blank is matches with only blank
            if i==0 and j==0: dp[i][j]=True
            elif i==0: dp[i][j]=False
            elif j==0:
                dp[i][j] = dp[i-2][j] if p[i-1]=='*' else False
            elif p[i-1]=='*':
                dp[i][j]=dp[i-2][j]
                if p[i - 2] in [s[i - 1], '.']:
                    dp[i][j]=dp[i][j] or dp[i][j-1]
            elif p[i-1]=='.':
                dp[i][j]=dp[i-1][j-1]
            elif p[i-1]==s[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                #else all other cases are False.
                dp[i][j]=False
    return "Yes-Matched" if dp[len(p)][len(s)] else "No-Mismatch"
  
#Input code
s=input()
p=input()
print(reGexMatch(s, p))

#Example:
'''
s="crosssection"
p="cros*ect.*"
Output - Yes-Matched
'''
