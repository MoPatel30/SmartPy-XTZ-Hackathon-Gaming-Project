import smartpy as sp
import random

    
def startGame():
    
    alert("Welcome to Betting Against the Odds!" + '\n' + "Guess seven random numbers between 0-100 and the closest for the majority number will win the pot." + '\n' + "Important: Be sure to only bet what you're willing to lose!" + '\n' + "Good Luck!")
    alert("Player One enter seven guesses ranging from 0-100: ")
    
    guessOne =  input()
    guessTwo = input()
    guessThree = input()
    guessFour = input()
    guessFive = input()
    guessSix = input()
    guessSeven = input()
    
    guessesOne = [guessOne, guessTwo, guessThree, guessFour, guessFive, guessSix, guessSeven]
    
    
    
    alert("Player Two enter seven guesses ranging from 0-100: ")
    TwoguessOne =  input()
    TwoguessTwo = input()
    TwoguessThree = input()
    TwoguessFour = input()
    TwoguessFive = input()
    TwoguessSix = input()
    TwoguessSeven = input()
    
    guessesTwo = [TwoguessOne, TwoguessTwo, TwoguessThree, TwoguessFour, TwoguessFive, TwoguessSix, TwoguessSeven]
    
    
    randNumOne = random.randint(0,101)
    randNumTwo = random.randint(0,101)
    randNumThree = random.randint(0,101)
    randNumFour = random.randint(0,101)
    randNumFive = random.randint(0,101)
    randNumSix = random.randint(0,101)
    randNumSeven = random.randint(0,101)
    
    randNums = [randNumOne, randNumTwo, randNumThree, randNumFour, randNumFive, randNumSix, randNumSeven]
    
    
    alert("Player One Guesses: " + guessOne + ", " + guessTwo + ", " + guessThree +  ", " + guessFour +  ", " + guessFive +  ", " + guessSix +  ", " + guessSeven)
    
    alert("Player Two Guesses: " + TwoguessOne + ", " + TwoguessTwo + ", " + TwoguessThree +  ", " + TwoguessFour +  ", " + TwoguessFive +  ", " + TwoguessSix +  ", " + TwoguessSeven)
    
    alert("generated Numbers: "  + str(randNumOne) + ", " + str(randNumTwo) + ", " + str(randNumThree) +  ", " + str(randNumFour) +  ", " + str(randNumFive) +  ", " + str(randNumSix) +  ", " + str(randNumSeven))
    
    determineWinner(guessesOne, guessesTwo, randNums)
    




def determineWinner(plyr_one_guesses, plyr_two_guesses, rand_nums):
    rounds = [0,0]
   
    
    length = len(plyr_one_guesses)
    
    
    for i in range(length):
        if abs(int(plyr_one_guesses[i]) - rand_nums[i]) < abs(int(plyr_two_guesses[i]) - rand_nums[i]):
            rounds[0] += 1
        if abs(int(plyr_one_guesses[i]) - rand_nums[i]) == abs(int(plyr_two_guesses[i]) - rand_nums[i]):
            continue
        else:
            rounds[1] += 1
            
            
    if rounds[0] > rounds[1]:
        alert("Player One Wins!!!")
        
    if rounds[0] == rounds[1]:
        alert("Game Tied! Prepare for next round!")
        startGame()
        
    else:
        alert("Player Two Wins!!!")
        
        
        
startGame()
            
    