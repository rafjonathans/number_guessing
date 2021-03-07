# Packages
from tabulate import tabulate
import numpy as np
import os

# Preparation
## Player data
if not (os.path.isfile("player_data.txt")):
    new_file = open("player_data.txt", "w+")
    new_file.write("id;pass\n")
    new_file.close()

## Highscore data
if not os.path.isfile("highscore_data.txt"):
    open("highscore_data.txt", "w+")

game = 1
while game == 1:
    print("""
    *************************************
    Selamat Menainkan Tebaaaak Angkaaa
    *************************************""")

    player_data = np.loadtxt("player_data.txt", 
                            dtype = {"names": ("id", "password"),
                                    "formats": ("U99", "U99")}, 
                            delimiter=";")

    # Main menu
    print("""
    Menu:
    1. Main
    2. Daftar
    3. Highscore
    4. Keluar
    """)
    menu1 = input("Silahkan pilih menu yang diinginkan:")

    ## Game
    if menu1 == "1":
        exec(open("game.py").read())

    ## Sign up
    elif menu1 == "2":
        exec(open("reg.py").read())

    ## Highscore
    elif menu1 == "3":
        # Load latest highscore
        highscore_data = np.loadtxt("highscore_data.txt", 
                                    dtype = {"names": ("name", "score"), 
                                            "formats": ("U99", "i")},
                                    delimiter=";")

        # Print in tabular
        n_top = 5
        a = highscore_data["score"].argsort()[-n_top:][::-1]
        print(tabulate(highscore_data[:][a], headers=("Player", "Score")))
    
    ## Exit game
    elif menu1 == "4":
        game = 2

    ## NON int input
    else:
        print("Masukin yang bener")

quit()