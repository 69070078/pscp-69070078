"""BigFrame"""
def main():
    """BigFrame"""
    message1 = input().strip()
    message2 = input().strip()
    message3 = input().strip()
    message4 = input().strip()
    message5 = input().strip()

    L = max(len(message1), len(message2), len(message3),
            len(message4), len(message5))

    print("*"*(L + 4))
    for message in (message1, message2, message3, message4, message5):
        print("*",message, " " * (L - len(message)) + "*")
    print("*"*(L + 4))
main()
