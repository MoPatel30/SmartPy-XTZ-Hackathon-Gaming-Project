import smartpy as sp
import random





class Game(sp.Contract):
    def __init__(self):
        self.init(
            # playerOne = sp.address(addressOne)
            # playerTwo = sp.address(addressTwo)
            
            bet = sp.nat(0),
            
            record_player_wins = {
                "player_one" : sp.nat(0),
                "player_two" : sp.nat(0)
            }
           
        )
        
        
    @sp.entry_point
    def playerWins(self, player):
        self.data.record_player_wins[player] += 1
        
        
    @sp.entry_point
    def betting(self, amount):
        self.data.bet =  amount
        
        
    


def startGame():
    
      
    alert("Enter betting amount in mxtz (1,000,000 mxtz = 1 xtz): ")
    bettingAmount = input()
  
    alert("Welcome to Betting Against the Odds!" + '\n' + "Guess seven random numbers between 0-100 and the closest for the majority number will win the pot." + '\n' + "Important: Be sure to only bet what you're willing to lose!" + '\n' + "Good Luck!")
    alert("Player One enter seven guesses ranging from 0-100: ")
    
    
    
   # alert("Agree upon a betting amount and enter here: ")
#    bettingAmount = input()
#    currentBet = float(bettingAmount)
    
#    sp.betting()
 
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
    
    temp = determineWinner(guessesOne, guessesTwo, randNums, bettingAmount)
    return temp
    


def determineWinner(plyr_one_guesses, plyr_two_guesses, rand_nums, amount):
    rounds = [0,0,0]
   
    
    length = len(plyr_one_guesses)
    
    for i in range(length):
        if plyr_one_guesses[i] == "":
            plyr_one_guesses[i] = "0"
            
        if plyr_two_guesses[i] == "":
            plyr_two_guesses[i] = "0"
        
    for i in range(length):
        if abs(int(plyr_one_guesses[i]) - rand_nums[i]) < abs(int(plyr_two_guesses[i]) - rand_nums[i]):
            #scenario += test_game.playerWins("player_one")
            rounds[0] += 1
            
        if abs(int(plyr_one_guesses[i]) - rand_nums[i]) == abs(int(plyr_two_guesses[i]) - rand_nums[i]):
            rounds[2] += 1
            continue
        if abs(int(plyr_one_guesses[i]) - rand_nums[i]) > abs(int(plyr_two_guesses[i]) - rand_nums[i]):
            #scenario += test_game.playerWins("player_two")
            rounds[1] += 1
            
       
            
    if rounds[0] > rounds[1]:
        alert("Player One Wins!!!"  + "\n" + "Winning pot recieved: " + amount + " mxtz" + "\n" + str(rounds[0]) + " rounds won!" + "\n" + str(rounds[1]) + " rounds lossed :(" + "\n" + str(rounds[2]) + " rounds tied...")
        
    if rounds[0] == rounds[1]:
        alert("Game Tied! Prepare for next round!")
        startGame()
    if rounds[0] < rounds[1]:
        alert("Player Two Wins!!!"  + "\n" + "Winning pot recieved: " + amount + " mxtz" + "\n" + str(rounds[1]) + " rounds won!" + "\n" + str(rounds[0]) + " rounds lossed :(" + "\n" + str(rounds[2]) + " rounds tied...")
    
    
    rounds.append(amount)
    
    alert("Want to start a new game? Enter (y/n)")
    newGame = input()
    if newGame == "y":
        startGame()
        
    return rounds
    
    
    
 
@sp.add_test(name = "Test Game Contract")
def test():
    tester = startGame()
    
    scenario = sp.test_scenario()
                
    test_game = Game()
                
    scenario += test_game
    scenario += test_game.betting(int(tester[3]))
    
      
    for i in range(tester[0]):
        scenario += test_game.playerWins("player_one")
       
        
        
    for j in range(tester[1]):
        scenario += test_game.playerWins("player_two")
        
    
    
    
            
    