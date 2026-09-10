"""จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""
A = int(input())
B = int(input())
C = int(input())
D = int(input())
count = []
for i in range(A,B+1):
    if i%C == D:
        count.append(i)
print(len(count))
