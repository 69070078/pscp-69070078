"""A-E-I-O-U"""
vowels = ["a","e","i","o","u"]
word = input().lower()
n = len(word)
a=0
e=0
i=0
o=0
u=0
for K in range(0,n):
    if word[K] in vowels:
        if word[K] == "a":
            a+=1
        elif word[K] == "e":
            e+=1
        elif word[K] == "i":
            i+=1
        elif word[K] == "o":
            o+=1
        elif word[K] == "u":
            u+=1

if a:
    print(f"a : {a}")

if e:
    print(f"e : {e}")

if i:
    print(f"i : {i}")

if o:
    print(f"o : {o}")

if u:
    print(f"u : {u}")
