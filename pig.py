import random

print("\nWelcome to the dice game Pig! The goal is to be the first player to reach 100 points.")
print("\nOn each turn, the player will roll a die ...")
print("\n\t > If the result is 1, the player earns 0 points for their turn and it becomes the other player\'s turn.")
print("\n\t > If the player holds, the score from the turn is added to their total score and the other player goes.")

class RolledOneException(Exception):
    print("\n\tA one was rolled")
    pass

class Player:
  def __init__(self, plyrnum, rollstate, gtotal):
    self.plyrnum = plyrnum
    self.rollstate = rollstate
    self.gtotal = gtotal

class Die:
    def __init__(self):
        self.value = random.randint(1, 6)

    def roll(self):
        """Returns the rolled dice, or raises RolledOneException if 1."""

        self.value = random.randint(1, 6)
        if self.value == 1:
            raise RolledOneException

        return self.value


    def __str__(self):
        return str(self.value)
        

class State:
  def __init__(self, whoturn, status):
    self.whoturn = whoturn
    self.status = status


gamestate = State(1, "go")
player1 = Player(1, "rolling", 0)
player2 = Player(2, "rolling", 0)


while(gamestate.status == "go"):
    
    if(player1.rollstate == "rolling"):
        turntotal = 0
        print("\nIt is Player 1\'s turn. They have a total score of " + str(player1.gtotal) + " and a turn total of " + str(turntotal))
        response = input("\nPlease enter either an \'r\' to roll or an \'h\' to hold ... ")
        
        if(response == 'r'):
            value = Die()
            print("You rolled a ")
            print(value)
            print("Your current turn total is ")
            print(value)
        elif(response == 'h'):
            gamestate.whoturn == 2
            player1.rollstate == "stopping"
            print("Player 1 is holding. Their turn total = " + str(turntotal))
            
    elif(gamestate.status == "go" and player2.rollstate == "rolling"):
        if(gamestate.whoturn == 2):
            value = Die()
            print("Computer rolled a ")
            print(value)
            print("Player 2 turn total is " + str(turntotal))
        
           