import random
import time
import os

list_number_alea = []
score = 0
statut = True
check_tour = True

while statut:
    number_alae = random.randint(0, 99)
    list_number_alea.append(number_alae)
    for number_alea in list_number_alea:
        print(f"{number_alea}")
        time.sleep(2)
    os.system('clear')
    print("A toi !")
    check_tour = True
    for expected in list_number_alea:
        number_player = None
        while number_player == None:
            try:
                number_player = int(input("Entrez un nombre en 0 et 99 : "))
            except ValueError:
                print("Veuillez entrer un nombre valide")

        if number_player != expected:
                check_tour = False
                statut = False
                print(f"Score = {score} \n Game over !")
                break

    if check_tour:
        score += 1
