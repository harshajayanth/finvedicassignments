def lcs(X, Y):
    m = len(X)
    n = len(Y)
    
    # Create a DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Length of LCS is dp[m][n]
    lcs_length = dp[m][n]
    
    # Backtrack to find the LCS string
    lcs_str = [""] * lcs_length
    i, j = m, n
    index = lcs_length - 1
    
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_str[index] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    # Join the LCS string array to form the final LCS string
    return dp[m][n], "".join(lcs_str)

# Driver code to test the function
if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    
    length, lcs_string = lcs(X, Y)
    print(f"Length of Longest Common Subsequence is {length}")
    print(f"Longest Common Subsequence is {lcs_string}")
