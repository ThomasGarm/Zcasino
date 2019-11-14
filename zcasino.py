#CASINO:


from random import randrange #computer select a random number in a choosen range

money=1000 #the amount you have when you start
continuer=True #boolean




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
        print ("you earn ",money,"€")
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
    if money <= 0:
        print("BANKROUT")
        continuer = False
    else:
        leave = input("Do you want to leave ? (y) ? ") #only 'y' count here
        if leave == "y":
            print("You leave with: ",money,"€")
            continuer = False