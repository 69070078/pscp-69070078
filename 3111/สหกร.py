"""สหกรณ์โรงเรียน"""
from decimal import Decimal, ROUND_HALF_UP
def main():
    """สหกรณ์โรงเรียน"""
    M = input()
    n = int(input())
    total=Decimal("0")
    for _ in range(n):
        cost = Decimal(input())
        total+=cost
    if M == "Y":
        total=total*Decimal("95")/Decimal("100")
    elif M == "N":
        if total>=Decimal("500"):
            total=total*Decimal("97")/Decimal("100")
    total = total.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
    print(f"{total:.2f}")
main()
