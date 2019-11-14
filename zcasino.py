#CASINO:

import math
import random

money=1000
continuer=True




while continuer: #boolean
    roulettenumber = -1 #before for starting the loop
    while roulettenumber < 0 or roulettenumber > 99: #the player choose which number is gonna bet on
        roulettenumber = input("Choose a number between 0 and 99 on the roulette: ")
        
        try: 
            roulettenumber = int(roulettenumber)
        except ValueError: #for no input
            print("no entry")
            roulettenumber = -1 #don't forget to return at the begin of the loop
            continue #python still run
        if roulettenumber < 0: #now the conditions which enter in 'while roulettenumber < 0 or roulettenumber > 99'
            print("No negative number on the roulette :)!")
        if roulettenumber > 99:
            print("too hight!")

    
    bet = 0 #now the loop for playing 'money'
    while bet <= 0 or bet > money:
        bet = input("How much you bet? : ")
        
        try:
            bet = int(bet)
        except ValueError: #again for no input
            print("Vous n'avez pas saisi de nombre")
            mise = -1
            continue
        if mise <= 0:
            print("La mise saisie est négative ou nulle.")
        if mise > argent:
            print("Vous ne pouvez miser autant, vous n'avez que", argent, "$")

    # Le nombre misé et la mise ont été sélectionnés par
    # l'utilisateur, on fait tourner la roulette
    numero_gagnant = randrange(50)
    print("La roulette tourne... ... et s'arrête sur le numéro", numero_gagnant)

    # On établit le gain du joueur
    if numero_gagnant == nombre_mise:
        print("Félicitations ! Vous obtenez", mise * 3, "$ !")
        argent += mise * 3
    elif numero_gagnant % 2 == nombre_mise % 2: # ils sont de la même couleur
        mise = ceil(mise * 0.5)
        print("Vous avez misé sur la bonne couleur. Vous obtenez", mise, "$")
        argent += mise
    else:
        print("Désolé l'ami, c'est pas pour cette fois. Vous perdez votre mise.")
        argent -= mise

    # On interrompt la partie si le joueur est ruiné
    if argent <= 0:
        print("Vous êtes ruiné ! C'est la fin de la partie.")
        continuer_partie = False
    else:
        # On affiche l'argent du joueur
        print("Vous avez à présent", argent, "$")
        quitter = input("Souhaitez-vous quitter le casino (o/n) ? ")
        if quitter == "o" or quitter == "O":
            print("Vous quittez le casino avec vos gains.")
            continuer_partie = False