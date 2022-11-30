from collections import deque

visited = dict()

visited[(1,1)] = [0, 0]

print(visited[(1,1)])

print(type(visited[(1,1)]))

moveA, moveB = visited[(1,1)]
print(moveA)