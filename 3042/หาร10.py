"""หาร 10"""
def main():
    """หาร 10"""
    num = int(input())
    List = []
    for i in range(num,-1,-1):
        if not i%10 :
            List.append(i)
            i-=10
    print(*List)
main()
