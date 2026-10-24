"""B - Fully pair?"""
from collections import Counter
word = input().strip()
count = Counter(word)

unpair = []
kuy = []
for char in word:
    if count[char]%2 and char not in kuy:
        unpair.append(char)
        kuy.append(char)
if not unpair:
    print("fully paired")
else:
    print("".join(unpair))
