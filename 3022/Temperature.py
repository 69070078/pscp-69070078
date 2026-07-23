"""Temperature"""
def main():
    """Temperature"""
    temp = float(input())
    unit_to_c = input()
    unit_f = input()
    ci = 0
    cf = 0
    if unit_to_c == "C":
        ci = temp
    elif unit_to_c =="F":
        ci = (temp-32)*5/9
    elif unit_to_c =="K":
        ci = temp - 273.15
    elif unit_to_c == "R":
        ci = (temp*5/9)-273.15

    if unit_f == "C":
        cf = ci
    elif unit_f =="F":
        cf = (ci*9/5)+32
    elif unit_f =="K":
        cf = ci + 273.15
    elif unit_f == "R":
        cf = (ci+273.15)*9/5
    print(f"{cf:.2f}")
main()

