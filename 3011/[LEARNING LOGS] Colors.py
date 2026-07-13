"""Colors"""
def main():
    """Colors"""
    color4 = input()
    color5 = input()
    if (color4 == "Red" and color5 == "Blue") or (color5 == "Red" and color4 == "Blue"):
        print("Violet")
    elif (color4 == "Red" and color5 == "Yellow") or (color5 == "Red" and color4 == "Yellow"):
        print("Orange")
    elif (color4 == "Yellow" and color5 == "Blue") or (color5 == "Yellow" and color4 == "Blue"):
        print("Green")
    elif color4 == "Red" and color5 == "Red":
        print("Red")
    elif color4 == "Blue" and color5 == "Blue":
        print("Blue")
    elif color4 == "Yellow" and color5 == "Yellow":
        print("Yellow")
    else:
        print("Error")
main()
