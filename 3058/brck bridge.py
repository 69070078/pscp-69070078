"""BrickBridge"""
A = int(input())
B = int(input())
GOAL = int(input())
BB = 5*B
GOALharn5 = GOAL%5

if GOALharn5<=A and GOALharn5 and BB>=GOAL:
    print(GOAL % 5)
elif GOAL - BB == A:
    print(A)
elif BB>=GOAL and not GOALharn5:
    print(0)
elif GOAL - BB > 0 and BB + A >= GOAL:
    print(GOAL - BB)
else:
    print(-1)
