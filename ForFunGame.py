import random
import time

# Random sleep durations
sleep_short = random.uniform(1, 2)
sleep_duration = random.uniform(2, 4)
sleep_long = random.uniform(5, 7)

# Global variables
health = 100
stamina = 100
mana = 100
power = 0
summonslots = 0
spec = "none"
name = ""
def mainplaymenu():
    main = ("inventory", "quests", "stats", "Look around")
    print(main)
def checkiffunccontinue(): #Developer tool to check if a repear function passes correctly
    wwasdsadas = input("did this pop up").strip().lower()
    time.sleep(sleep_short)
    if wwasdsadas == "yes":
        print("it worked")
    if wwasdsadas == "no":
        print("Liar")
def checklocation(): #CHECKS THE LOCATION OF A PLAYER, useful for if player is in wrong location for quest
    global locationcheck
    global playerlocation
    global location
    locationcheck = False
    if location == playerlocation:
        locationcheck = True
    else:
        print("you are in the wrong town for that")
        locationcheck = False
def startofgame():
    global health, stamina, mana, power, summonslots, spec
    health = 100
    stamina = 100
    mana = 100
    power = 0
    summonslots = 0
    nameis()
    purpose()
    def checkclass():
        mainclass()
        youchose()
        readstats()
        startofadventure()
    checkclass()
    
def startagain():
    startofgame()

def isplayeralive():
    global health, name
    if health < 1:
        print("You have failed " + name + ". You will meet your family again. Goodbye, friend.")
        time.sleep(sleep_long)
        print("Oh, you're still here?")
        time.sleep(sleep_duration)
        print("Would you like to stay? To start a new journey?")
        time.sleep(sleep_short)
        startagain_input = input("Will you continue your journey for revenge in another life traveler? (yes or no) ").lower().strip()
        if startagain_input == "yes":
            print("Thank you, friend. I may not remember you when you return. Thank you...")
            time.sleep(sleep_long)
            startagain()
        elif startagain_input == "no":
            print("Thank you for playing, friend.")
        else:
            print("Invalid answer. Please type 'yes' or 'no'.")
            isplayeralive()

def nameis(): # Asks the player's name
    global name
    name = input("What is your name, traveler? ").strip()
    time.sleep(sleep_short)
    print("Hello " + name + ", welcome to your journey.")
    time.sleep(sleep_short)

def purpose():
    global name
    fam = False
    while not fam:
        family = input("Do you have a family, " + name + "? ").strip().lower()
        if family == "yes":
            print("No longer my friend.")
            time.sleep(sleep_short)
            fam = True
        elif family == "no":
            time.sleep(sleep_short)
            print("My condolences, " + name + ".")
            fam = True
        else:
            print("Invalid answer. Please type 'yes' or 'no'.")

def mainclass(): # Choosing main class for the entire game
    global choice, health, stamina, mana, power, summonslots, spec
    choice = False
    while not choice:
        time.sleep(sleep_short)
        spec = input("I'm sorry for your loss. Your family was killed by an evil wizard. What class will you choose to avenge your family? (warlock, brawler, swordsman, necromancer) ").strip().lower()
        if spec == "warlock":
            power = 5
            stamina = 60
            mana = 200
            health = 115
            summonslots = 0
            choice = True
        elif spec == "brawler":
            power = 20
            stamina = 125
            mana = 40
            health = 175
            summonslots = 0
            choice = True
        elif spec == "swordsman":
            power = 10
            stamina = 145
            mana = 30
            health = 150
            summonslots = 0
            choice = True
        elif spec == "necromancer":
            power = 1
            stamina = 75
            mana = 250
            health = 105
            summonslots = 1
            choice = True
        else:
            print("Invalid input. Please choose a valid class.")

def youchose():
    global health, stamina, mana, power, summonslots, spec
    print("You have chosen: " + spec)
    print("Power is " + str(power))
    print("Stamina is " + str(stamina))
    print("Mana is " + str(mana))
    print("Health is " + str(health))
    if summonslots >= 1:
        print("You have " + str(summonslots) + " summon slot(s).")
def readstats():
    time.sleep(sleep_long)
    readd = False
    while not readd:
        read = input("have you read your stats? ").strip().lower()
        if read == "yes":
            readd = True
        if read == "no":
            readstats()
        else:
            print("invalid input, yes or no")
def startofadventure():
    time.sleep(sleep_short)
    starttt = False
    while not starttt:
        print("This is the start of your journey, are you sure you want that class for the rest of it?")
        finalizeclass = input("Yes or No ").strip().lower()
        if finalizeclass == "yes":
            starttown()
            starttt = True
        if finalizeclass == "no":
            time.sleep(sleep_short)
            print("choose well friend")
            starttt = True
            mainclass()
            youchose()
        else:
            print("invalid input, yes or no") #FIXTHISITSAYSIT
def starttown():
    print("you begin your journey in mildew village, a small town with a rough population of 28, there may be a few things to do around town.")
    time.sleep(sleep_duration)
    mildewvillage()
def mildewvillage():
    mainplaymenu()
    
# Start the game
startofgame()
