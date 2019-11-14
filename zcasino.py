#CASINO:


from random import randrange

money=1000
continuer=True




while continuer: #boolean
    roulettenumber = -1 #before for starting the loop
    while roulettenumber < 0 or roulettenumber > 99: #the player choose which number is gonna bet on
        roulettenumber = input("Choose a number between 0 and 99 on the roulette: ")
        
        try: 
            roulettenumber = int(roulettenumber)
        except ValueError: #for no input or no int
            print("Wrong entry")
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
        except ValueError: #again for no input or no int
            print("Wrong entry")
            bet = -1 #again don't forget to return at the loop's beginning: while bet <= 0 or bet > money
            continue #python still run
        if bet <= 0:
            print("less than 0 money? :): ")
        if bet > money: #for the balance
            print("Too much, you only have:", money, "€")

    
    winnernumber = randrange(99) #from import random with the highest number of the roulette
    print("AND SPIN !!!! .............", winnernumber, "!")

    # No pain no gain, three conditions
    if winnernumber == roulettenumber:
        print("CONGRATULATIONS !!! You win: ", bet * 10000000000000, "€ !") #because i'm generous
        money += bet * 10000000000000 #you add the gain at the money value
    elif winnernumber % 2 == roulettenumber % 2: # same color
        bet = bet*500 #too generous
        print("Same color!You win: ", bet,"€")
        money += bet #incremantation of the bet in money's value
    else:# the last condition: loosing
        print("You lost :(, here a euro for cheer !")
        money -= bet #soustraction of the bet
        money += 1 #too generous

    #game's ending
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