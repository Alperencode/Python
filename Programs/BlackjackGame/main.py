import random
import time
import subprocess as sp
global gamecount
tmp = sp.call('color 3',shell=True)
gamecount = 0


def playagain():
    main()
    

def gameover():
    global gamecount
    gamecount += 1
    player.lose()
    print("\n====== You Crashed! ======")
    print("Game Over! \n")
    time.sleep(3)
    playagain()

def computerwon():
    global gamecount
    gamecount += 1
    player.lose()
    print("\nYour cards total:",player.cards)
    print("Computer cards total:",computer.cards,"\n")
    print("====== Computer Won ======")
    print("Game Over! \n".upper())
    time.sleep(3)
    playagain()

def draw():
    print("\nYour cards total:",player.cards)
    print("Computer cards total:",computer.cards,"\n")
    print("====== Its Draw! ======".upper())
    print("Game Over! \n")    
    time.sleep(3)
    playagain()

def won():
    global gamecount
    gamecount += 1
    player.won()
    print("")
    print("\nYour cards total:",player.cards)
    print("Computer cards total:",computer.cards)
    print("====== You Won! ======\n".upper())
    time.sleep(3)
    playagain()

def computerstour():
    time.sleep(1)
    print("")
    print("Computer hidden card was:",computer.hidden)
    ifstatement = computer.cards == 21 and player.cards == 21
    ifstatement2 = computer.cards == player.cards and computer.cards < 21
    loop4 = 1
    while loop4 == 1:
        if(computer.cards < player.cards or ifstatement2 == True):
            if(computer.cards < 21):
                computer.takecard()
                print("Computer took",computer.cards - computer.oldcards)
                computer.newcard = 0
                time.sleep(1)
            else:
                loop4 = 0
                won()
        elif(computer.cards == player.cards or ifstatement == True):
            if(computer.cards < 15):
                computer.takecard()
                print("Computer took",computer.cards - computer.oldcards)
                computer.newcard = 0
                time.sleep(1)
            else:
                draw()
        else:
            if(computer.cards <= 21):
                loop4 = 0
                computerwon()
            else:
                won()
    

def main():

    if(Player.count == 0):
        sp.call('cls',shell=True)
        print("\nPlease answer the questions like 'yes' or 'no'\n".upper())
        time.sleep(1.5)
        sp.call('cls',shell=True)
        print("\n========= BLACKJACK =========")
        loop6 = 1
        while loop6 == 1:
            tutorial = str(input("\nDo you wanna read tutorial?\nAnswer: "))
            tutorial = tutorial.upper()
            if(tutorial == "YES"):
                print("\nFirst, you and Computer will take 2 cards.")
                print("If you get over of 21, you will lose.")
                print("If you and computer under of 21, higher score till 21 will win\n")
                loop6 = 0
                time.sleep(2)
            elif(tutorial == "NO"):
                loop6 = 0
                time.sleep(1)
            else:
                print("Please select 'yes' or 'no'")
        playername = str(input("\nWhats your name?: "))
        playername = playername.strip()
        sp.call('cls',shell=True)
        print("\n========= BLACKJACK =========")
        global player
        player = Player(playername,random.randint(2,10),750)
        global computer
        computer = Computer("Computer",random.randint(2,10))
        game()
    else:
        sp.call('cls',shell=True)
        print("\n========= BLACKJACK =========")
        computer = Computer("Computer",random.randint(2,10))
        player.cards = 0
        player.cards = random.randint(2,10)
        game()

class Player:
    
    count = 0
    woncounter = 0
    outofcreditcounter = 0

    def __init__(self, name,cards,credit):
        self.credit = credit
        self.name = name 
        self.cards = cards
        Player.count += 1

    def takecard(self):
        Player.newcard = 0
        Player.oldcards = self.cards
        Player.newcard = random.randint(1,11)
        self.cards += Player.newcard
    
    def won(self):
        self.credit += 250
        Player.woncounter += 1

    def lose(self):
        self.credit -= 250
    
    def ascard(self):
        loop = 1
        while(loop == 1):
            x = input("\nDo you wanna take 1 or 11\nAnswer: ")
            x = str(x)
            if(x == "11"):
                loop = 0
                player.cards += 11
                print("You took 11")
            elif(x == "1"):
                loop = 0
                player.cards += 1
                print("You took 1")
            else:
                print("Please choose 1 or 11")


    def outofcredit(self):
        Player.outofcreditcounter += 1
        Player.woncounter = 0

class Computer:

    def __init__(self,name,cards):
        self.name = name
        self.cards = cards
        Computer.hidden = cards

    def takecard(self):
        Computer.oldcards = self.cards
        Computer.newcard = random.randint(2,10)
        self.cards += Computer.newcard
 
 
def game():
    global gamecount
    if(player.credit == 0):
        gamecount = 0
        player.outofcredit()
        print("Out of Credit!".upper())
        print("Game Over".upper())
        loop9 = 1
        while loop9 == 1: 
            again = str(input("\nDo you wanna play again? \nAnswer: "))
            again = again.upper()
            if(again == "YES"):
                loop9 = 0
                player.credit = 750
                playagain()
            elif(again == "NO"):
                loop9 = 0
                sp.call('cls',shell=True)
                print("Goodbye!\n")
                time.sleep(1)
                sp.call('cls',shell=True)
                quit()
            else:
                print("Please select 'yes' or 'no'")
    else:
        print("")
        print("Welcome", player.name+"!","====== Credit:",player.credit,"=== Games Won/Played: {}/{}".format(player.woncounter,gamecount))
        print("\nComputer Card 1: Hidden")
        computer.takecard()
        print("Computer Card 2:",computer.newcard)
        time.sleep(1)
        print("")
        print("Your Card 1:",player.cards)
        player.takecard()
        print("Your Card 2:",player.newcard)
        time.sleep(1)
        loop2 = 1
        while loop2 == 1:
            if(player.cards > 21):
                loop2 = 0
                print("Your cards total:",player.cards,"\n")
                gameover()
            else:
                print("Your cards total:",player.cards,"\n")
                question = str(input("Do you wanna take card? \nAnswer: "))
                question = question.upper()
                questionsplit = question.split()
                if("YES" in questionsplit):
                    player.takecard()
                    if(player.newcard == 1):
                        player.cards -= 1
                        print("\nYou took the As card")
                        time.sleep(1)
                        player.ascard()
                    elif(player.newcard == 11):
                        player.cards -= 11
                        print("\nYou took the As card")
                        time.sleep(1)
                        player.ascard()
                    else:
                        print("You took",player.cards - player.oldcards)
                        time.sleep(1)
                elif("NO" in questionsplit):
                    loop2 = 0
                    computerstour()
                else:
                    if("YES" in question[0:]):
                        player.takecard()
                        if(player.newcard == 1):
                            player.cards -= 1
                            print("\nYou took the As card")
                            time.sleep(1)
                            player.ascard()
                        elif(player.newcard == 11):
                            player.cards -= 11
                            print("\nYou took the As card")
                            time.sleep(1)
                            player.ascard()
                        else:
                            print("You took",player.cards - player.oldcards)
                            time.sleep(1)
                    elif("NO" in question[0:]):
                        loop2 = 0
                        computerstour()
                    else:
                        print("Please select 'yes' or 'no'")
                        

if __name__ == "__main__":
    main()
