
while True:
    try:
        str1,str2=input().split()
        dp = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]
        max1 = 0
        
        for i in range(len(str1)):
            for j in range(len(str2)):
                if str1[i] == str2[j]:
                    dp[i][j] = max(dp[i][j],dp[i-1][j-1])+1
                else:dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                max1 = max(dp[i][j],max1)
        print(max1)
        dp.clear()
    except EOFError:
        break
