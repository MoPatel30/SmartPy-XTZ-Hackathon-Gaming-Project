import smartpy as sp
import random



class Game(sp.Contract):
    def __init__(self):

        self.init(
            
            
            record_player_wins = {
                "Player One" : sp.nat(0),
                "Player Two" : sp.nat(0),
                "Draw" : sp.nat(0)
                
            }
           
           
        )
        
    
       
    @sp.entry_point
    def playerWins(self, player):
        self.data.record_player_wins[player] += 1
        

        
        
def startGame():
      
  
    alert("Welcome to Betting Against the Odds!" + '\n' + "Guess seven random numbers between 0-100 and the closest for the majority of the numbers will win and be able to post a message to the blockchain." + '\n' + "Good Luck!")
    
    alert("Player one enter username: ")
    player_one_name = input()
    
    alert("Player two enter username: ")
    player_two_name = input()
    alert(str(player_one_name) + " enter seven guesses ranging from 0-100: ")
    
    

 
    guessOne = input()
    guessTwo = input()
    guessThree = input()
    guessFour = input()
    guessFive = input()
    guessSix = input()
    guessSeven = input()
    
    guessesOne = [guessOne, guessTwo, guessThree, guessFour, guessFive, guessSix, guessSeven]
    
    
    
    alert(str(player_two_name) + " enter seven guesses ranging from 0-100: ")
    
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
    
    
    alert(player_one_name + " Guesses: " + guessOne + ", " + guessTwo + ", " + guessThree +  ", " + guessFour +  ", " + guessFive +  ", " + guessSix +  ", " + guessSeven)
    
    alert(player_two_name + " Guesses: " + TwoguessOne + ", " + TwoguessTwo + ", " + TwoguessThree +  ", " + TwoguessFour +  ", " + TwoguessFive +  ", " + TwoguessSix +  ", " + TwoguessSeven)
    
    alert("generated Numbers: "  + str(randNumOne) + ", " + str(randNumTwo) + ", " + str(randNumThree) +  ", " + str(randNumFour) +  ", " + str(randNumFive) +  ", " + str(randNumSix) +  ", " + str(randNumSeven))

    temp = determineWinner(guessesOne, guessesTwo, randNums,  player_one_name,  player_two_name)
    #temp.append(addressOne)
    #temp.append(addressTwo)
    temp.append(player_one_name)
    temp.append(player_two_name)
    return temp
    


def determineWinner(plyr_one_guesses, plyr_two_guesses, rand_nums, player_one_name,  player_two_name):
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
        alert(player_one_name + " Wins!!!"  + "\n" + str(rounds[0]) + " rounds won!" + "\n" + str(rounds[1]) + " rounds lossed :(" + "\n" + str(rounds[2]) + " rounds tied...")
        
    if rounds[0] == rounds[1]:
        alert("Game Tied! Prepare for next round!")
        startGame()
        
    if rounds[0] < rounds[1]:
        alert(player_two_name +  " Wins!!!" + "\n" + str(rounds[1]) + " rounds won!" + "\n" + str(rounds[0]) + " rounds lossed :(" + "\n" + str(rounds[2]) + " rounds tied...")
    
  
    

    return rounds
    
    
    
 
@sp.add_test(name = "Test Game Contract")
def test():
    tester = startGame()
    
    scenario = sp.test_scenario()
    

    test_game = Game()
                
    scenario += test_game
    
    
    #test_game.data.record_player_wins[tester[3]] = test_game.data.record_player_wins.pop(test_game    .data.record_player_wins["player_one"])
    #del test_game.data.record_player_wins["player_one"]
    
    #test_game.data.record_player_wins[tester[4]] = test_game.data.record_player_wins.pop(test_game.data.record_player_wins["player_two"])
    #del test_game.data.record_player_wins["player_two"]
    
    for i in range(tester[2]):
        scenario += test_game.playerWins("Draw")
    
      
    for i in range(tester[0]):
        scenario += test_game.playerWins("Player One")
        
        
    for j in range(tester[1]):
        scenario += test_game.playerWins("Player Two")
        
"""
 How to Deploy a Smart Contract in 10 Steps!
 
 1. After running the game by clicking “Run” on the command bar, information will be outputted to right panel of the SmartPy editor. 
 Navigate to the “Michelson” tab and click “Deploy Contract”
 2. A testnet private key to deploy the contract is required. At time of writing, the primary test is carthagenet.
 3. Pressing Tezos Faucet Importer will bring us to SmartPy’s built-in utility for generating private keys from an Alphanet Faucet account file, 
 despite the name, the accounts generated by this faucet works across various test nets.
 4. After getting JSON file from the Alphabet Faucet, copy the data into the provided text box 
 5. Click “compute your private key” in order to generate the private key
 6. Next, hit “activate account” and then hit “Reveal account
 7. Grab the private and then go back to the deployment view
 8. Paste the private key in the box labeled “Private Key: “ and then hit the box “check credentials and compute account public key hash.” 
 9. Next, select your favorite Tezos node and click “Deploy”
 10. A successful operation injection will output an address of the contract pending deployment, in this case, an address beginning with “KT1…. 

 Congratulations, you have successfully originated a smart contract on the tezos alphanet!
"""
        
