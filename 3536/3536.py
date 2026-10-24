"""isPrime_large"""
num = int(input())
prime = True
if num<2:
    prime=False
else:
    for i in range(2,int(num**0.5)+1):
        if not num%i:
            prime = False
            break

if prime:
    print("YES")
else:
    print("NO")
