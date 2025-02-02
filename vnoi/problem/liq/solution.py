"""
Problem: Longest Increasing Subsequence (Easy Version)
---------------------------------------------------
Given a sequence of N integers, find the length of the longest increasing subsequence.
A subsequence is increasing if each element is strictly greater than the previous one.

Constraints:
- 1 ≤ N ≤ 1000
- 1 ≤ Ai ≤ 10000

Strategy:
--------
Use dynamic programming where dp[i] represents the length of the longest
increasing subsequence ending at index i. For each position, we look back
at all previous positions to find sequences we can extend.

Complexity:
----------
Time: O(n^2) - two nested loops to fill dp array
Space: O(n) - dp array to store LIS lengths
"""

import sys
input = sys.stdin.readline

def solve():
    # Read number of elements and the sequence
    n = int(input())
    a = list(map(int, input().split()))
    
    # Initialize dp array - minimum LIS length is 1 for each position
    dp = [1] * n
    
    # For each position, try to extend sequences ending at previous positions
    for i in range(n):
        for j in range(i):
            if a[i] > a[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # Answer is the maximum LIS length found
    print(max(dp))

if __name__ == '__main__':
    solve()