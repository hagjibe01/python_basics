import random


Players = []
player_numbers = int(input("Anzahl der Mitspieler: "))
for i in range(player_numbers):

    player_names = input("Mitspielernamen: ")
    Players.append(player_names)
    
for i in range(len(Players)):
    player_turn = i+1
    print(player_turn, ".", Players[i])

print("Das Spiel geht nun los")


for i in range(5):
    print(random.randint(1,6))


    








