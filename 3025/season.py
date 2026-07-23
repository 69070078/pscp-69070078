"""Season"""
def main():
    """Season"""
    month = int(input())
    day = int(input())

    if month in(1,2):
        print("winter")
    if month in(4,5):
        print("spring")
    if month in(7,8):
        print("summer")
    if month in(10,11):
        print("fall")
    if month == 3:
        print("spring" if day >= 21 else "winter")
    if month == 6:
        print("summer" if day >= 21 else "spring")
    if month == 9:
        print("fall" if day >= 21 else "summer")
    if month == 12:
        print("winter" if day >= 21 else "fall")
main()
