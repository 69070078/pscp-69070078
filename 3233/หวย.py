"""หวยคัว"""
real = input()
fake = input()

if real == fake:
    print(1000000)
elif (real[3:] == fake[3:]) and (real[0] != fake[0]):
    print(100000)
elif (real[-3:] == fake[-3:]) and (real[0] == fake[0]):
    print(2000)
elif (real[-2:] == fake[-2:]) and (real[0] == fake[0]):
    print(1000)
elif (real[-3:] == fake[-3:]) and (real[0] != fake[0]):
    print(200)
elif (real[-2:] == fake[-2:]) and (real[0] != fake[0]):
    print(100)
elif real[0] == fake[0]:
    print(20)
else:
    print(0)
