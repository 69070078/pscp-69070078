"""SurprisingVote"""
def main():
    """SurprisingVote"""
    total = float(input())
    Max = float(input())
    Mid = (total - Max)/2
    Min = Mid-1
    if Min<0:
        Min = 0

    if Max-Min <= 2:
        print("Not surprising")
    elif Max - Min > 2:
        print("Surprising")
main()
