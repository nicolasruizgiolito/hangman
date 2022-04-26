import random 
import time 
from character import character
from search_word import search_word
import os 


#This function allow us to search a word that will be use later on the game
def choose_word():
    with open("words_list.txt", 'r') as f:
        words = f.read().splitlines()
        word = random.choice(words)
        f.close()
        return word


#This is the main fuction on the program that contains the game logic. It recives the chosen word that will be guessed as a parameter. 
def play(word):
    #This variable will enable us to know if the player has won. If he does, we break the while loop.
    victory = False
    #With this three variables we will set the score
    start = time.time()
    errors = 0
    hits = 0

    #With this list comprehension we will show the progress
    progress = ['_ ' for words in word]


    #In this list we will gather all the letters that has been used
    letters_used = []

    #We create a list with the letters of the word that it's been guessed for comparing to the player's progress and see if he has won. 
    final_word = [(i + ' ') for i in word]

    while errors < 6:
        #We call the character funcition from the character document to show the hangman draw according to the amount of errors.
        character(errors, word)
    
        print('*******************')

        #We print the player's progress
        print('Word to be guessed: ',''.join(progress))

        print('*******************')

        #We print the letters used so far
        print('Letters used: ', letters_used)

        print('*******************')

        #We ask a letter
        letter = input('Enter a letter: ')
        os.system("cls")


        #We use a simple sequential search algorithm to see if the letter is already used
        if letter in letters_used:
            os.system("cls")
            print('You have already used this letter')
        else: 
            #If the letter has not been used we add it to the list
            letters_used.append(letter)

            mistake = True

            #Now we look if the letter is in the word
            for i in range(len(word)):
                #If so, we add the letter to the progress list 
                if word[i] == letter:
                    progress[i] = letter + ' '
                    mistake = False
                    hits += 1
                    #If not, we add and error
            if mistake:
                errors += 1

            #We check if the player has won and calculate his score. If not we break de while loop
            if final_word == progress:
                victory = True
                end = time.time()
                time_spend = end - start
                print()
                print(f'You won!')
                print()
                print('The word was: ', ''.join(progress))
                score(errors, time_spend, hits)
                break


    #If the player won, we ask if he wants to play once more time or if he wants to go back to the main menu           
    if victory == True:
        while True:
            option = input("Enter 'm' if you want to go back to the main manu or 'p' to play again: ")
            if option == 'm':
                os.system("cls")
                hangman_menu()
                break 
            elif option == 'p':
                os.system("cls")
                play(choose_word())
            else:
                input('Enter a valid option ')


    #We do the same if he loses          
    if victory == False: 
        end = time.time()
        time_spend = end - start          
        character(errors, word)
        print()
        print('You lost!')
        print()
        print(f'The word was: {word}')   
        print()
        score(errors, time_spend, hits)
        print()
        while True:
            option = input("Enter 'm' if you want to go back to the main manu or 'p' to play again: ")
            if option == 'm':
                os.system("cls")
                hangman_menu()
                break 
            elif option == 'p':
                os.system("cls")
                play(choose_word())
            else:
                input('Enter a valid option ')        

#This function enables us to add a new word to the list 
def add_word():
    #We open the txt file
    with open('words_list.txt', 'a') as f:
        print("If you want to return to the main menu enter 'm'")
        print()
        word_to_add = input('Enter a new word to the list: ').lower()
        os.system("cls")
        #We search if the word is already on the list
        while search_word(word_to_add) == True:
            print('That word is already on the list!')
            word_to_add = input('Please, enter another one: ')
            search_word(word_to_add)
        else:
            #If it's not on the list, we add it
            print()
            if word_to_add != 'm':
                print("The word", word_to_add, "will be added")
                print("If you want to continue please enter 'ok', otherwise you'll return to the menu: ")
                confirmation = input().lower()
                if confirmation == 'ok':
                    f.write(word_to_add + '\n')
                    f.close()
                    print('The word has been added.')
                    print('You will return to the menu now.')
                    time.sleep(5)
                    os.system("cls")
                    hangman_menu()
                else:
                    hangman_menu()
            else:
                os.system("cls")
                hangman_menu()

#main manu
def hangman_menu():
    print('''

    ******WELCOME TO HANGMAN GAME******

    Choose an option: 
    
    1. Play
    2. Add a new word
    3. Quit

    *******************************

    ''')

    option = (input(''))

    print()

    if option == '1':
        os.system("cls")
        palabra = choose_word()
        play(palabra)
    elif option == '2':
        os.system("cls")
        add_word()
    elif option == '3':
        os.system("cls")
        print('Thanks for playing!')
        time.sleep(3)
        quit()
    else:
        os.system("cls")
        print('Please, enter a valid option:')
        hangman_menu()



#This function calculates the score
def score(errors, time_spend, hits):
    final_score = 0

    #If the player was able to guess at least one letter, we add 50 points each
    if hits > 0:
        final_score += hits * 50

    #Depending on the number of errors we add a score
    if errors == 0:
        final_score += 60000
    elif errors == 1:
        final_score += 50000
    elif errors == 2:
        final_score += 40000
    elif errors == 3:
        final_score += 30000
    elif errors == 4:
        final_score += 20000
    elif errors == 5:
        final_score += 10000
    
    #If the player wins, we consider time as a socre variable
    if errors < 6:
        if time_spend < 5:
            final_score += 10000 
        elif time_spend <= 10:
            final_score += 9000 
        elif time_spend <= 15:
            final_score += 8000 
        elif time_spend <= 20:
            final_score += 7000 
        elif time_spend <= 25:
            final_score += 6000 
        elif time_spend <= 30:
            final_score += 5000 
        elif time_spend <= 35:
            final_score += 4000 
        elif time_spend <= 40:
            final_score += 3000 
        elif time_spend <= 45:
            final_score += 2000 
        elif time_spend <= 50:
            final_score += 1000
    
    print(f'Your final score is {final_score}')

if __name__ == '__main__':
    print('hello')
    hangman_menu()   

