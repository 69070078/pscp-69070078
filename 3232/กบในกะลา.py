"""กบน้อยกระโดด"""
x,y = map(int,input().split())

total = 0
count = 0
if x == y:
    count = 1
    total = y
else:
    while total<y:
        total+=x
        if x < 1:
            break

        x-=2
        count+=1

if total>=y:
    print(count)
else:
    print(-1)
