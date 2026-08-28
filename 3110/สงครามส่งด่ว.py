""""สงครามส่งด่วน"""
def main():
    """สงครามส่งด่วน"""
    n = input().split()
    weight = float(input())
    if n[0] == "BKK" and n[1] == "CNX":
        print(f"{10+(weight*30):.2f}")
    elif n[0] == "CNX" and n[1] == "UBP":
        print(f"{15+(weight*40):.2f}")
    elif n[0] == "UBP" and n[1] == "BKK":
        print(f"{20+(weight*40):.2f}")
    elif n[0] == "BKK" and n[1] == "PKT":
        print(f"{25+(weight*50):.2f}")
    elif n[0] == "PKT" and n[1] == "CNX":
        print(f"{30+(weight*60):.2f}")
    elif n[0] == "UBP" and n[1] == "PKT":
        print(f"{40+(weight*70):.2f}")
    else:
        print("Error")
main()
