import numpy as np

def sequence_alignment(D1, D2):
    n1, n2 = len(D1), len(D2)

    # Step 1: Initialize DP table
    dp = np.zeros((n1 + 1, n2 + 1), dtype=int)

    # Base cases: Aligning with empty strings requires inserting spaces
    for i in range(n1 + 1):
        dp[i][0] = i  # Cost of deleting all characters in D1
    for j in range(n2 + 1):
        dp[0][j] = j  # Cost of inserting all characters in D2

    # Step 2: Fill DP table using recurrence relation
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            match_mismatch = dp[i - 1][j - 1] + (1 if D1[i - 1] != D2[j - 1] else 0)
            insert_D1 = dp[i][j - 1] + 1  # Insert space in D1
            insert_D2 = dp[i - 1][j] + 1  # Insert space in D2
            dp[i][j] = min(match_mismatch, insert_D1, insert_D2)

    # Step 3: Backtrack to reconstruct alignment
    aligned_D1 = []
    aligned_D2 = []
    i, j = n1, n2

    while i > 0 or j > 0:
        if i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + (1 if D1[i - 1] != D2[j - 1] else 0):
            # Match/mismatch case
            aligned_D1.append(D1[i - 1])
            aligned_D2.append(D2[j - 1])
            i -= 1
            j -= 1
        elif j > 0 and dp[i][j] == dp[i][j - 1] + 1:
            # Insert space in D1 (shift right in D2)
            aligned_D1.append('_')
            aligned_D2.append(D2[j - 1])
            j -= 1
        else:
            # Insert space in D2 (shift right in D1)
            aligned_D1.append(D1[i - 1])
            aligned_D2.append('_')
            i -= 1

    # Reverse the alignments since they were built backwards
    aligned_D1.reverse()
    aligned_D2.reverse()

    return dp[n1][n2], ''.join(aligned_D1), ''.join(aligned_D2), dp

# Test case
D1 = "ctatg"
D2 = "ttaagc"
cost, aligned_D1, aligned_D2, dp_table = sequence_alignment(D1, D2)

print("Optimal Cost:", cost)
print("Aligned D1:  ", aligned_D1)
print("Aligned D2:  ", aligned_D2)

# Print the DP table for debugging
print("\nDP Table:")
for row in dp_table:
    print(row)