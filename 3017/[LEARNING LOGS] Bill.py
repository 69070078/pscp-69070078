"""[LEARNING LOGS] Bill"""
def main():
    """[LEARNING LOGS] Bill"""
    price = int(input())
    service = price*0.1
    vat = (price + service)*0.07
    if service <50:
        service = 50
    elif service>1000:
        service = 1000
    vat = (price + service)*0.07
    total = price + service + vat
    print(f"{total:.2f}")
main()
