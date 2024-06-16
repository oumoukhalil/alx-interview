def minOperations(n):
    if n == 1:
        return 0  # Only one 'H' is already in the file.

    dp = [0] * (n + 1)  # Initialize an array to store the minimum operations for each number of characters.

    for i in range(2, n + 1):
        dp[i] = i  # Initialize with the maximum possible operations.

        for j in range(2, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n]

# Example usage
n = 9
result = minOperations(n)
print("Number of operations:", result)


n = 9
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
