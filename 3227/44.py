"""ไพ่ 44 ใบ"""
card = input().upper()
D,H,S,C = "diamonds","hearts","spades","clubs"
A,J,Q,K = "ace","jack","queen","king"
dork = card[-1]
lek = card[0:-1]
if dork == "D":
    dork = D
elif dork == "H":
    dork = H
elif dork == "S":
    dork = S
elif dork == "C":
    dork = C

if lek == "A":
    lek = A
elif lek == "J":
    lek = J
elif lek == "Q":
    lek = Q
elif lek == "K":
    lek = K

print(f"{lek} of {dork}")
