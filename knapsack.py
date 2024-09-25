def knapsack(weight_limit, weights, values, n):
    # Initialize the DP table
    dp = [[0 for _ in range(weight_limit + 1)] for _ in range(n + 1)]
    
    # Build the DP table
    for i in range(1, n + 1):
        for w in range(1, weight_limit + 1):
            if weights[i-1] <= w:
                # Include the current item or exclude it
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                # Exclude the current item
                dp[i][w] = dp[i-1][w]
    
    # Return the maximum value at the bottom-right corner of the table
    return dp[n][weight_limit]

# Driver code to test the function
if __name__ == "__main__":
    # Define item weights and values
    values = [60, 100, 120]
    weights = [10, 20, 30]
    weight_limit = 15
    n = len(values)
    
    # Get the maximum value
    max_value = knapsack(weight_limit, weights, values, n)
    print(f"Maximum value that can be taken in the knapsack: {max_value}")
