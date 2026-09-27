"""Flower"""
def main():
    """Flower"""
    L, N = map(int, input().split())
    tayang = 1
    total_tayang = 1
    while total_tayang < N:
        tayang += 1
        total_tayang += tayang

    teemo = tayang//L
    if tayang%L:
        teemo+=1
    print(teemo)
main()
