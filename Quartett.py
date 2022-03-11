import os
import random
import time

__author__ = "7518074, Biesecker, 7076367, Vu"
__email__ = "s6912946@stud.uni-frankfurt.de, s2770441@stud.uni-frankfurt.de"
__credits__ = " "


def type_player():
    '''
    generates the playerlist
    :return: the completed playerlist
    '''

    player_list = list()

    # This loop will take care of inputs with a wrong vallue.
    # It will be never ending till an integer is typed.

    while True:
        try:
            number_of_players = int(input("Wie viele Spieler sind Sie?: "))

            while number_of_players < 2 or number_of_players > 8:
                print("Es müssen mindestens 2 oder maximal 8 Spieler sein, um\
 das Spiel zu spielen.")
                number_of_players = int(input("Wie viele Spieler sind Sie?: "))

                if number_of_players >= 2:
                    break
            break
        except ValueError:
            print("Geben Sie bitte eine Ganzzahl ein.")
            continue

    print("\n")
    print("| Falls Sie gegen einen oder mehrere Computer spielen wollen,|")
    print("| geben sie als Spieler 'computer' ein.                      |")
    print("| Geben sie die realen Spieler als erstes und die 'computer' |")
    print("| als letzes an!                                             |")
    print("\n")

    # This loop will request the name of the players.

    for i in range(0, number_of_players, 1):
        while True:
            try:
                player_name = str(input("Geben Sie den Namen ein: "))
                while len(player_name) <= 2:
                    print("Bitte geben Sie mindestens 3 Buchstaben ein.")
                    player_name = str(input("Geben Sie den Namen ein: "))
                    
                    if len(player_name) >= 3:
                           break
                break
            except ValueError:
                print("Bitte geben Sie Buchstaben ein.")
                continue

        player_list.append(player_name)

    # The real players now will be validated.

    for i in range(0, number_of_players):
        if player_list[i] != "computer":
            player_list[i] = (player_list[i], True)

    count = 0

    # The total number of computers will be counted.

    for i in player_list:
        if i == "computer":
            count += 1

    # The computers will be removed so they can be renamed.

    for i in range((number_of_players - count), number_of_players):
        player_list.pop()

    # Afterwards they will be put in the playerlist again.

    for i in range(count):
        x = (("computer" + str(i + 1)), False)
        player_list.append(x)

    print("")
    print("| TEILNEMHMER |")
    print(player_list)
    print("")

    return player_list


def card_deck(player_list):
    '''
    This function distributes the cards to each player.
    :param player_list: is the player list
    :return: The distributed cards of all players and the
    rest cards if only two are playing.
    '''

    HEARTS, DIAMONDS, CLUBS, SPADES = "\u2665", "\u2666", "\u2663", "\u2660" 

    all_cards = set()

    all_cards = {("rot", " 1", HEARTS), ("rot", "2", HEARTS),
                 ("rot", "3", HEARTS), ("rot", "4", HEARTS),
                 ("schwarz", "1", HEARTS), ("schwarz", "2", HEARTS),
                 ("schwarz", "3", HEARTS), ("schwarz", "4", HEARTS),
                 ("rot", "1", DIAMONDS), ("rot", "2", DIAMONDS),
                 ("rot", "3", DIAMONDS) , ("rot", "4", DIAMONDS),
                 ("schwarz", "1", DIAMONDS),("schwarz", "2", DIAMONDS),
                 ("schwarz", "3", DIAMONDS),("schwarz", "4", DIAMONDS),
                 ("rot", "1", CLUBS), ("rot", "2", CLUBS), ("rot", "3", CLUBS),
                 ("rot", "4", CLUBS),
                 ("schwarz", "1", CLUBS), ("schwarz", "2", CLUBS),
                 ("schwarz", "3", CLUBS),("schwarz", "4", CLUBS),
                 ("rot", "1", SPADES), ("rot", "2", SPADES),
                 ("rot", "3", SPADES), ("rot", "4", SPADES),
                 ("schwarz", "1", SPADES), ("schwarz", "2", SPADES),
                 ("schwarz", "3", SPADES),("schwarz", "4", SPADES)}

    on_hand_player = list()
    card_list = list()

    # Random cards will be distributed to two players till both of them got
    # 10 cards on their hands.

    if len(player_list) == 2:
        print('--------------------------------')
        for i in range(0, len(player_list)):
            on_hand_player = []
            while len(on_hand_player) < 10:
                temp_card = all_cards.pop()
                on_hand_player.append(temp_card)
            x = list(player_list[i])
            x.append(on_hand_player)
            tuple(x)
            card_list.append(x)
            
        # These rest cards will be saved for later.

        rest_cards = all_cards

    # If there are more than two players the cards will be distributed fairly.

    if len(player_list) > 2 and len(player_list) != 4 and len(player_list) != 8 :

        divided = len(all_cards) // len(player_list)
        for i in range(0, len(player_list)):
            on_hand_player = []
            while len(on_hand_player) < divided:
                temp_card = all_cards.pop()
                on_hand_player.append(temp_card)

            x = list(player_list[i])
            x.append(on_hand_player)
            tuple(x)
            card_list.append(x)

        rest_cards = all_cards

    if len(player_list) == 4 or len(player_list) == 8 :

        divided = len(all_cards) // len(player_list)
        for i in range(0, len(player_list)):
            on_hand_player = []
            while len(on_hand_player) < divided:
                temp_card = all_cards.pop()
                on_hand_player.append(temp_card)

            x = list(player_list[i])
            x.append(on_hand_player)
            tuple(x)
            card_list.append(x)

        rest_cards = set()    
    game_list = list()

    #

    for i in range(0, len(player_list)):
        if ((player_list[i])[1]) == False:
            computer_dict = {}
            computer_dict[player_list[i][0]] = "Name"
            for x in card_list[i][2]:
                computer_dict[x] = ""        
            game_list.append(computer_dict)
        
        if ((player_list[i])[1]) == True:
            player_dict = {}
            player_dict[player_list[i][0]] = "Name"
            for x in card_list[i][2]:
                player_dict[x] = ""        
            game_list.append(player_dict)
   
    return game_list, rest_cards


def quartett(player_dict):
    '''
    This function will check if there are any quartetts in the deck.
    :param player_dict: dictionary of player
    :return: is the game list
    '''
    
    HEARTS, DIAMONDS, CLUBS, SPADES = "\u2665", "\u2666", "\u2663", "\u2660"
    
    counter_heart_red = list()
    counter_heart_black = list()
    counter_diamonds_red = list()
    counter_diamonds_black = list()
    counter_clubs_red = list()
    counter_clubs_black = list()
    counter_spades_red = list()
    counter_spades_black = list()

    # The cards in the deck will be counted.

    for y in player_dict.keys():
        if y[2] == HEARTS and y[0] == "rot":
            counter_heart_red.append(y)
           
        if y[2] == HEARTS and y[0] == "schwarz":
            counter_heart_black.append(y)
           
        if y[2] == DIAMONDS and y[0] == "rot":
            counter_diamonds_red.append(y)
            
        if y[2] == DIAMONDS and y[0] == "schwarz":
            counter_diamonds_black.append(y)
            
        if y[2] == CLUBS and y[0] == "rot":
            counter_clubs_red.append(y)
            
        if y[2] == CLUBS and y[0] == "schwarz":
            counter_clubs_black.append(y)
            
        if y[2] == SPADES and y[0] == "rot":
            counter_spades_red.append(y)
           
        if y[2] == SPADES and y[0] == "schwarz":
            counter_spades_black.append(y)

    # If there are 4 same cards a quartett is found and the
    # dictionary will be updated.

    if len(counter_heart_red) == 4:
        for z in player_dict.keys():
            if z[2] == HEARTS and z[0] == "rot":
               player_dict.update({z:'quartett'})
            
    if len(counter_heart_black) == 4:
        for z in player_dict.keys():
            if z[2] == HEARTS and z[0] == "schwarz":
               player_dict.update({z:'quartett'})
            
    if len(counter_diamonds_red) == 4:
        for z in player_dict.keys():
            if z[2] == DIAMONDS and z[0] == "rot":
               player_dict.update({z:'quartett'})
        
    if len(counter_diamonds_black) == 4:
        for z in player_dict.keys():
            if z[2] == DIAMONDS and z[0] == "schwarz":
               player_dict.update({z:'quartett'})
        
    if len(counter_clubs_red) == 4:
        for z in player_dict.keys():
            if z[2] == CLUBS and z[0] == "rot":
               player_dict.update({z:'quartett'})
            
    if len(counter_clubs_black) == 4:
        for z in player_dict.keys():
            if z[2] == CLUBS and z[0] == "schwar    z":
                   player_dict.update({z:'quartett'})

    if len(counter_spades_red) == 4:
        for z in player_dict.keys():
            if z[2] == SPADES and z[0] == "rot":
               player_dict.update({z:'quartett'})

    if len(counter_spades_black) == 4:
        for z in player_dict.keys():
            if z[2] == SPADES and z[0] == "schwarz":
               player_dict.update({z:'quartett'})

    return player_dict


def game(game_list, player_list, rest_cards):
    '''
    This function sets the procedure of the game.
    :param game_list: Includes all cards of all players
    :param player_list: the player list
    :param rest_cards: the rest cards
    '''

    quit_counter = 0

    HEARTS, DIAMONDS, CLUBS, SPADES = "\u2665", "\u2666", "\u2663", "\u2660"

    # As long as no quartetts are found this loop will continue

    while  quit_counter != 8:
        for i in range(0, len(player_list)):

            # The current player will be called out.

            if ((player_list[i])[1]) == False:
                print("An der Reihe ist...\n")
                print("-------------------")
                print(" ", (player_list[i])[0])
                print("-------------------\n")

                x = 0

                while x == 0:
                    counter_heart_red = list()
                    counter_heart_black = list()
                    counter_diamonds_red = list()
                    counter_diamonds_black = list()
                    counter_clubs_red = list()
                    counter_clubs_black = list()
                    counter_spades_red = list()
                    counter_spades_black = list()

                    # All cards of the same symbol and colour on the hand
                    # will be counted together and put in a list.

                    for y in game_list[i].keys():
                        if y[2] == HEARTS and y[0] == "rot":
                            counter_heart_red.append(y)
 
                        if y[2] == HEARTS and y[0] == "schwarz":
                            counter_heart_black.append(y)
  
                        if y[2] == DIAMONDS and y[0] == "rot":
                            counter_diamonds_red.append(y)

                        if y[2] == DIAMONDS and y[0] == "schwarz":
                            counter_diamonds_black.append(y)

                        if y[2] == CLUBS and y[0] == "rot":
                            counter_clubs_red.append(y)

                        if y[2] == CLUBS and y[0] == "schwarz":
                            counter_clubs_black.append(y)
 
                        if y[2] == SPADES and y[0] == "rot":
                            counter_spades_red.append(y)
 
                        if y[2] == SPADES and y[0] == "schwarz":
                            counter_spades_black.append(y)

                    best_choice = [("counter_heart_red", len(counter_heart_red)),
                                   ("counter_heart_black", len(counter_heart_black)),
                                   ("counter_diamond_red", len(counter_diamonds_red)),
                                   ("counter_diamond_black", len(counter_diamonds_black)),
                                   ("counter_clubs_red", len(counter_clubs_red)),
                                   ("counter_clubs_black", len(counter_clubs_black)),
                                   ("counter_spades_red", len(counter_spades_red)),
                                   ("counter_spades_black", len(counter_spades_black))]

                    # Here we will check for any quartetts.

                    quartett(game_list[i])

                    # Now the Computere will pick a card it has the most of it.

                    tempt_max = 0
                    best_card_to_pick = ""
                    for x in best_choice:
                        if x[1] > tempt_max and x[1] < 4 :
                            tempt_max = x[1]
                            best_card_to_pick = x[0]

                    # The next player is the next on the player list.
                    # If you already are the last player on the list,
                    # the next player will be the first player on the list

                    next_player = i + 1
                    if i == len(player_list) - 1:
                        next_player = 0
                    print("nächster Spieler: \n", player_list[next_player], "\n")

                    # In this loop the computer will ask for a card he picked
                    # before. In a following loop it will be checked if this card
                    # exists in the next players card deck. If so the card
                    # will be marked as taken away in the deck of the next player.
                    # If there are only 2 players and the next player does'nt
                    # have that card the computer needs to pick up a new one.
                    
                    v = 0
                    while v == 0 :
                        if best_card_to_pick == "counter_heart_red" : 
                            print("Hast du Herz rot?")

                            heart = 0 
                            for k in game_list[next_player].keys():
                                if k[2] == HEARTS and k[0] == "rot" and heart == 0: 
                                    print("Ja hab ich")
                                    game_list[next_player].update({k:'weggenommen'})
                                    game_list[i][k] = 'mitgenommen'
                                    print('gamelist', game_list[i]) 
                                    heart = 1 
                                if heart == 0: 
                                    print("Nein hab ich nicht") 
                                    v = 1
                                    x = 1 
                                    heart = 2
                                    if len(player_list) == 2 :
                                        if len(rest_cards) != 0 : 
                                            new_card = rest_cards.pop() 
                                            game_list[i][new_card] = "" 
                                            print("neue Karte", new_card) 
                                            x = 1
                                        else :
                                            my_quartett = quartett(game_list[i])
                                            your_quartett = quartett(game_list[next_player])
                                            v = 1
                                            quit_counter == 8

                        if best_card_to_pick == "counter_heart_black" :
                            print("Hast du Herz schwarz?")
                            heart = 0
                            for k in game_list[next_player].keys():
                                    if k[2] == HEARTS and k[0] == "schwarz" and heart == 0:
                                        print("Ja hab ich")
                                        game_list[next_player].update({k:'weggenommen'})
                                        game_list[i][k] = 'mitgenommen'
                                        print('gamelist', game_list[i])
                                        heart = 1
                                    if heart == 0:
                                        print("Nein hab ich nicht")
                                        v = 1
                                        x = 1 
                                        heart = 2
                                        if len(player_list) == 2:
                                            if len(rest_cards) != 0 : 
                                                new_card = rest_cards.pop()
                                                game_list[i][new_card] = ""
                                                print("neue Karte", new_card)
                                                v = 1
                                                x = 1
                                            else :
                                                my_quartett = quartett(game_list[i])
                                                your_quartett = quartett(game_list[next_player])
                                                v = 1
                                                quit_counter == 8

 
                        if best_card_to_pick == "counter_diamond_red" : 
                            print("Hast du Diamond rot?")
                            diamond = 0 
                            for k in game_list[next_player].keys():
                                if k[2] == DIAMONDS and k[0] == "rot" and diamond == 0: 
                                    print("Ja hab ich")
                                    game_list[next_player].update({k:'weggenommen'})
                                    game_list[i][k] = 'mitgenommen'
                                    print('gamelist', game_list[i]) 
                                    heart = 1 
                                if diamond == 0: 
                                    print("Nein hab ich nicht") 
                                    v = 1
                                    x = 1 
                                    diamond = 2
                                    if len(player_list) == 2 :
                                        if len(rest_cards) != 0 :
                                            new_card = rest_cards.pop() 
                                            game_list[i][new_card] = "" 
                                            print("neue Karte", new_card)
                                        else :
                                            my_quartett = quartett(game_list[i])
                                            your_quartett = quartett(game_list[next_player])
                                            v = 1
                                            quit_counter == 8


                        if best_card_to_pick == "counter_diamond_black" : 
                            print("Hast du Diamond black?")
                            diamond = 0 
                            for k in game_list[next_player].keys():                            
                                if k[2] == DIAMONDS and k[0] == "rot" and diamond == 0: 
                                    print("Ja hab ich")
                                    game_list[next_player].update({k:'weggenommen'})
                                    game_list[i][k] = 'mitgenommen'
                                    print('gamelist', game_list[i]) 
                                    diamond = 1 
                                if diamond == 0: 
                                    print("Nein hab ich nicht") 
                                    v = 1
                                    x = 1 
                                    diamond = 2
                                    if len(player_list) == 2 : 
                                            if len(rest_cards) != 0 : 
                                                new_card = rest_cards.pop() 
                                                game_list[i][new_card] = "" 
                                                print("neue Karte", new_card)
                                            else :
                                                my_quartett = quartett(game_list[i])
                                                your_quartett = quartett(game_list[next_player])
                                                v = 1
                                                quit_counter == 8

                                        
                            if best_card_to_pick == "counter_clubs_red" :
                                print("Hast du Clubs rot?")
                                clubs = 0
                                for k in game_list[next_player].keys():
                                    if k[2] == CLUBS and k[0] == "rot" and clubs == 0:
                                        print("Ja hab ich")
                                        game_list[next_player].update({k:'weggenommen'})
                                        game_list[i][k] = 'mitgenommen'
                                        print('gamelist', game_list[i])
                                        clubs = 1
                                    if clubs == 0:
                                        print("Nein hab ich nicht")
                                        v = 1
                                        x = 1  
                                        clubs = 2
                                        if len(player_list) == 2:
                                            if len(rest_cards) != 0 : 
                                                new_card = rest_cards.pop()
                                                game_list[i][new_card] = ""
                                                print("neue Karte", new_card)
                                                v = 1
                                                x = 1
                                            else :
                                                my_quartett = quartett(game_list[i])
                                                your_quartett = quartett(game_list[next_player])
                                                v = 1
                                                quit_counter == 8


                        if best_card_to_pick == "counter_clubs_black" :
                            print("Hast du Clubs rot?")
                            clubs = 0
                            for k in game_list[next_player].keys():
                                if k[2] == SPADES and k[0] == "schwarz" and  clubs == 0:
                                    print("Ja hab ich")
                                    game_list[next_player].update({k:'weggenommen'})
                                    game_list[i][k] = 'mitgenommen'
                                    print('gamelist', game_list[i])
                                    clubs = 1
                                if clubs == 0:
                                    print("Nein hab ich nicht")
                                    v = 1
                                    x = 1
                                    clubs = 2
                                    if len(player_list) == 2:
                                        if len(rest_cards) != 0 : 
                                            new_card = rest_cards.pop()
                                            game_list[i][new_card] = ""
                                            print("neue Karte", new_card)
                                            v = 1
                                            x = 1
                                        else :
                                            my_quartett = quartett(game_list[i])
                                            your_quartett = quartett(game_list[next_player])
                                            v = 1
                                            quit_counter == 8

                        if best_card_to_pick == "counter_spades_red" :
                            print("Hast du Spades rot?")
                            spades = 0
                            for k in game_list[next_player].keys():
                                if k[2] == SPADES and k[0] == "rot" and spades == 0:
                                    game_list[next_player].update({k:'weggenommen'})
                                    game_list[i][k] = 'mitgenommen'
                                    print('gamelist', game_list[i])
                                    spades = 1
                                if spades == 0:
                                    print("Nein hab ich nicht")
                                    v = 1 
                                    x = 1  
                                    spades = 2
                                    if len(player_list) == 2:
                                        if len(rest_cards) != 0 : 
                                            new_card = rest_cards.pop()
                                            game_list[i][new_card] = ""
                                            print("neue Karte", new_card)
                                            v = 1
                                            x = 1
                                        else :
                                            my_quartett = quartett(game_list[i])
                                            your_quartett = quartett(game_list[next_player])
                                            v = 1
                                            quit_counter == 8

                        if best_card_to_pick == "counter_spades_black" :
                            print("Hast du Spades schwarz?")
                            spades = 0
                            for k in game_list[next_player].keys():
                                spades = 0
                                if k[2] == SPADES and k[0] == "schwarz" and spades == 0:
                                    game_list[next_player].update({k:'weggenommen'})
                                    game_list[i][k] = 'mitgenommen'
                                    print('gamelist', game_list[i])
                                    spades = 1
                                if spades == 0:
                                    print("Nein hab ich nicht")
                                    v = 1
                                    x = 1  
                                    spades = 2
                                    if len(player_list) == 2:
                                        if len(rest_cards) != 0 :
                                            new_card = rest_cards.pop()
                                            game_list[i][new_card] = ""
                                            print("neue Karte", new_card)
                                            v = 1
                                            x = 1
                                        else :
                                            my_quartett = quartett(game_list[i])
                                            your_quartett = quartett(game_list[next_player])
                                            v = 1
                                            quit_counter == 8
    
            if ((player_list[i])[1]) == True:

                # The current real player will be called out.
                
                print("An der Reihe ist...\n")
                print("-------------------")
                print(" ", (player_list[i])[0])
                print("-------------------\n")
                print("Es werden gleich Ihre Karten angezeigt...")

                time.sleep(3)

                print("----Deine Karten---\n")
                print(game_list[i], "\n")

                x = 0

                while x == 0:
                    
                    counter_heart_red = list()
                    counter_heart_black = list()
                    counter_diamonds_red = list()
                    counter_diamonds_black = list()
                    counter_clubs_red = list()
                    counter_clubs_black = list()
                    counter_spades_red = list()
                    counter_spades_black = list()
                
                    for y in game_list[i].keys():
                        if y[2] == HEARTS and y[0] == "rot":
                            counter_heart_red.append(y)

                        if y[2] == HEARTS and y[0] == "schwarz":
                            counter_heart_black.append(y)

                        if y[2] == DIAMONDS and y[0] == "rot":
                            counter_diamonds_red.append(y)

                        if y[2] == DIAMONDS and y[0] == "schwarz":
                            counter_diamonds_black.append(y)
 
                        if y[2] == CLUBS and y[0] == "rot":
                            counter_clubs_red.append(y)

                        if y[2] == CLUBS and y[0] == "schwarz":
                            counter_clubs_black.append(y)
 
                        if y[2] == SPADES and y[0] == "rot":
                            counter_spades_red.append(y)

                        if y[2] == SPADES and y[0] == "schwarz":
                            counter_spades_black.append(y)

                    best_choice = [("counter_heart_red", len(counter_heart_red)),
                                  ("counter_heart_black", len(counter_heart_black)),
                                  ("counter_diamond_red", len(counter_diamonds_red)),
                                  ("counter_diamond_black", len(counter_diamonds_black)),
                                  ("counter_clubs_red", len(counter_clubs_red)),
                                  ("counter_clubs_black", len(counter_clubs_black)),
                                  ("counter_spades_red", len(counter_spades_red)),
                                  ("counter_spades_black", len(counter_spades_black))]
                    
                    quartett(game_list[i])
                    next_player = i + 1
                
                    if i == len(player_list) - 1:
                        next_player = 0

                    print("nächster Spieler: \n", player_list[next_player], "\n")

                    print("------- verfügbare Karten: --------")
                    print("für:", HEARTS, "fragen Sie nach 'herz rot' \
oder 'herz schwarz'")
                    print("für:", CLUBS, "fragen Sie nach 'kreuz rot' \
oder 'kreuz schwarz'")
                    print("für:", DIAMONDS, "fragen Sie nach 'karo rot' \
oder 'karo schwarz'")
                    print("für:", SPADES, "fragen Sie nach 'pik rot' \
oder 'pik schwarz'")
                    print("------------------------------------\n")

                    print("Nach welcher Karte wollen Sie", player_list[next_player])

                    while True:
                        try:
                            best_choice_player = str(input("fragen?:"))
                            while best_choice_player != "herz rot" or "herz \
schwarz" or "pik rot" or "pik schwarz" or "karo rot" or "karo \
schwarz" or "kreuz rot" or "kreuz schwarz":
                                print("Achten Sie auf eine korrekte Eingabe.")
                                best_choice_player = str(input("fragen?:"))

                                if best_choice_player == "herz rot" or "herz \
schwarz" or "pik rot" or "pik schwarz" or "karo rot" or "karo \
schwarz" or "kreuz rot" or "kreuz schwarz":
                                    break
                            break
                        except ValueError:
                            print("Geben Sie bitte Buchstaben ein.")
                            continue


                    # In this loop the player can ask for a card
                    # In a following loop it will be checked if this card
                    # exists in the next players card deck. If so the card
                    # will be marked as taken away in the deck of the next player.
                    # If there are only 2 players and the next player does'nt
                    # have that card the player needs to pick up a new one.
    
                    v = 0
                    while v == 0 :
                        if best_choice_player == "herz rot" :
                            print("Hast du Herz rot?")
                            heart = 0
                            for k in game_list[next_player].keys():
                                if game_list[next_player][k] == 'Name':
                                    continue
                                if k[2] == HEARTS and k[0] == "rot" and heart == 0:
                                    print("Ja hab ich")
                                    game_list[next_player].update({k:'weggenommen'})
                                    game_list[i][k] = 'mitgenommen'
                                    print('gamelist', game_list[i])
                                    heart = 1
                                    v = 1
                                    x = 1
                                if heart == 0:
                                    print("Nein hab ich nicht")
                                    v = 1
                                    x = 1 
                                    heart = 1
                                    if len(player_list) == 2:
                                        if len(rest_cards) != 0 :
                                            new_card = rest_cards.pop()
                                            game_list[i][new_card] = ""
                                            print("neue Karte", new_card)
                                            v = 1
                                            x = 1
                                        else :
                                            my_quartett = quartett(game_list[i])
                                            your_quartett = quartett(game_list[next_player])
                                            v = 1
                                            quit_counter == 8
                                    
   
                        if best_choice_player == "herz schwarz":
                            print("Hast du Herz schwarz?")
                            
                            heart = 0
                                
                            for k in game_list[next_player].keys():
                               
                                if game_list[next_player][k] == 'Name':
                                    continue
                
                                if k[2] == HEARTS and k[0] == "schwarz" and heart == 0:
                                    print("Ja hab ich")
                                    game_list[next_player].update({k:'weggenommen'})
                                    game_list[i][k] = 'mitgenommen'
                                    print('gamelist', game_list[i])
                                    heart = 1
                                    v = 1
                                    x = 1
                                if heart == 0:
                                    print("Nein hab ich nicht")
                                    v = 1
                                    x = 1
                                    heart = 2
                                    if len(player_list) == 2:
                                        if len(rest_cards) != 0 :
                                            new_card = rest_cards.pop()
                                            game_list[i][new_card] = ""
                                            print("neue Karte", new_card)
                                            v = 1
                                            x = 1
                                        else :
                                            my_quartett = quartett(game_list[i])
                                            your_quartett = quartett(game_list[next_player])
                                            v = 1
                                            quit_counter == 8
                                        
        
                        if best_choice_player == "karo rot" :
                            print("Hast du Diamond rot?")
                            diamond = 0
                            for k in game_list[next_player].keys():     
                                if game_list[next_player][k] == 'Name':
                                    continue
                                if k[2] == DIAMONDS and k[0] == "rot" and diamond == 0:
                                    print("Ja hab ich")
                                    game_list[next_player].update({k:'weggenommen'})
                                    game_list[i][k] = 'mitgenommen'
                                    print('gamelist', game_list[i])
                                    diamond = 1
                                    v = 1
                                    x = 1
                            
                                if diamond == 0:
                                    print("Nein hab ich nicht")
                                    v = 1
                                    x = 1  
                                    diamond = 2
                                    if len(player_list) == 2:
                                        if len(rest_cards) != 0 :
                                            new_card = rest_cards.pop()
                                            game_list[i][new_card] = ""
                                            print("neue Karte", new_card)
                                            v = 1
                                            x = 1
                                        else :
                                            my_quartett = quartett(game_list[i])
                                            your_quartett = quartett(game_list[next_player])
                                            v = 1
                                            quit_counter == 8  
        
                        if best_choice_player == "karo schwarz" :
                            print("Hast du Diamond black?")
                            diamond = 0
                            for k in game_list[next_player].keys():                                
                                if game_list[next_player][k] == 'Name':
                                    continue
                                if k[2] == DIAMONDS and k[0] == "schwarz" and diamond == 0:
                                    print("Ja hab ich")
                                    game_list[next_player].update({k:'weggenommen'})
                                    game_list[i][k] = 'mitgenommen'
                                    print('gamelist', game_list[i])
                                    diamond = 1
                                    v = 1
                                    x = 1
                                if diamond == 0:
                                    print("Nein hab ich nicht")
                                    v = 1
                                    x = 1  
                                    diamond = 2
                                    if len(player_list) == 2:
                                        if len(rest_cards) != 0 :
                                            new_card = rest_cards.pop()
                                            game_list[i][new_card] = ""
                                            print("neue Karte", new_card)
                                            v = 1
                                            x = 1
                                        else :
                                            my_quartett = quartett(game_list[i])
                                            your_quartett = quartett(game_list[next_player])
                                            v = 1
                                            quit_counter == 8
                
                        if best_choice_player == "kreuz rot" :
                            print("Hast du Clubs rot?")
                            clubs = 0
                            for k in game_list[next_player].keys():
                                if game_list[next_player][k] == 'Name':
                                        continue
                                if k[2] == CLUBS and k[0] == "rot" and clubs == 0:
                                        print("Ja hab ich")
                                        game_list[next_player].update({k:'weggenommen'})
                                        game_list[i][k] = 'mitgenommen'
                                        print('gamelist', game_list[i])
                                        clubs = 1
                                        v = 1
                                        x = 1
                                if clubs == 0:
                                        print("Nein hab ich nicht")
                                        v = 1
                                        x = 1  
                                        clubs = 2
                                        if len(player_list) == 2:
                                            if len(rest_cards) != 0 :
                                                new_card = rest_cards.pop()
                                                game_list[i][new_card] = ""
                                                print("neue Karte", new_card)
                                                v = 1
                                                x = 1
                                            else :
                                                my_quartett = quartett(game_list[i])
                                                your_quartett = quartett(game_list[next_player])
                                                v = 1
                                                quit_counter == 8

                        if best_choice_player == "kreuz schwarz" :
                            print("Hast du Clubs rot?")
                            clubs = 0
                            for k in game_list[next_player].keys():
                                if game_list[next_player][k] == 'Name':
                                    continue
                                if k[2] == SPADES and k[0] == "schwarz" and clubs == 0:
                                    print("Ja hab ich")
                                    game_list[next_player].update({k:'weggenommen'})
                                    game_list[i][k] = 'mitgenommen'
                                    print('gamelist', game_list[i])
                                    clubs = 1
                                    v = 1
                                    x = 1
                                if clubs == 0:
                                    print("Nein hab ich nicht")
                                    v = 1
                                    x = 1  
                                    clubs = 2
                                    if len(player_list) == 2:
                                        if len(rest_cards) != 0 :
                                            new_card = rest_cards.pop()
                                            game_list[i][new_card] = ""
                                            print("neue Karte", new_card)
                                            v = 1
                                            x = 1
                                        else :
                                            my_quartett = quartett(game_list[i])
                                            your_quartett = quartett(game_list[next_player])
                                            v = 1
                                            quit_counter == 8
                                        
                        if best_choice_player == "pik rot" :
                            print("Hast du Spades rot?")
                            spades = 0
                            for k in game_list[next_player].keys():
                                if game_list[next_player][k] == 'Name':
                                    continue
                                if k[2] == SPADES and k[0] == "rot" and spades == 0:
                                    game_list[next_player].update({k:'weggenommen'})
                                    game_list[i][k] = 'mitgenommen'
                                    print('gamelist', game_list[i])
                                    spades = 1
                                    v = 1
                                    x = 1
                                if spades == 0:
                                    print("Nein hab ich nicht")
                                    v = 1 
                                    x = 1  
                                    spades = 2
                                    if len(player_list) == 2:
                                        if len(rest_cards) != 0 :
                                            new_card = rest_cards.pop()
                                            game_list[i][new_card] = ""
                                            print("neue Karte", new_card)
                                            v = 1
                                            x = 1
                                        else :
                                            my_quartett = quartett(game_list[i])
                                            your_quartett = quartett(game_list[next_player])
                                            v = 1
                                            quit_counter == 8
                                        
                        if best_choice_player == "pik schwarz" :
                            print("Hast du Spades schwarz?")
                            spades = 0
                            for k in game_list[next_player].keys():
                                if game_list[next_player][k] == 'Name':
                                    continue
                                if k[2] == SPADES and k[0] == "schwarz" and spades == 0:
                                    print("Ja hab ich")
                                    game_list[next_player].update({k:'weggenommen'})
                                    game_list[i][k] = 'mitgenommen'
                                    print('gamelist', game_list[i])
                                    spades = 1
                                    v = 1
                                    x = 1
                                if spades == 0:
                                    print("Nein hab ich nicht")
                                    v = 1
                                    x = 1  
                                    spades = 2
                                    if len(player_list) == 2:
                                        if len(rest_cards) != 0 :
                                            new_card = rest_cards.pop()
                                            game_list[i][new_card] = ""
                                            print("neue Karte", new_card)
                                            v = 1
                                            x = 1
                                        else :
                                            my_quartett = quartett(game_list[i])
                                            your_quartett = quartett(game_list[next_player])
                                            v = 1
                                            quit_counter == 8

            time.sleep(3)
            print(40 * "\n")

         # The game ends when someone has no more cards or
         # someone has all the quartetts.

        for x in best_choice :
            if x[1] == 4 or x[1] == 0 :   
                quit_counter += 1
        
        if quit_counter == 8 :
                print('Game ends')
                print('---------------------------------')
                print('Winner', ((player_list[i])[0]))
                print('ende')

