import sys
input = sys.stdin.readline

x, y, c = map(int, input().split())

print(c * ((x / y) + (y / x)))