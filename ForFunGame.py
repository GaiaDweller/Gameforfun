import random
import time
sleep_short = random.uniform(1,2)
sleep_duration = random.uniform(2, 4)
sleep_long = random.uniform(5, 10)


global health
global stamina
global mana
global power

def startofgame():
    health = 100
    stamina = 100
    mana = 100
    power = 0
    nameis()
def startagain():
    startofgame()

def isplayeralive():
#checks if the players health is above 1, if it isnt the game will trigger a restart
    if health >= 1:
        alive = True
    else:
        alive = False
    if alive == False:
        print("you have failed " + name + " you will meet your family again, goodbye friend")
        time.sleep(sleep_long)
        print("oh, youre still here?")
        time.sleep(sleep_duration)
        print("would you like to stay? To start a new journey?")
        time.sleep(sleep_short)
        startagain = input("will you continue your journey for revenge in another life traveler?").lower().strip()
        if startagain == "yes":
            print("thank you friend, may not remember you when you return, thank you...")
            time.sleep(sleep_long)
            startagain()
        if startagain == "no":
            print("thank you for playing friend")
        else:
            print("play again?(yes or no)")
def nameis(): #asks the players name
    global name
    name = input("what is your name traveler? ").strip()
    time.sleep(sleep_duration)
    print("hello " + name + " welcome to your journey")
    time.sleep(sleep_short)
def purpose():
    fam = False #simple lore
    while fam != True:
        family = input("do you have a family " + name + "? ").strip().lower()
        if family == "yes":
            print("no longer my friend")
            time.sleep(sleep_short)
            fam = True
        elif family == "no":
            time.sleep(sleep_short)
            print("my condolences " + name)
            fam = True
        else:
            print("invalid answer, yes or no.")
        
def mainclass(): #choosing main class for the entire game
    global choice
    global health
    global stamina
    global mana
    global power
    choice = False
    global spec
    while not choice:
        time.sleep(sleep_short)
        spec = input(" im sorry for your loss, your family was killed by an evil wizard, what class will you choose to avenge your family? (warlock,brawler,swordsman,necromancer) ").strip().lower()
        if spec == "warlock":
            power = 5#damage
            stamina = 60#stamina
            mana = 200#mana
            health = 115#health, self explanatory^^
            choice = True
        elif spec == "brawler":
            power = 20
            stamina = 125
            mana = 40
            health = 175
            choice = True
        elif spec == "swordsman":
            power = 10
            stamina = 145
            mana = 30
            health = 150
            choice = True
        elif spec == "necromancer":
            global summonslots
            power = 1
            stamina = 75
            mana = 250
            health = 105
            summonslots = 1
            choice = True
        else:
            print("invalid input")

def youchose():
    if spec == ["swordsman", "brawler", "warlock"]: #WORK ON THIS NOWWWWWWWWWWWWWWWWWWWW
        print("you have chosen: " + spec)
        print("power is " + str(power))
        print("stamina is " + str(stamina))
        print("mana is " + str(mana))
        print("health is " + str(health))
    if spec == "necromancer":
        print("you have chosen: " + spec)
        print("power is " + str(power))
        print("stamina is " + str(stamina))
        print("mana is " + str(mana))
        print("health is " + str(health))
        print("you have " + str(summonslots) + " summoning slots")
    pass









#main game
startofgame()
purpose()
mainclass()
youchose()



