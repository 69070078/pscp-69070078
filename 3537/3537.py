"""imposter"""
import json
player = {}
while True:
    a = input()
    if a == "Start":
        break
    player_dict1 = json.loads(a)
    player.update(player_dict1)

dead={}
while True:
    b = input()
    if b=="End":
        break
    if b in player:
        role = player.pop(b)
        dead[b]=role

imposter = 0
for key in player:
    if player[key] == "Impostor":
        imposter += 1

print(f"{imposter} Impostor Remains")
print("***Alive***")
for name in sorted(player):
    print(f"{name} : {player[name]}")
print("***Dead***")
for name in sorted(dead):
    print(f"{name} : {dead[name]}")
