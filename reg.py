# Package
from getpass import getpass

# Create new player
## ID
player_id = input("Masukan ID pemain baru: ")
## Password
player_pass = getpass("Masukan password pemain baru: ")

# Result
if player_id in player_data["id"]:
    print("Player ID already exist")
else:
    open("player_data.txt", "a").write(player_id + ";" + player_pass + "\n")