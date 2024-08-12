import random
import time

# Random sleep durations
sleep_short = random.uniform(1, 2)
sleep_duration = random.uniform(2, 4)
sleep_long = random.uniform(5, 7)

class color:
    RED = '\033[91m' #red
    GREEN = '\033[92m'#green
    YELLOW = '\033[93m'#yellow
    BLUE = '\033[94m' #blue
    MAGENTA = '\033[95m'#purple
    WHITE = '\033[97m' #white
    END = '\033[0m'
def additem(inv, item_id, name, quantity, value, power, mana, stamina, health, summonslots, equipable, equiped, rarity): #adding items to inventory
    color_code = colorcode(rarity)
    if item_id in inv:
        inv[item_id]['quantity'] += quantity
        print(f"Added {quantity} more of {color_code}{name}{color.END}.")
    else:
        inv[item_id] = {'name': name, 'quantity': quantity, 'value': value, 'power' : power, 'mana' : mana, 'stamina': stamina, 'health' : health, 'summon slots':summonslots, 'equipable?': equipable, 'equiped?': equiped, 'rarity': rarity}
        print(f"Picked up a new item: {color_code}{name}{color.END}")
def removeitem(inv, item_id, quantity): #REMOVE ITEM FROM INVENTORY
    rarity = inv[item_id]['rarity']
    color_code = colorcode(rarity)
    if item_id in inv:
        if inv[item_id]['quantity'] >= quantity:
            inv[item_id]['quantity'] -= quantity
            if inv[item_id]['quantity'] == 0:
                del inv[item_id]
            print(f"Used {quantity} of {color_code}{inventory[item_id]['name']}{color.END}.")
        else:
            print("Not enough of this item.")
    else:
        print("Item not found in inventory.")
# Global variables
health = 100
stamina = 100
mana = 100
power = 0
summonslots = 0
spec = "none"
name = ""
equipeditems = {

}
inv = {
}#PLAYER INVENTORY
def colorcode(rarity):
    color_map = {
        'mythic': color.RED,
        'uncommon': color.GREEN,
        'legendary': color.YELLOW,
        'rare': color.BLUE,
        'quest': color.MAGENTA,
        'common': color.WHITE
    }
    return color_map.get(rarity.lower(), color.END)

def inventory():
    print("Inventory:")
    for item_id, details in inv.items():
        name = details['name']
        quantity = details['quantity']
        value = details['value']
        rarity = details['rarity']
        color_code = colorcode(rarity)  # Get the color code for the rarity
        print(f"Name: {color_code}{name}{color.END}, Quantity: {quantity}, Value: {value}, Rarity: {rarity}")
    invquestion = input("Would you like to 'Go Back', 'Equip', or 'Use'").lower().strip()
    if invquestion == "go back":
        mainplaymenu()
    elif invquestion == "Equip":
        pass
    elif invquestion == "Use":
        pass
    else:
        print("invalid input, 'Go Back', 'Equip', or 'Use'")
        
def quests():
    print("quests")
def stats():
    print("stats")
def town():
    print("town")
def gear():
    global health, stamina, mana, power, summonslots, spec
    print("Equiped Gear:")
    print(f"Power:{power} Health:{health} Mana:{mana} Stamina:{stamina}")
    if spec == "necromancer":
        print(f"Summon Slots: {summonslots}")
    for item_id, details in equipeditems.items():
        name = details['name']
        health = details['health']
        power = details['power']
        mana = details['mana']
        stamina = details['stamina']
        summonslots = details['summonslots']
        print(name)
        if details['health'] >1:
            print('+' + health + ' Health')
            
        elif details['health'] <0:
            print('-' + health + ' Health')
            
        elif details['power'] >1:
            print('+' + power + ' Power')
            
        elif details['power'] <0:
            print('-' + power + ' Power')
            
        elif details['mana'] >1:
            print('+' + mana + 'Mana')

        elif details['mana'] <0:
            print('-' + mana + 'Mana')

        elif details['stamina'] >1:
            print('+' + stamina + 'Stamina')

        elif details['stamina'] <0:
            print('-' + stamina + 'Stamina')

        elif details['summonslots'] >1:
            print('+' + summonslots + 'Summon Slots')

        elif details['summonslots'] <0:
            print('-' + summonslots + 'Summon Slots')
            
            
def mainplaymenu():
    main = ("inventory", "quests", "stats", "Look around", "Equips")
    print(main)
    selectedinmenu = False
    while selectedinmenu is not True:
        navigateinv = input("where would you like to go?").strip().lower()
        if navigateinv == "inventory":
            inventory()
            selectedinmenu = True
        elif navigateinv == "quests":
            quests()
            selectedinmenu = True
        elif navigateinv == "stats":
            stats()
            selectedinmenu = True
        elif navigateinv == "look around":
            town()
            selectedinmenu = True
        elif navigateinv == "equips":
            gear()
            selectedinmenu = True
        else:
            print("invalid input, choose one of these options:")
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
def checkclass():
    mainclass()
    youchose()
    readstats()
    startofadventure()
def startofgame():
    global health, stamina, mana, power, summonslots, spec
    health = 100
    stamina = 100
    mana = 100
    power = 0
    summonslots = 0
    nameis()
    purpose()
    checkclass()
    starttown()
    mildewvillage()
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
    time.sleep(sleep_duration)
    readd = False
    while not readd:
        read = input("have you read your stats? ").strip().lower()
        if read == "yes":
            readd = True
        elif read == "no":
            readstats()
        else:
            print("invalid input, yes or no")
def startofadventure():
    time.sleep(sleep_short)
    starttt = False
    while not starttt:
        print("This is the start of your journey, are you sure you want that class for the rest of it?")#inv, item_id, name, quantity, value, power, mana, stamina, health, summonslots, equiped, equipable, rarity
        finalizeclass = input("Yes or No ").strip().lower()
        if finalizeclass == "yes":
            if spec == "necromancer":
                additem(inv, "SHstaff", "Minor Staff of the Undead", 1, 100, 5, 15, 5, 0, 0,'yes','no', 'uncommon')
                additem(inv, "robe", "Shoddy Black Robe", 1, 15, 0, 50, 5, 50, 0,'yes','no', 'common')
                additem(inv, "SHtome", "Common Tome of Necromancy", 1, 0, 0, 0, 0, 0, 1,'yes','no', 'common')
                additem(inv, "Potion", "Lesser Mana Potion", 3, 25, 0, 0, 0, 0, 0,'no','no', 'uncommon')
                additem(inv, "Potion", "Lesser Healing Potion", 2, 20, 0, 0, 0, 0, 0,'no','no', 'common')
                starttt = True
            elif spec == "brawler":
                additem(inv, "BHweapon", "Cracked Stone Cestus", 1, 12, 25, 0, -12, 15, 0,'yes','no', 'common')
                additem(inv, "Arms", "Fighters Wraps", 1, 15, 10, 0, 25, 10, 0,'yes','no', 'uncommon')
                additem(inv, "Armor", "Leather Patchwork Armor", 1, 100, 0, 0, 10, 100, 0,'yes','no', 'common')
                additem(inv, "Potion", "Lesser Healing Potion", 5, 20, 0, 0, 0, 0, 0,'no','no', 'common')
                starttt = True
            elif spec == "warlock":
                 #KEEPWORKING ON THIS HEREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
                pass
        elif finalizeclass == "no":
            time.sleep(sleep_short)
            print("choose well friend")
            starttt = True
            checkclass()
        else:
            print("invalid input, yes or no")
def starttown():
    print("you begin your journey in mildew village, a small town with a rough population of 28, there may be a few things to do around town.")
    time.sleep(sleep_duration)
def mildewvillage():
    mainplaymenu()
    global location
    global playerlocation
    location = mildewvillage
    playerlocation = mildewvillage
    
# Start the game
startofgame()
