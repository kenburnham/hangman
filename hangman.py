import random as ran
import numpy as np
import os

#FUNCTION prints out chart 
def print_chart(mistakes):
    print("\n\n")
    if(mistakes == 0):
        print("   |-----------|")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("              _|_")
    elif(mistakes == 1):
        print("   |-----------|")
        print("  (_)          |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("              _|_")
    elif(mistakes == 2):
        print("   |-----------|")
        print("  (_)          |")
        print("  \|           |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("              _|_")
    elif(mistakes == 3):
        print("   |-----------|")
        print("  (_)          |")
        print("  \|/          |")
        print("   |           |")
        print("               |")
        print("               |")
        print("               |")
        print("              _|_")
    elif(mistakes == 4):
        print("   |-----------|")
        print("  (_)          |")
        print("  \|/          |")
        print("   |           |")
        print("  /            |")
        print("               |")
        print("               |")
        print("              _|_")
    elif(mistakes == 5):
        print("   |-----------|")
        print("  (_)          |")
        print("  \|/          |")
        print("   |           |")
        print("  / \          |")
        print("               |")
        print("               |")
        print("              _|_")



#FUNCTION - handles each iteration of game  
def play(line_count, directory):

    #Calling Random Word function
    entry = random_word(line_count, directory)

    #Making random word a list rather than string
    word = list(entry)
    mistakes = 0
    #List of what has been correctly guessed, with -'s where unguessed
    uncovered = np.array(['-'] * len(word))
    #Keeps track of guessed letters
    guessed = np.array(['-'] * 26)
    #When won = 1 it will break while loop, symbolizing player won the game
    won = 0
    #Keeps track of how many characters of the word have been correctly guessed
    completed = 0
    #line_len helps with drawing textbox, based off of how long word is
    line_len = len(entry)*2 + 9

    #Start the Game
    while(mistakes < 5 and won == 0):
        print_chart(mistakes)

        #Printing out the text box around the Remaining Answer
        i = 0
        print(" ", end = '')
        while i < line_len:
            print("-", end='')
            i += 1
        print("\n| Answer:", end=' ')
        i = 0
        for i in uncovered:
            print(i, end=' ')
        print("|\n ", end ='')
        i = 0
        while i < line_len:
            print("-", end='')
            i += 1
        #Printing out letters that have been guessed so far
        print("\nGuessed: ", end= ' ')
        for index, val in enumerate(guessed):
            if val != '-':
                print(val, end=' ')
        
        #Receiving guess from user, and then checking if it is valid
        letter = input("\n\nGuess the next letter: ")
        letter_guess = 0
        while letter_guess == 0:
            #If is string, or not alphabet, rquest new letter
            if len(letter) != 1:
                letter = input("Please enter only one letter. Try again: ")
            elif letter.isalpha():
                letter_guess = 1
            else:
                letter = input("Please only enter in alphabetic letters. Try again: ")

        #ASSUMING APPROVED LETTER
        #if letter in word loop through word and finds index, swapping to - to ensure
        #it does not get picked up as an accepted guess next time
        # else - adds a mistake 
        if letter.upper() in word:
            for index, val in enumerate(word):
                if val == letter.upper():
                    uncovered[index] = letter.upper()
                    word[index] = '-'
                    completed += 1
                    if completed == len(word):
                        print("\nCongratulations! The correct word was: ", entry)
                        won = 1
        else:
            mistakes += 1
            if(won == 0 and mistakes == 5):
                print_chart(5)
                print("Game Over! The correct word was: ", entry)
        #Adds letter to already guessed list
        spot = 0
        for index, val in enumerate(guessed):
            if val != '-':
                spot +=1
        guessed[spot] = letter.upper()
    return won

#FUNCTION - Pulls word from random line from file via directory variable. 
def random_word(line_count, directory):
    catch_val = ran.randrange(line_count)
    with open(directory) as file:
        for index, line in enumerate(file):
            if(index == catch_val):
                #Strips off new line at end of line
                game_word = line.strip()
    file.close()
    #returns the UPPER CASE version of word
    return game_word.upper()

#Prints out stats of game
def stats(victories, losses):
    games = victories + losses
    if(games > 0):
        win_per = (victories/games)*100
    else:
        win_per = 0
    print(f'\n-------------\nGames Played: {games} \nGames Won: {victories} \nGames Lost: {losses} \nWinning Percentage: {win_per:.2f}%\n-------------')
  
#MAIN FUNCTION 
print("Welcome to Hang Man!")
print("--------------------\n")
response = 1
victories = 0
losses = 0
line_count = 0
directory = os.getcwd() + "/hangman_words.txt"

#Opens file of words and calculates how many lines are in file
with open(directory) as file:
    for line in file:
        line_count += 1
file.close()

#Ask user what would like to do:
while response != 3:
    print("Please Select from the Menu:")
    print("  1. Play Again")
    print("  2. Print out statistics")
    print("  3. Exit simulation")
    user_in = input("\n>: ")
    #Received user input, while input is not a number, ask again
    num_true = 0
    while num_true == 0:
        if user_in.isnumeric():
            response = int(user_in)
            num_true = 1
        else:
            print("Invalid - Try again. Please enter a number. ")
            user_in = input("\n>: ")

    #If win, result = 1, if lose, result = 0
    if response == 1:
        result = play(line_count, directory)
        if result == 1:
            victories += 1
            print("Your record is now ", victories, "-", losses, "!\n")
        elif result == 0:
            losses += 1
            print("You'll get them next time! Your record is now ", victories, "-", losses, "!\n")
    elif response == 2:
        stats(victories, losses)
    elif response == 3:
        print("Thanks for playing!")
    else: 
        print("Invalid entry, please try again!")




