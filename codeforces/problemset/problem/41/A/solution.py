# This code is generated by AI just for testing
# Using claude-3.5-sonnet

# https://codeforces.com/problemset/problem/41/A
# 41A - Translation

import sys
input = sys.stdin.readline

def solve():
    s = input().strip()
    t = input().strip()
    print("YES" if s == t[::-1] else "NO")

if __name__ == "__main__":
    solve()