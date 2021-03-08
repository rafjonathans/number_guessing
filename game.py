import random
from getpass import getpass

# Preparation
angka = random.randint(1,20)

player_name = input("Masukan ID pemain: ")
player_pass = getpass("Masukan password: ")
tebak = 0
score = 100

# Game
if player_name in player_data["id"] and player_pass in player_data["password"]:
    # Game is on if ID and password input OK
    while score > 0 and int(tebak) != angka:
        print("Score saat ini " + str(score))
        tebak = input("Tebak angka antara 1 - 20: ")
        if tebak.strip().isdigit():
            if int(tebak) < angka:
                print("Tebak lebih besar")
                score = score - 10
            elif int(tebak) > angka:
                print("Tebak lebih kecil")
                score = score - 10
            else:
                print("ANDA BENARRRR")
        else:
            score = score - 20
            print("TEBAKNYA ANGKA WOY!")
            tebak = 0
    

    ## Result
    ### Show
    print("Player " + player_name + " score " + str(score))

    ### Open highscore data file and append new score
    open("highscore_data.txt", "a").write(player_name + ";" + str(score) + "\n")
else:
    print("""
    ID or Password is incorrect""")