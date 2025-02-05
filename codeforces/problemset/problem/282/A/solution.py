# This code is generated by AI just for testing
# Using claude-3.5-sonnet

# https://codeforces.com/problemset/problem/282/A
# 282A - Bit++

import sys
input = sys.stdin.readline

def solve():
    x = 0
    n = int(input())
    for _ in range(n):
        s = input().strip()
        x += 1 if '+' in s else -1
    print(x)

if __name__ == "__main__":
    solve() 