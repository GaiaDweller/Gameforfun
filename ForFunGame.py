import random
import time

# Random sleep durations
sleep_short = random.uniform(1, 2)
sleep_duration = random.uniform(2, 4)
sleep_long = random.uniform(5, 7)
sleep_huge = random.uniform(7, 12)

#Global Variables
health = 100
stamina = 100
mana = 100
power = 1
gold = 100
summonslots = 0
currenthealth = 100
currentstamina = 100
currentmana = 100
opensummonslots = 100
spec = "none"
name = ""
town = ""
againinjohns = ""
firsttimeinmildew = 0
firsttimeinjohns = 0
firsttimegetjohnmeat = 0
firsttimeinednas = 0
ednagivingointment = 0
Goddessname = 'Narukya'
Darkgoddessname = 'Ire'
takenjohnsblessing = 0
completedquests = {}
currentquests = {}
unequipeditems = {}
newequipeditems ={}
equipeditems = {
    'Torso': {}, 'Legs': {}, 'Feet': {}, 'Arms': {}, 'Hands': {},
    'WeaponLeft': {}, 'WeaponRight': {}, 'WeaponBoth': {}, 'Head': {},
    'Wrist': {}, 'Earings': {}, 'Ring': {}, 'Necklace': {}
}
inv = {

    }  # PLAYER INVENTORY
FORWEAPONS = {
    "FullLeft": {'name': 'Full', 'quantity': 1, 'value': 0, 'power': 0, 'mana': 0,
            'stamina': 0, 'health': 0, 'summonslots': 0, 'equipable': 'yes',
            'rarity': 'common', 'slot': 'WeaponLeft'},
    "FullRight": {'name': 'Full', 'quantity': 1, 'value': 0, 'power': 0, 'mana': 0,
            'stamina': 0, 'health': 0, 'summonslots': 0, 'equipable': 'yes',
            'rarity': 'common', 'slot': 'WeaponRight'},
    "FullBoth": {'name': 'Full', 'quantity': 1, 'value': 0, 'power': 0, 'mana': 0,
            'stamina': 0, 'health': 0, 'summonslots': 0, 'equipable': 'yes',
            'rarity': 'common', 'slot': 'WeaponBoth'},
    }
NecromancerSummons = {}
class Color:
    RED = '\033[91m'   # red
    GREEN = '\033[92m' # green
    YELLOW = '\033[93m'# yellow
    BLUE = '\033[94m'  # blue
    MAGENTA = '\033[95m'# purple
    WHITE = '\033[97m' # white
    END = '\033[0m'
def losehealth(amount):
    print(f'You lost {amount} Health!')
    time.sleep(sleep_duration)
    currenthealth -= amount
def addlesserhealingpotion(quantity):
    additem(inv, "LHPotion", "Lesser Healing Potion", quantity, 20, 0, 0, 0, 50, 0,'no', 'common', 'none', 'yes', 'A potion that restores a small amount of health')
def addlessermanapotion(quantity):
    additem(inv, "LMPotion", "Lesser Mana Potion", quantity, 25, 0, 50, 0, 0, 0,'no', 'uncommon', 'none', 'yes', 'A potion that restores a small amount of mana.')
def colorcode(rarity):
    color_map = {
        'mythic': Color.RED,
        'uncommon': Color.GREEN,
        'legendary': Color.YELLOW,
        'rare': Color.BLUE,
        'quest': Color.MAGENTA,
        'common': Color.WHITE
    }
    return color_map.get(rarity.lower(), Color.END)
def addgold(amount):
    global gold
    print(f'+{amount} gold')
    gold += amount
def sellitem(itemsold): #EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
    global gold, inv
    print(f'-Sold {itemsold}')
    pass
def additem(inv, item_id, name, quantity, value, power, mana, stamina, health, summonslots, equipable, rarity, slot, consumable, description):
    color_code = colorcode(rarity)
    if item_id in inv:
        inv[item_id]['quantity'] += quantity
        print(f"Added {quantity} more of {color_code}{name}{Color.END}.")
    else:
        inv[item_id] = {
            'name': name, 'quantity': quantity, 'value': value, 'power': power, 'mana': mana,
            'stamina': stamina, 'health': health, 'summonslots': summonslots, 'equipable': equipable,
            'rarity': rarity, 'slot': slot, 'consumable' : consumable, 'description': description
        }
        print(f"Picked up a new item: {color_code}{name}{Color.END}")
def silentadditem(inv, item_id, name, quantity, value, power, mana, stamina, health, summonslots, equipable, rarity, slot, consumable, description):
    color_code = colorcode(rarity)
    if item_id in inv:
        inv[item_id]['quantity'] += quantity
    else:
        inv[item_id] = {
            'name': name, 'quantity': quantity, 'value': value, 'power': power, 'mana': mana,
            'stamina': stamina, 'health': health, 'summonslots': summonslots, 'equipable': equipable,
            'rarity': rarity, 'slot': slot, 'consumable' : consumable, 'description': description
        }
def silentremoveitem(inv, item_id, quantity):
    if item_id in inv:
        if inv[item_id]['quantity'] >= quantity:
            rarity = inv[item_id]['rarity']
            color_code = colorcode(rarity)
            inv[item_id]['quantity'] -= quantity
            if inv[item_id]['quantity'] == 0:
                del inv[item_id]
    else:
        print("Item not found in inventory.")

def removeitem(inv, item_id, quantity):
    if item_id in inv:
        if inv[item_id]['quantity'] >= quantity:
            rarity = inv[item_id]['rarity']
            color_code = colorcode(rarity)
            inv[item_id]['quantity'] -= quantity
            print(f"Used {quantity} of {color_code}{inv[item_id]['name']}{Color.END}.")
            if inv[item_id]['quantity'] == 0:
                del inv[item_id]

        else:
            print("Not enough of this item.")
    else:
        print("Item not found in inventory.")
def deleteitem(inv, item_id, quantity):
    if item_id in inv:
        if inv[item_id]['quantity'] >= quantity:
            rarity = inv[item_id]['rarity']
            color_code = colorcode(rarity)
            inv[item_id]['quantity'] -= quantity
            print(f"Deleted {quantity} of {color_code}{inv[item_id]['name']}{Color.END}.")
            if inv[item_id]['quantity'] == 0:
                del inv[item_id]

        else:
            print("Not enough of this item.")
    else:
        print("Item not found in inventory.")

def addquest(questname, description, town):
    global currentquests, completedquests

    if questname in completedquests:
        print('You have already completed this quest.')
    elif questname in currentquests:
        print("You are currently doing this quest.")
    else:
        print(f'{questname} added to quests')
        currentquests[questname] = {'Description': description, 'Location': town}

def finishedquest(questname):
    global currentquests, completedquests

    if questname in completedquests:
        pass
    elif questname in currentquests:
        questdetails = currentquests.pop(questname)
        completedquests[questname] = questdetails
        print(f'Completed {questname}')
    else:
        print(f'{questname} is not in your current quests.')


def display_item_stats(item):
    name = item.get('name', 'Unknown')
    stats = {
        'Health': item.get('health', 0),
        'Power': item.get('power', 0),
        'Mana': item.get('mana', 0),
        'Stamina': item.get('stamina', 0),
        'Summon Slots': item.get('summonslots', 0)
    }
    for stat, value in stats.items():
        if value != 0:
            print(f"{'+' if value > 0 else ''}{value} {stat}")



def checkcurrentstats():
    global health, currenthealth, currentstamina, currentmana, opensummonslots, summonslots, stamina, mana
    if currenthealth > health:
        currenthealth = health

    if currentmana > mana:
        currentmana = mana

    if currentstamina > stamina:
        currentstamina = stamina

    if opensummonslots > summonslots:
        opensummonslots = summonslots
def displaycurrentstats():
    global mana, health, stamina, summonslots, power, currenthealth, currentmana, currentstamina, opensummonslots, spec
    print(f'Power: {power}')
    print(f'Health: {currenthealth}/{health}')
    print(f'Stamina: {currentstamina}/{stamina}')
    print(f'Mana: {currentmana}/{mana}')
    if spec == 'necromancer':
        print(f'Summon Slots: {opensummonslots}/{summonslots}')
def doctorheal():
    global currenthealth, currentmana, currentstamina, mana, stamina, health
    if currenthealth < health or currentmana < mana or currentstamina < stamina:
        print('You rest after getting patched up...')
        time.sleep(sleep_duration)
        healed = health - currenthealth
        manarecovered = mana - currentmana
        staminarecovered = stamina - currentstamina
        if healed > 0:
            print(f'+{healed} Health')
            currenthealth = health
        if manarecovered > 0:
            print(f'+{manarecovered} Mana')
            currentmana = mana
        if staminarecovered > 0:
            print(f'+{staminarecovered} Stamina')
            currentstamina = stamina
        time.sleep(sleep_duration)
        print("You're completely healed, and well rested")
        displaycurrentstats()
        time.sleep(sleep_long)
        checkcurrentstats()
    else:
        time.sleep(sleep_short)
        print("You're in perfect health!")
        time.sleep(sleep_short)


def mildewvillagesquare():
    def Johnmildewshop():
        def johnsshop():
            global gold, equipeditems, inv
            print('John: Let me check what i have for you...')
            time.sleep(sleep_duration)
            print('''
                  Savory Meat: 100 Gold
                  Strongly Seasoned Meat: 75 Gold
                  Sharp Tasting Meat: 45 Gold
                  Steak: 30 Gold
                  Raw Meat: 15 Gold
''')
            buyingfromjohn = True
            while buyingfromjohn:
                print('John: What would you like to buy?')
                purchasefromjohn = input('Items name, (N)evermind, (S)ell').lower().strip()
                if purchasefromjohn == 'savory meat' or purchasefromjohn == 'strongly seasoned meat' or purchasefromjohn == 'sharp tasting meat' or purchasefromjohn == 'steak' or purchasefromjohn == 'raw meat' or purchasefromjohn == 'n':
                    buyingfromjohn = False
                if purchasefromjohn == 's':
                    sellingtojohn = True
                    buyingfromjohn = False
                else:
                    print('John: What was that?')

            while sellingtojohn == True:
                #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                print("\nInventory:")
                for item_id, details in inv.items():
                    name = details['name']
                    quantity = details['quantity']
                    value = details['value']
                    rarity = details['rarity']
                    description = details['description']
                    color_code = colorcode(rarity)  # Get the color code for the rarity
                    whitecolor = colorcode('common')

                    print(f"\nName: {color_code}{name}{Color.END}, Quantity: {quantity}, Value: {value}, Rarity: {rarity}, {whitecolor}Description: {description}{Color.END}")

                    itemtosell = input("John: What would you like to sell lad?")
            if purchasefromjohn == 'savory meat':
                howmanyy = True
                while howmanyy:
                    howmany = input('John: How Many? (N)evermind')
                    price = int(howmany) * 100
                    if gold >= price:
                        additem(inv, 'SM', 'Savory Meat', howmany, 50, 0, 25, 25, 125, 0, 'no', 'rare', None, 'yes', 'When you taste this meat, you will feel so many great emotions, John is an amazing cook...')
                        howmanyy = False
                    if howmany == 'n':
                        print('John: Alrighty then, Anything else?')
                        time.sleep(sleep_duration)
                        johnsshop()

                        howmanyy = False
                    else:
                        print('John: You dont have enough Gold!')
                        howmanyy = False

                        johnsshop()
            if purchasefromjohn == 'strongly seasoned meat':
                howmanyy = True
                while howmanyy:
                    howmany = input('John: How Many? (N)evermind')
                    price = int(howmany) * 75
                    if gold >= price:
                        additem(inv, 'SSM', 'Strongly Seasoned Meat', howmany, 30, 0, 15, 15, 70, 0, 'no', 'uncommon', None, 'yes', 'John is a great cook, this meat will keep you well fed and possibly accelerate your healing...')
                        howmanyy = False
                    if howmany == 'n':
                        print('John: Alrighty then, Anything else?')
                        time.sleep(sleep_duration)
                        johnsshop()

                        howmanyy = False
                    else:
                        print('John: You dont have enough Gold!')
                        howmanyy = False

                        johnsshop()
            if purchasefromjohn == 'sharp tasting meat':
                howmanyy = True
                while howmanyy:
                    howmany = input('John: How Many? (N)evermind')
                    price = int(howmany) * 45
                    if gold >= price:
                        additem(inv, 'STM', 'Sharp Tasting Meat', howmany, 20, 0, 10, 10, 45, 0, 'no', 'uncommon', None, 'yes', 'Meat with an interesting taste!')
                        howmanyy = False
                    if howmany == 'n':
                        print('John: Alrighty then, Anything else?')
                        time.sleep(sleep_duration)
                        johnsshop()

                        howmanyy = False
                    else:
                        print('John: You dont have enough Gold!')
                        howmanyy = False

                        johnsshop()
            if purchasefromjohn == 'steak':
                howmanyy = True
                while howmanyy:
                    howmany = input('John: How Many? (N)evermind')
                    price = int(howmany) * 30
                    if gold >= price:
                        additem(inv, 'S', 'Steak', howmany, 10, 0, 5, 5, 25, 0, 'no', 'common', None, 'yes', 'Steak, Blessed with johns great cooking...')
                        howmanyy = False
                    if howmany == 'n':
                        print('John: Alrighty then, Anything else?')
                        time.sleep(sleep_duration)
                        johnsshop()

                        howmanyy = False
                    else:
                        print('John: You dont have enough Gold!')
                        howmanyy = False

                        johnsshop()
            if purchasefromjohn == 'raw meat':
                howmanyy = True
                while howmanyy:
                    howmany = input('John: How Many? (N)evermind')
                    price = int(howmany) * 15
                    if gold >= price:
                        additem(inv, 'RM', 'Raw Meat', howmany, 30, 0, 2, 2, -15, 0, 'no', 'common', None, 'yes', 'Uncooked Meat, maybe you could cook it eventually?')
                        howmanyy = False
                    if howmany == 'n':
                        print('John: Alrighty then, Anything else?')
                        time.sleep(sleep_duration)
                        johnsshop()

                        howmanyy = False
                    else:
                        print('John: You dont have enough Gold!')
                        howmanyy = False

                        johnsshop()
            if purchasefromjohn == 'n':
                print('John: Alrighty then, if u need anything let me know!')
                time.sleep(sleep_duration)
                Johnmildewshop()

        def talkingtojohn():
            choosingjohnsblessing = True
            global name, Goddessname, spec, power, health, stamina, mana, summonslots, takenjohnsblessing, againinjohns
            color_code_purple = colorcode('quest')
            print('John: Of course kid, i always have time for you')
            time.sleep(sleep_short)
            print(f'You explain {againinjohns}what happened to your family in detail to John...')
            time.sleep(sleep_duration)
            print("John: so that what happened, I thought something was up when your parents hadn't come to my shop for over a week.")
            time.sleep(sleep_duration)
            print(f'John: Youre a good kid {name}, id hate it if something happened to you...')
            if takenjohnsblessing == 0:
                time.sleep(sleep_long)
                print(f'John: You know, I have a small gift i could give you, although its not much, I used to be a priest of the goddess {Goddessname}')
                time.sleep(sleep_long)
                print(f'John: before you go on your journey i want to bestow upon you a {color_code_purple}blessing{Color.END}')
                time.sleep(sleep_long)
                print('John: Choose wisely kid...')
                if spec == 'necromancer':
                    print('John: The Blessing of Power, The Blessing of Health, The Blessing of Endurance, The Blessing of Intellect')
                    time.sleep(sleep_long)
                    print('You feel something arise inside of you...')
                    time.sleep(sleep_long)
                    print('A goddess of darkness is contacting you...')
                    time.sleep(sleep_duration)
                    print("She offers you a 'blessing' of sorts, although you may want to be careful accepting it...If you accept she will alter the blessing from John...")
                    time.sleep(sleep_long)
                    print("John: You alright kid? Take as long as you want to decide, heres your options again kid.")
                    time.sleep(sleep_duration)
                while choosingjohnsblessing:
                    print('\nBlessing of (P)ower\nBlessing of (H)ealth\nBlessing of (E)ndurance\nBlessing of (I)ntelect')
                    if spec == 'necromancer':
                        print('(C)urse of a Dark Heart')
                    johnsblessing = input('Which Blessing do you choose?').strip().lower()
                    if johnsblessing == 'p':
                        print('John: Dono vobis benedictionem magnae virtutis')
                        time.sleep(sleep_short)
                        print('John: Goodluck kid *John smiles softly*')
                        print('+5 Power')
                        power += 5
                        takenjohnsblessing += 1
                        againinjohns = 'again '
                        Johnmildewshop()
                        choosingjohnsblessing = False
                    elif johnsblessing == 'h':
                        print('John: Dono vobis benedictionem magnae salutis')
                        time.sleep(sleep_short)
                        print('John: Stay safe kid *John smirks softly*')
                        print('+20 Health')
                        health += 20
                        takenjohnsblessing += 1
                        againinjohns = 'again '
                        Johnmildewshop()
                        choosingjohnsblessing = False
                    elif johnsblessing == 'e':
                        print('John: Dono vobis benedictionem magnae patientiae')
                        time.sleep(sleep_short)
                        print('John: you going to run a marathon? HOH HOH!')
                        print('+25 Stamina')
                        stamina += 25
                        takenjohnsblessing += 1
                        againinjohns = 'again '
                        Johnmildewshop()
                        choosingjohnsblessing = False
                    elif johnsblessing == 'i':
                        print('John: Dono vobis benedictionem magni intellectus')
                        time.sleep(sleep_short)
                        print('John: Smart ass... HOH HOH!')
                        print('+30 mana')
                        mana += 30
                        takenjohnsblessing += 1
                        againinjohns = 'again '
                        Johnmildewshop()
                        choosingjohnsblessing = False

                    elif johnsblessing == 'c' and spec == 'necromancer':
                        print('John: Erat captionem, cav......')
                        time.sleep(sleep_short)
                        print('Johns voice becomes too faint to hear.')
                        time.sleep(sleep_duration)
                        print('You sit quietly for a moment, pondering your decision')
                        time.sleep(sleep_long)
                        print('Did i choose right?')
                        time.sleep(sleep_short)
                        print('A rippling pain pierces your chest, you feel as though your heart will explode...')
                        time.sleep(sleep_duration)
                        print(f'{Darkgoddessname}: *her voice pierces your ears like a sharp screech* YOU HAVE CHOSEN WISELY MORTAL')
                        time.sleep(sleep_long)
                        print('Johns voice comes back')
                        time.sleep(sleep_short)
                        print('John: You alright kid?')
                        time.sleep(sleep_short)
                        print('You: Yes.... i feel good...')
                        time.sleep(sleep_short)
                        print('John: If you say so kid, *John smiles weakly, a slight tear in his eye*')
                        time.sleep(sleep_duration)
                        print('+1 summonslot')
                        print('-35 Health')
                        health -= 35
                        summonslots += 1
                        takenjohnsblessing += 1
                        againinjohns = 'again '
                        Johnmildewshop()
                        choosingjohnsblessing = False

                    else:
                        print('What blessing kid?')
            else:
                print('John: Im always here for you kid')
                Johnmildewshop()
        def johnsdadjokes():
            pickjoke = random.randint(1,5)
            if pickjoke == 1:
                print('John: What kind of underpants do lawyers wear?')
                time.sleep(sleep_short)
                print('John: BRIEFS!!! HOH HOH HOH!!')
                time.sleep(sleep_short)
                Johnmildewshop()
            if pickjoke == 2:
                print('John: What do you call it when a cow grows facial hair?')
                time.sleep(sleep_short)
                print('John: A MOOOOOO-STACHE! HOH HOH HOH!')
                time.sleep(sleep_short)
                Johnmildewshop()
            if pickjoke == 3:
                print('John: Did you hear about the two rowboats that got into an argument?')
                time.sleep(sleep_short)
                print('John: it was a real OAR DEAL! HOH HOH!')
                time.sleep(sleep_short)
                Johnmildewshop()
            if pickjoke == 4:
                print("John: There are only two things I don't eat for breakfast")
                time.sleep(sleep_short)
                print('John: Lunch and Dinner! HOH HOH HOH!')
                time.sleep(sleep_short)
                Johnmildewshop()
            if pickjoke == 5:
                print('John: I adopted a dog from a blacksmith')
                time.sleep(sleep_short)
                print('John: As soon as i brought him home he made a bolt for the door... HOH HOH HOH!')
                time.sleep(sleep_short)
                Johnmildewshop()
        def johnquest():
            answeredjohnquest = False
            if 'Slime Chunk Gathering' not in currentquests and 'Slime Chunk Gathering' not in completedquests:
                print('John: Matter of fact... Ive been needing some slime chunks for my furnace, ive heard it gives meat a unique taste')
                time.sleep(sleep_long)
                print('John: Would you mind gathering me 5 slime chunks? Ill pay you for it?')
                acceptjohnquest = input('\n(Y)es or (N)o').strip().lower()
                if acceptjohnquest == 'y':
                    addquest('Slime Chunk Gathering', 'John needs 5 [slime chunk]s for his furnace to cook some food', 'Mildew Village')
                    print('John: HOH! HOH! THANKS KID! YOURE A LIFE SAVER!')
                    time.sleep(sleep_duration)
                    Johnmildewshop()
                if acceptjohnquest == 'n':
                    print('John: Well alrighty then, ill get another young chap to do it, offer still stands though')
                    time.sleep(sleep_duration)
                    Johnmildewshop()
            if 'Slime Chunk Gathering' in currentquests and 'Slime Chunk Gathering' not in completedquests:
                print('John: Have you gotten the slime chunks?')
                while not answeredjohnquest:
                    slimequestyesorno = input('(Y) or (N) ').lower().strip()
                    if slimequestyesorno == 'y':
                        slime_chunk_info = inv.get('Slime Chunk', None)
                        if slime_chunk_info:
                            if slime_chunk_info['quantity'] >= 5:
                                print("John: HOH HOH HOH!, Thank you kid, these will do just fine!")
                                time.sleep(sleep_duration)
                                print("John: OH YEAH!!! heres yer payment!")
                                removeitem(inv, 'Slime Chunk', 5)
                                additem(inv, 'Gloves', 'Butchers Gloves', 1, 150, 5, 0, 25, 15, 0, 'yes', 'rare', 'Hands', 'no')
                                addgold(72)
                                time.sleep(sleep_duration)
                                print('John: Sorry thats all i have right now, thanks for the help kid.')
                                answeredjohnquest = True
                                Johnmildewshop()
                            else:
                                print('HOH HOH! I may be old but you dont have 5 slime chunks, come back when you have 5 kid')
                                time.sleep(sleep_long)
                                Johnmildewshop()
                                answeredjohnquest = True
                        else:
                            print('John: HOH HOH! you dont even have any slime chunks kid, happy hunting, be safe!')
                            time.sleep(sleep_duration)
                            answeredjohnquest = True
                            Johnmildewshop()
                    elif slimequestyesorno == 'n':
                        print('Come back when youre ready kid! HOH HOH! Dont hurt yourself!')
                        answeredjohnquest = True
                        time.sleep(sleep_duration)
                        Johnmildewshop()
                    else:
                        print('What was that kid?')
            else:
                if firsttimegetjohnmeat == 0:
                    print('John: Thanks for those slime chunks, The meat had a more slimy texture, i actually have some leftovers, here you are kid')
                    time.sleep(sleep_long)
                    additem(inv, 'Meat', 'Slimy Meat', 2, 10, 0, 25, 25, 45, 0, 'no', 'uncommon', 'none', 'yes', 'Slimy meat, kind of tastes like green jolly ranchers, wait.... whats that?')
                    Johnmildewshop()
                else:
                    print('John: Thanks for the help kid.')
        johngreeting = 0
        askquestionjohn = True
        checkcurrentstats()
        while askquestionjohn:
            global firsttimeinjohns
            if firsttimeinjohns == 0:
                print("You enter John's Butcher Shop, this man is like a second father to you, he would always keep you fed when you were hungry and saved your life on multiple occasions.")
                firsttimeinjohns += 1
                time.sleep(sleep_long)
            if johngreeting == 0:
                greetings = [
                    "John: HOH! HOH! HOH!",
                    "John: Hey there Kid!",
                    "John: How're you kid?"
                ]
                selected_greeting = random.choice(greetings)
                print(selected_greeting)
                johngreeting = 1
            time.sleep(sleep_duration)
            print("John: What cen I du you fer?")
            johnquestion = input("(W)anna talk?, (A)nything you need done?, (T)ell me a joke please, (S)hop, (G)oodbye").strip().lower()

            if johnquestion == 'w':
                print(f'{name}: Can we talk?')
                time.sleep(sleep_duration)
                talkingtojohn()
                askquestionjohn = False
            elif johnquestion == 'a':
                print(f"{name}: I've been looking to make some money, do you need anything done around here?")
                time.sleep(sleep_duration)
                johnquest()
                askquestionjohn = False
            elif johnquestion == 't':
                print(f'{name}: Can you tell me a joke?')
                time.sleep(sleep_short)
                johnsdadjokes()
                askquestionjohn = False
            elif johnquestion == 's':
                print(f'{name}: What do you have for sale?')
                time.sleep(sleep_short)
                johnsshop()
                askquestionjohn = False
            elif johnquestion == 'g':
                print(f'{name}: See you later John!')
                time.sleep(sleep_short)
                print("John: Yer always welcome, see ya kid")
                time.sleep(sleep_short)
                mildewvillagesquare()
                askquestionjohn = False
            else:
                print("What was that kid? My ears aren't the same as they used to be... HOH HOH!")
    def mildewsmallgarden(): #Later thought, maybe just make a randint and if its a certain value make it so they get an item with the additem function, instead of doing something so complicated
        green = colorcode('uncommon')
        red = colorcode('mythic')

        global GardenCooldown
        currenttime = time.time()
        interval = 15  # Interval in minutes between garden mini-games
        time_since_last_garden = (currenttime - GardenCooldown) / 60  # Time passed since last garden mini-game in minutes
        time_to_wait = (interval - time_since_last_garden) / 60  # Time remaining to wait in minutes

        # Check if enough time has passed since the last mini-game
        if time_since_last_garden >= interval:
            gardenminigamequestion = True
            time.sleep(sleep_duration)
            print(f'\nYou enter the garden, there seems to be 6 holes in the ground, do you reach in one?\n')
            time.sleep(sleep_duration)

            while gardenminigamequestion:
                Y_or_N_for_garden = input('(Y)es or (N)o?').strip().lower()
                if Y_or_N_for_garden == 'y':
                    doingminigame = True
                    print('You decide to stick your hand into a hole... Which one? (1-10)')
                    while doingminigame:
                        gardenminigame = input(f'\n1, 2, 3, 4, 5, 6, 7, 8, 9, 10\n').strip()
                        holewgoodloot = random.randint(1, 10)
                        holewithbadloot = random.randint(1, 10)
                        while holewithbadloot == holewgoodloot:
                            holewithbadloot = random.randint(1, 10)

                        print(f'Checking hole {gardenminigame}...')

                        if int(gardenminigame) == holewgoodloot:
                            print(f'You put your hand in hole {gardenminigame}...')
                            time.sleep(sleep_long)
                            print(f'{green}LUCKY!{Color.END}')
                            time.sleep(sleep_short)

                            itemfoundinluckyhole = random.randint(0, 1)
                            if itemfoundinluckyhole <= 0.4:
                                additem(inv, "mgcseed", 'Magic Seed', 1, 100, 0, 200, 0, 50, 0, 'no', 'rare', 'none', 'yes', 'A rare seed that will restore your mana by 200 and magically heal small wounds.')
                            elif itemfoundinluckyhole <= 0.8:
                                additem(inv, "Med Heal", "Medium Healing Potion", 1, 150, 0, 0, 0, 150, 0, 'no', "rare", 'none', 'yes', 'A healing potion crafted larger and stronger than its smaller versions')
                            else:
                                additem(inv, 'sm pouch', "Small Pouch of Gold", 1, 135, 0, 0, 0, 0, 0, 0, 'uncommon', 'none', 'no', 'A sealed small pouch with a small amount of gold, can be sold to a merchant, who will give you a large share of the gold found')
                            time.sleep(sleep_duration)

                            GardenCooldown = currenttime
                            doingminigame = False

                        elif int(gardenminigame) == holewithbadloot:
                            print(f'You put your hand in hole {gardenminigame}...')
                            time.sleep(sleep_long)
                            print(f'{red}UNLUCKY{Color.END}')
                            time.sleep(sleep_short)
                            itemfoundinunluckyhole = random.randint(0, 1)
                            if itemfoundinunluckyhole <= 0.2:
                                print('OW!....')
                                time.sleep(sleep_short)
                                damagefrombug = random.randint(1, 20)
                                print('You were bitten by a bug.')
                                time.sleep(sleep_short)
                                losehealth(damagefrombug)
                                time.sleep(sleep_duration)
                                mildewvillagesquare()
                                GardenCooldown = currenttime
                                doingminigame = False
                            else:
                                additem(inv, "garbage", 'Garbage', 1, 0, 0, 0, 0, 0, 0, 'no', 'common', 'none', 'no', 'Literal garbage.')
                                time.sleep(sleep_duration)
                                mildewvillagesquare()
                                GardenCooldown = currenttime
                                doingminigame = False

                        elif not gardenminigame.isdigit():
                            print('Choose a number 1-10')

                        else:
                            print(f'You put your hand in hole {gardenminigame}...')
                            time.sleep(sleep_long)
                            print('OH!?!?')
                            time.sleep(sleep_duration)
                            print('Nothing........')
                            time.sleep(sleep_duration)
                            mildewvillagesquare()
                            GardenCooldown = currenttime
                            doingminigame = False

                elif Y_or_N_for_garden == 'n':
                    print(f'\nYou leave the garden without checking the holes.\n')
                    time.sleep(sleep_duration)
                    mildewvillagesquare()
                    gardenminigamequestion = False

                else:
                    print('(Y)es or (N)o?')
        else:
            print(f'You need to wait another {time_to_wait:.1f} minutes to do this again.')
            time.sleep(sleep_duration)
            mildewvillagesquare()





    def ednashome():
        def ednasdialogue():
            ednaquestion = False
            time.sleep(sleep_short)
            print('(H)eal, (D)o you need anything?, (Hug), (G)oodbye')
            while ednaquestion == False:
                choice = input('').lower().strip()
                if choice == 'h':
                    print(f'{name}: Could you patch me up?')
                    time.sleep(sleep_duration)
                    print(f'Edna: Of course {name}, why dont you go lie down...')
                    doctorheal()
                    time.sleep(sleep_duration)
                    ednasdialogue()
                    ednaquestion = True
                elif choice == 'd':
                    ednaquestanswer = False
                    global currentquests, completedquests, inv
                    if 'Gather Herbs for Edna' not in currentquests and 'Gather Herbs for Edna' not in completedquests:
                        print("Edna: I'm actually running low on simple herbs, there could be some in the forest... There are slimes there aswell, and it could be dangerous... If youre willing, could you get me 3 [Simple Herbs]?")
                        time.sleep(sleep_huge)
                        while ednaquestanswer == False:
                            ednaquest = input('(Y)es or (N)o').strip().lower()
                            if ednaquest == 'y':
                                print('Edna: Great! Ill pay you well!')
                                time.sleep(sleep_short)
                                addquest('Gather Herbs for Edna', 'Edna needs 3 [Simple Herbs] to make some ointment, they can be found in the Mildew Forest', 'Mildew')
                                time.sleep(sleep_short)
                                ednasdialogue()
                            if ednaquest == 'n':
                                print('Edna: well alright then! If you change your mind feel free to come back!')
                            else:
                                print('What was that young man? (Y)es or (N)o')
                    if 'Gather Herbs for Edna' not in completedquests and 'Gather Herbs for Edna' in currentquests:
                        print('Edna: Have you gotten those Herbs? (Y)es or (N)o')
                        gottenherbs = input('').lower().strip()
                        if gottenherbs == 'y':
                            herbinfo = inv.get('Simple Herb', None)
                            if herbinfo['Simple Herb'] >= 3:
                                removeitem(inv, 'Simple Herb', 3)
                                print('Edna: Great! Thank you so much!')
                                time.sleep(sleep_duration)
                                addgold(105)
                                additem(inv, 'Ednacookie', 'Ednas Chocolate Chip Cookie', 5, 0, 0, 20, 20, 20, 0, 'no', 'rare', 'none', 'yes', 'Baked with Love')
                                time.sleep(sleep_long)

                                finishedquest('Gather Herbs for Edna')

                                ednasdialogue()
                            else:
                                print('Edna: Thats not 3? Gather me 3 please, come back when youre done')
                                time.sleep(sleep_duration)
                                ednasdialogue()
                        if gottenherbs == 'n':
                            print("Edna: That's alright! Please bring me 3 [Simple Herb]s! Be safe!")
                            time.sleep(sleep_duration)
                    if 'Gather Herbs for Edna' in completedquests and ednagivingointment == 0:
                        print('Edna: Thanks for the help young man!')
                        time.sleep(sleep_duration)
                        print('Edna: I actually only needed two, so i have a little extra, take it and be safe!')
                        time.sleep(sleep_duration)
                        additem(inv, 'Edna Ointment', 'Ednas Homemade Ointment', 3, 20, 0, 0, 0, 65, 0, 'no', 'uncommon', 'none', 'yes', 'A homemade ointment for cuts and bruises made by Edna, She may not look it but she was an alchemist in her earlier years, very effective!')
                        time.sleep(sleep_duration)
                        ednagivingointment +=1
                        ednasdialogue()


                elif choice == 'hug':
                    print(f'{name}: Could i have a hug?')
                    time.sleep(sleep_duration)
                    print('Edna: Of course!')
                    time.sleep(sleep_duration)
                    print('You two hug, edna gives you some back pats..')
                    time.sleep(sleep_long)
                    ednasdialogue()
                    ednaquestion = True
                elif choice == 'g':
                    print(f'{name}: Goodbye Edna!')
                    time.sleep(sleep_short)
                    print('Edna: Stay safe out there!')
                    time.sleep(sleep_short)
                    mildewvillagesquare()
                    ednaquestion = True
                else:
                    print('Edna: What was that young man?')
        global firsttimeinednas, name
        ednagreeting = 0
        if firsttimeinednas == 0:
            print('This is Johns mother, shes sweet to everyone in the village and makes the BEST COOKIES!')
            print(f"Edna: oh hello there {name}, youve gotten so big!")
            time.sleep(sleep_duration)
            print('Edna: let me go grab you a cookie, theyre fresh out of the oven...')
            time.sleep(sleep_long)
            print('Edna: Here you are, enjoy it!')
            time.sleep(sleep_short)
            additem(inv, 'Ednacookie', 'Ednas Chocolate Chip Cookie', 1, 0, 0, 20, 20, 20, 0, 'no', 'rare', 'none', 'yes', 'Baked with Love')
            firsttimeinednas += 1
        if ednagreeting == 0:
            ednasgreetings = ['Edna: Hello young man!', 'Edna: How are you?', 'Edna: Hows John doing?', 'Edna: Have you gotten taller?']
            greeting = random.choice(ednasgreetings)
            print(greeting)
            time.sleep(sleep_duration)
            ednagreeting +=1
        print('Edna: Is there anything I can do for you?')
        ednasdialogue()
    def mildewforest():
        pass
    mildewgoto = True
    while mildewgoto:
        time.sleep(sleep_duration)
        print("(J)ohn's Butcher Shop, (S)mall garden, (O)ld Widow Edna's House, (F)orest, (P)layer Menu")
        wheregoinmildew = input("\nWhere do you go?").lower().strip()

        if wheregoinmildew == 'j':
            mildewgoto = False
            Johnmildewshop()
        elif wheregoinmildew == 's':
            mildewgoto = False
            mildewsmallgarden()
        elif wheregoinmildew == 'o':
            mildewgoto = False
            ednashome()
        elif wheregoinmildew == 'f':
            mildewgoto = False
            mildewforest()
        elif wheregoinmildew == 'p':
            mildewgoto = False
            mainplaymenu()
        else:
            print("Where?")

def mildewvillagetownstart():
    global spec
    color_code_red = colorcode('mythic')
    color_code_purple = colorcode('quest')
    if spec == 'necromancer':
        print(f"I could revive them, but it wouldnt fix it, they would just be {color_code_red}empty husks{Color.END} of themselves that follow my every order, it would be wrong")
        time.sleep(sleep_long)
    print(f'''You exit your previously happy family home, that is now {color_code_red}tainted with the blood of your dead family members{Color.END}.
           {color_code_purple}You lock the door and throw away the key{Color.END}, {color_code_red}never{Color.END} to {color_code_purple}return again.{Color.END}''')
    time.sleep(sleep_huge)
    print(f'You take a deep breath and take the first steps of your new life, a life of revenge, you look into the village square and see the faces of your young neighbors, {color_code_red}happy{Color.END}, you used to be like them.')
    time.sleep(sleep_long)
    print('You enter the village square, maybe you could earn some money before beginning your journey.')
    mildewvillagesquare()

def mainplaymenu():
    def inventory():
        def update_weapon_slots():
            global equipeditems

            # Scenario 1 & 2: If only WeaponLeft or WeaponRight has an item, make WeaponBoth full
            if (equipeditems['WeaponLeft'] and not equipeditems['WeaponRight']) or (equipeditems['WeaponRight'] and not equipeditems['WeaponLeft']):
                if not equipeditems['WeaponBoth']:
                    equipeditems['WeaponBoth'] = FORWEAPONS['FullBoth']

            # Scenario 3: If WeaponBoth is full, placehold both single slots
            if equipeditems['WeaponBoth'] and equipeditems['WeaponBoth'] != FORWEAPONS['FullBoth']:
                if not equipeditems['WeaponLeft']:
                    equipeditems['WeaponLeft'] = FORWEAPONS['FullLeft']
                if not equipeditems['WeaponRight']:
                    equipeditems['WeaponRight'] = FORWEAPONS['FullRight']

            # Scenario 4: If both WeaponLeft and WeaponRight are equipped, make WeaponBoth full
            if equipeditems['WeaponLeft'] and equipeditems['WeaponRight']:
                if not equipeditems['WeaponBoth']:
                    equipeditems['WeaponBoth'] = FORWEAPONS['FullBoth']

            # Scenario 5: If no weapons are equipped, there should be no placeholders
            if not equipeditems['WeaponLeft'] and not equipeditems['WeaponRight'] and not equipeditems['WeaponBoth']:
                equipeditems['WeaponLeft'] = None
                equipeditems['WeaponRight'] = None
                equipeditems['WeaponBoth'] = None

            # Scenario 6: If WeaponBoth doesn't have a weapon, then both single slots shouldn't have a placeholder
            if not equipeditems['WeaponBoth']:
                if equipeditems['WeaponLeft'] == FORWEAPONS['FullLeft']:
                    equipeditems['WeaponLeft'] = None
                if equipeditems['WeaponRight'] == FORWEAPONS['FullRight']:
                    equipeditems['WeaponRight'] = None

            # Scenario 7: If WeaponBoth is full and both single slots are empty, reset WeaponBoth to empty
            if equipeditems['WeaponBoth'] == FORWEAPONS['FullBoth']:
                if not equipeditems['WeaponLeft'] and not equipeditems['WeaponRight']:
                    equipeditems['WeaponBoth'] = None
            if (equipeditems['WeaponLeft'] == FORWEAPONS['FullLeft'] and
            equipeditems['WeaponRight'] == FORWEAPONS['FullRight'] and
            equipeditems['WeaponBoth'] == FORWEAPONS['FullBoth']):
                equipeditems['WeaponLeft'] = None
                equipeditems['WeaponRight'] = None
                equipeditems['WeaponBoth'] = None
        def equipitems():
            def updatestatsforequips():
                global health, stamina, mana, power, summonslots, spec, currentstamina, currenthealth, currentmana, opensummonslots
                health_increase = 0
                stamina_increase = 0
                mana_increase = 0
                power_increase = 0
                summonslots_increase = 0

                for slot, item in newequipeditems.items():
                    if isinstance(item, dict):  # Ensure item is a dictionary
                        health_increase += item.get('health', 0)
                        stamina_increase += item.get('stamina', 0)
                        mana_increase += item.get('mana', 0)
                        power_increase += item.get('power', 0)
                        summonslots_increase += item.get('summonslots', 0)

                health += health_increase
                stamina += stamina_increase
                mana += mana_increase
                power += power_increase
                currentstamina += stamina_increase
                currentmana += mana_increase
                currenthealth += health_increase

                if spec == "necromancer":
                    summonslots += summonslots_increase
                    opensummonslots += summonslots_increase
            global equipeditems, inv
            for item_id, details in inv.items():
                if details.get('equipable') == 'yes':
                    color_code = colorcode(details.get('rarity', 'common'))
                    print(f'\n{color_code}{details.get("name", "Unknown")}{Color.END}')
                    display_item_stats(details)
                    print(f'A {details.get("slot", "unknown")} Equipable')

            while True:
                whatwantequip = input("What is the name of the item you would like to Equip? Or type 'inventory' to go back: ").lower().strip()
                itemtoequip = next((item_id for item_id, details in inv.items() if details.get('name', '').lower() == whatwantequip), None)

                if itemtoequip:
                    item_details = inv.pop(itemtoequip)
                    if item_details.get('equipable') == 'yes':
                        slot = item_details.get('slot', 'none')
                        if slot == "ring":
                            if "ring" not in equipeditems:
                                equipeditems["ring"] = []

                            if len(equipeditems["ring"]) < 2:
                                equipeditems["ring"].append(item_details)
                                newequipeditems[itemtoequip] = item_details
                                print(f"Equipped {item_details['name']} in the {slot} slot.")
                            else:
                                print("You already have two rings equipped. Please unequip one first.")
                                inv[itemtoequip] = item_details
                        else:
                            if equipeditems.get(slot):
                                print(f"You already have an item equipped in the {slot} slot. Please unequip it first.")
                                inv[itemtoequip] = item_details
                            else:
                                equipeditems[slot] = item_details
                                newequipeditems[itemtoequip] = item_details
                                print(f"Equipped {item_details['name']} in the {slot} slot.")
                        update_weapon_slots()
                        updatestatsforequips()
                        checkcurrentstats()
                        newequipeditems.pop(itemtoequip)
                        inventory()
                        break
                    else:
                        print(f"The item {item_details['name']} is not equipable.")
                elif whatwantequip == 'inventory':
                    inventory()
                    break
                else:
                    print("Item not found in inventory.")
        def unequipitems():
            def removeequipstats():
                global health, stamina, mana, power, summonslots, spec
                health_decrease = 0
                stamina_decrease = 0
                mana_decrease = 0
                power_decrease = 0
                summonslots_decrease = 0

                for item_id, item in unequipeditems.items():
                    health_decrease += item.get('health', 0)
                    stamina_decrease += item.get('stamina', 0)
                    mana_decrease += item.get('mana', 0)
                    power_decrease += item.get('power', 0)
                    summonslots_decrease += item.get('summonslots', 0)

                health -= health_decrease
                stamina -= stamina_decrease
                mana -= mana_decrease
                power -= power_decrease

                if spec == "necromancer":
                    summonslots -= summonslots_decrease
            global equipeditems, inv, unequipeditems
            for slot, item in equipeditems.items():
                if slot == "ring":
                    if item:
                        for ring in item:
                            name = ring.get('name', 'Unknown')
                            health = ring.get('health', 0)
                            power = ring.get('power', 0)
                            mana = ring.get('mana', 0)
                            stamina = ring.get('stamina', 0)
                            summonslots = ring.get('summonslots', 0)
                            rarity = ring.get('rarity', 'common')
                            color_code = colorcode(rarity)

                            print(f'\n{color_code}{name}{Color.END}')

                            if health != 0:
                                print(f'{"+" if health > 0 else ""}{health} Health')
                            if power != 0:
                                print(f'{"+" if power > 0 else ""}{power} Power')
                            if mana != 0:
                                print(f'{"+" if mana > 0 else ""}{mana} Mana')
                            if stamina != 0:
                                print(f'{"+" if stamina > 0 else ""}{stamina} Stamina')
                            if summonslots != 0:
                                print(f'{"+" if summonslots > 0 else ""}{summonslots} Summon Slots')
                    else:
                        print("Ring: None equipped.")
                else:
                    if item:
                        name = item.get('name', 'Unknown')
                        health = item.get('health', 0)
                        power = item.get('power', 0)
                        mana = item.get('mana', 0)
                        stamina = item.get('stamina', 0)
                        summonslots = item.get('summonslots', 0)
                        rarity = item.get('rarity', 'common')
                        color_code = colorcode(rarity)

                        print(f'\n{slot.capitalize()}: {color_code}{name}{Color.END}')

                        if health != 0:
                            print(f'{"+" if health > 0 else ""}{health} Health')
                        if power != 0:
                            print(f'{"+" if power > 0 else ""}{power} Power')
                        if mana != 0:
                            print(f'{"+" if mana > 0 else ""}{mana} Mana')
                        if stamina != 0:
                            print(f'{"+" if stamina > 0 else ""}{stamina} Stamina')
                        if summonslots != 0:
                            print(f'{"+" if summonslots > 0 else ""}{summonslots} Summon Slots')
                    else:
                        print(f"{slot.capitalize()}: None equipped.")

            whatwantunequip = input("What is the name of the item you would like to Unequip? Or type 'inventory' to go back: ").lower().strip()
            itemtounequip = None

            for slot, item in equipeditems.items():
                if item is None:
                    continue  # Skip if the item is None
                if item.get('name', '').lower() == whatwantunequip:
                    if item.get('name', '') == 'Full':
                        print("You can't unequip that.")
                        break
                if slot == "ring":
                    if isinstance(item, list):  # Ensure item is a list before iterating
                        for ring in item:
                            if ring and ring.get('name', '').lower() == whatwantunequip:
                                itemtounequip = ring
                                item.remove(ring)
                                break
                else:
                    if item.get('name', '').lower() == whatwantunequip:
                        itemtounequip = item
                        equipeditems[slot] = None
                        break

            if itemtounequip:
                item_id = itemtounequip.get('name').lower().replace(' ', '_')
                inv[item_id] = itemtounequip
                unequipeditems[item_id] = itemtounequip
                print(f"Unequipped {itemtounequip['name']}.")
                removeequipstats()
                checkcurrentstats()
                unequipeditems.pop(item_id)
                print(unequipeditems)
            elif whatwantunequip == 'inventory':
                inventory()
            else:
                print("Item not found.")

            update_weapon_slots()
            inventory()
        def useitem():


            global currenthealth, currentstamina, currentmana

            for item_id, details in inv.items():
                if details.get('consumable') == 'yes':
                    color_code = colorcode(details.get('rarity', 'common'))
                    print(f'\n{color_code}{details.get("name", "Unknown")}{Color.END}')
                    display_item_stats(details)
                    print(f'A {details.get("slot", "unknown")} Equipable')

            whatwantuse = input('\nWhat would you like to use?').lower().strip()

            item_to_use = None
            for item_id, details in inv.items():
                if details.get('name', '').lower() == whatwantuse:
                    item_to_use = (item_id, details)
                    break

            if item_to_use:
                item_id, details = item_to_use
                if details.get('consumable') == 'yes':
                    healthtoadd = details.get('health', 0)
                    staminatoadd = details.get('stamina', 0)
                    manatoadd = details.get('mana', 0)

                    currenthealth += healthtoadd
                    currentstamina += staminatoadd
                    currentmana += manatoadd

                    removeitem(inv, item_id, 1)

                    checkcurrentstats()

                    if healthtoadd > 0:
                        print(f"+ {healthtoadd} health")
                    if manatoadd > 0:
                        print(f"+{manatoadd} mana")
                    if staminatoadd > 0:
                        print(f"+{staminatoadd} stamina")

                    time.sleep(sleep_short)
                    inventory()
                else:
                    print('That is not a consumable.')
            else:
                print("Invalid input, please type the item's name.")
        def trashitem():
            global inv
            print("\nInventory:")
            for item_id, details in inv.items():
                name = details['name']
                quantity = details['quantity']
                value = details['value']
                rarity = details['rarity']
                description = details['description']
                color_code = colorcode(rarity)  # Get the color code for the rarity
                whitecolor = colorcode('common')

                print(f"\nName: {color_code}{name}{Color.END}, Quantity: {quantity}, Value: {value}, Rarity: {rarity}, {whitecolor}Description: {description}{Color.END}")
            trashing = True
            time.sleep(sleep_duration)
            print('What would you like to trash? (B)ack?')
            while trashing:
                trash = input('(Any item)').lower().strip()
                item_to_trash = None
                for item_id, details in inv.items():
                    if details.get('name', '').lower() == trash:
                        item_to_trash = (item_id, details)
                        break

                if item_to_trash:
                    item_id, details = item_to_trash
                    name = details.get('name', None)
                    print(f'How many of {name} would you like to trash? (You have {details.get("quantity", 0)})')

                    amount = input('').strip()
                    if amount.isdigit():  # Correct validation check
                        amount = int(amount)
                        if amount >= details.get('quantity', 0):
                            time.sleep(sleep_short)
                            print('This will trash ALL of them, are you sure?')
                            suresure = False
                            while not suresure:
                                sure = input('(Y) or (N)?').lower().strip()
                                if sure == 'y':
                                    allofthem = details.get('quantity', 0)
                                    deleteitem(inv, item_id, allofthem)  # Fix: use item_id
                                    time.sleep(sleep_short)
                                    inventory()
                                    trashing = False
                                    suresure = True
                                elif sure == 'n':
                                    inventory()
                                    trashing = False
                                    suresure = True
                        else:
                            print(f'This will trash {amount} of {name}, are you sure?')
                            suresure = False
                            while not suresure:
                                sure = input('(Y) or (N)?').lower().strip()
                                if sure == 'y':
                                    deleteitem(inv, item_id, amount)  # Fix: use amount
                                    time.sleep(sleep_short)
                                    inventory()
                                    trashing = False
                                    suresure = True
                                elif sure == 'n':
                                    inventory()
                                    trashing = False
                                    suresure = True
                    else:
                        print('Please enter a number.')
                elif trash == 'b':
                    print('Returning')
                    time.sleep(sleep_duration)
                    inventory()
                    trashing = False
                else:
                    print('Item not found.')


        update_weapon_slots()
        global equipeditems, inv
        print("\nEquipped Items:")
        for slot, item in equipeditems.items():
            if slot == "ring":
                if item:
                    for ring in item:
                        rarity = ring['rarity']
                        color_code = colorcode(rarity)
                        print(f"Ring: {color_code}{ring['name']}{Color.END}, Rarity: {rarity}")
                else:
                    print(f"Ring: Empty")
            else:
                if item:
                    rarity = item['rarity']
                    color_code = colorcode(rarity)
                    print(f"{slot.capitalize()}: {color_code}{item['name']}{Color.END}, Rarity: {rarity}")
                else:
                    print(f"{slot.capitalize()}: Empty")
        print("\nInventory:")
        for item_id, details in inv.items():
            name = details['name']
            quantity = details['quantity']
            value = details['value']
            rarity = details['rarity']
            description = details['description']
            color_code = colorcode(rarity)  # Get the color code for the rarity
            whitecolor = colorcode('common')

            print(f"\nName: {color_code}{name}{Color.END}, Quantity: {quantity}, Value: {value}, Rarity: {rarity}, {whitecolor}Description: {description}{Color.END}")
        while True:
            invquestion = input("\nWould you like to 'Go (B)ack', '(E)quip Gear', '(U)nequip Gear', '(USE) Item', or '(T)rash item").lower().strip()

            if invquestion == "b":
                mainplaymenu()

            elif invquestion == "e":
                equipitems()

            elif invquestion == "u":
                unequipitems()

            elif invquestion == "use":
                useitem()

            elif invquestion == 't':
                trashitem()
            else:
                print("invalid input, 'Go Back', 'Equip', or 'Use'")
    def currenttown():
        global town, firsttimeinmildew
        if town == 'Mildew':
            if firsttimeinmildew > 0:
                mildewvillagesquare()
            if firsttimeinmildew == 0:
                firsttimeinmildew += 1
                mildewvillagetownstart()
        else:
            print('DEBUG IN CURRENTTOWN(), town is not a valid town, double check your variables')
    def stats():
        global health, stamina, mana, power, summonslots, spec
        print(f'''Spec: {spec.capitalize()}
    Power: {power}
    Health: {currenthealth}/{health}
    Mana: {currentmana}/{mana}
    Stamina: {currentstamina}/{stamina}''')
        if spec == "necromancer":
            print(f"Summon Slots: {opensummonslots}/{summonslots}")
        jsajsdajklsajkl = False
        while jsajsdajklsajkl == False:
            returnfromstats = input("\nType 'yes' if you have read your stats")
            if returnfromstats == 'yes':
                mainplaymenu()
                jsajsdajklsajkl = True
            if returnfromstats == 'adminadminadminnocheatingguys':
                mainplaymenu()
                jsajsdajklsajkl = True
            else:
                print("invalid input, type 'yes' if you would like to return")
    def quests():
        if len(currentquests) > 0:
            for questname, details in currentquests.items():
                description = details['Description']
                town = details['Location']
                print(f'\n{questname}: {description} in {town}')
        else:
            print('You have no quests currently')

        mainplaymenu()
    def gear():
        global health, stamina, mana, power, summonslots, spec
        printhealth = health
        printstam = stamina
        printmana = mana
        printpower = power
        printsummonslots = summonslots
        if equipeditems == {}:
            print("You have nothing equipped")
            mainplaymenu()
        print("Equipped Gear:")
        print(f'''Power: {printpower}
    Health: {currenthealth}/{printhealth}
    Mana: {currentmana}/{printmana}
    Stamina: {currentstamina}/{printstam}''')
        if spec == "necromancer":
            print(f"Summon Slots: {opensummonslots}/{printsummonslots}")
        for slot, details in equipeditems.items():
            if details:
                namee = details.get('name', 'Unknown')
                healthh = details.get('health', 0)
                powerr = details.get('power', 0)
                manaa = details.get('mana', 0)
                staminaa = details.get('stamina', 0)
                summonslotss = details.get('summonslots', 0)
                rarity = details.get('rarity', 'common')
                color_code = colorcode(rarity)

                print(f'{color_code}{namee}{Color.END}')
                if healthh > 0:
                    print(f'+{healthh} Health')
                elif healthh < 0:
                    print(f'-{healthh} Health')

                if powerr > 0:
                    print(f'+{powerr} Power')
                elif powerr < 0:
                    print(f'-{powerr} Power')

                if manaa > 0:
                    print(f'+{manaa} Mana')
                elif manaa < 0:
                    print(f'-{manaa} Mana')

                if staminaa > 0:
                    print(f'+{staminaa} Stamina')
                elif staminaa < 0:
                    print(f'-{staminaa} Stamina')

                if summonslotss > 0:
                    print(f'+{summonslotss} Summon Slots')
                elif summonslotss < 0:
                    print(f'-{summonslotss} Summon Slots')
        klaskldlsadklsakldsak = False
        while klaskldlsadklsakldsak == False:
            checkifseengear = input("Type 'Yes' if you have seen your gear").lower().strip()
            if checkifseengear == 'yes':
                mainplaymenu()
                klaskldlsadklsakldsak = True
            else:
                print("Type 'Yes' if you have seen your gear")

    main = ("(I)nventory", "(Q)uests", "(S)tats", "(L)ook around", "(G)ear")
    print(f'\n{main}')
    selectedinmenu = False
    while selectedinmenu is not True:
        navigateinv = input("where would you like to go?").strip().lower()
        if navigateinv == "i":
            inventory()
            selectedinmenu = True
        elif navigateinv == "q":
            quests()
            selectedinmenu = True
        elif navigateinv == "s":
            checkcurrentstats()
            stats()
            selectedinmenu = True
        elif navigateinv == "l":
            currenttown()
            selectedinmenu = True
        elif navigateinv == 'g':
            checkcurrentstats()
            gear()
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
    else:
        print("LOL YOU TYPED IT WRONG LOSER BAHAHHAHAHAA NOW U HAVE TO REDO EVERY INPUT TILL THIS POINT LLLLLLLLLLL")
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
    global GardenCooldown, ednagivingointment, currentstamina,againinjohns, FORWEAPONS, firsttimeinednas, Goddessname, Darkgoddessname, currentmana, opensummonslots, gold, name, currenthealth, health, stamina, mana, power, summonslots, spec, town, firsttimeinmildew, firsttimeinjohns, firsttimegetjohnmeat, inv, NecromancerSummons, takenjohnsblessing, completedquests, currentquests, unequipeditems, newequipeditems, equipeditems
    health = 100
    stamina = 100
    mana = 100
    power = 1
    gold = 100
    summonslots = 0
    currenthealth = 100
    currentstamina = 100
    currentmana = 100
    opensummonslots = 100
    GardenCooldown = 0
    spec = "none"
    name = ""
    town = "Mildew"
    againinjohns = ""
    firsttimeinmildew = 0
    firsttimeinjohns = 0
    firsttimegetjohnmeat = 0
    firsttimeinednas = 0
    ednagivingointment = 0
    Goddessname = 'Narukya'
    Darkgoddessname = 'Ire'
    takenjohnsblessing = 0
    completedquests = {}
    currentquests = {}
    unequipeditems = {}
    newequipeditems ={}
    equipeditems = {
        'Torso': {}, 'Legs': {}, 'Feet': {}, 'Arms': {}, 'Hands': {},
        'WeaponLeft': {}, 'WeaponRight': {}, 'WeaponBoth': {}, 'Head': {},
        'Wrist': {}, 'Earings': {}, 'Ring': {}, 'Necklace': {}
    }
    inv = {

        }  # PLAYER INVENTORY
    FORWEAPONS = {
        "FullLeft": {'name': 'Full', 'quantity': 1, 'value': 0, 'power': 0, 'mana': 0,
                'stamina': 0, 'health': 0, 'summonslots': 0, 'equipable': 'yes',
                'rarity': 'common', 'slot': 'WeaponLeft'},
        "FullRight": {'name': 'Full', 'quantity': 1, 'value': 0, 'power': 0, 'mana': 0,
                'stamina': 0, 'health': 0, 'summonslots': 0, 'equipable': 'yes',
                'rarity': 'common', 'slot': 'WeaponRight'},
        "FullBoth": {'name': 'Full', 'quantity': 1, 'value': 0, 'power': 0, 'mana': 0,
                'stamina': 0, 'health': 0, 'summonslots': 0, 'equipable': 'yes',
                'rarity': 'common', 'slot': 'WeaponBoth'},
        }
    NecromancerSummons = {}
    nameis()
    purpose()
    checkclass()
    starttown()
    mildewvillage()
def startagain():
    startofgame()

def isplayeralive():
    global currenthealth, name
    if currenthealth < 1:
        theyalreadydied = True
        while theyalreadydied:
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
        family = input("Do you remember your family, " + name + "? ").strip().lower()
        if family == "yes":
            print("This may be hard to hear...")
            time.sleep(sleep_short)
            fam = True
        elif family == "no":
            time.sleep(sleep_short)
            print("This may be a little easier to bear then, " + name + ".")
            time.sleep(sleep_duration)
            fam = True
        else:
            print("Invalid answer. Please type 'yes' or 'no'.")

def mainclass(): # Choosing main class for the entire game
    global choice, health, stamina, mana, power, summonslots, spec, currenthealth, opensummonslots, currentstamina, currentmana
    choice = False
    while not choice:
        time.sleep(sleep_short)
        spec = input("I'm so sorry friend... Your family was slaughtered just last night, A shady wisard was seen around the village last night, it was him... On your quest for revenge which path do you choose to follow? (warlock, brawler, swordsman, necromancer) ").strip().lower()
        if spec == "warlock":
            power = 5
            stamina = 60
            mana = 200
            health = 115
            summonslots = 0
            currenthealth = health
            currentstamina = stamina
            currentmana = mana
            choice = True
        elif spec == "brawler":
            power = 20
            stamina = 125
            mana = 40
            health = 175
            summonslots = 0
            currenthealth = health
            currentstamina = stamina
            currentmana = mana
            choice = True
        elif spec == "swordsman":
            power = 10
            stamina = 145
            mana = 30
            health = 150
            summonslots = 0
            currenthealth = health
            currentstamina = stamina
            currentmana = mana
            choice = True
        elif spec == "necromancer":
            power = 1
            stamina = 75
            mana = 250
            health = 105
            summonslots = 1
            opensummonslots = summonslots
            currentstamina = stamina
            currentmana = mana
            currenthealth = health
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
        print("This is the start of your journey, are you sure you want that class forever?")#inv, item_id, name, quantity, value, power, mana, stamina, health, summonslots, equiped, equipable, rarity
        finalizeclass = input("Yes or No ").strip().lower()
        if finalizeclass == "yes":
            if spec == "necromancer":
                additem(inv, "MSOTU", "Minor Staff of the Undead", 1, 100, 5, 15, 5, 0, 0,'yes', 'uncommon', 'WeaponLeft', 'no', 'A staff a random passerby gave you when you were a child, you kept it hidden and learned how to conjure the dead, not too shabby.')
                additem(inv, "DADS ROBE", "Shoddy Black Robe", 1, 15, 0, 50, 5, 50, 0,'yes', 'common', 'Torso', 'no', 'An old robe you found in your fathers closet.')
                additem(inv, "TON", "Common Tome of Necromancy", 1, 0, 0, 10, 0, 0, 1,'yes', 'common', 'WeaponRight', 'no', 'A tome of your findings on the undead')
                addlessermanapotion(4)
                addlesserhealingpotion(3)
                addgold(50)
                starttt = True
            elif spec == "brawler":
                additem(inv, "CSC", "Cracked Stone Cestus", 1, 12, 25, 0, -12, 15, 0,'yes', 'common', 'WeaponBoth', 'no', 'Two old rocks you hand carved yourself, you dropped it and it cracked though.')
                additem(inv, "Start Fighters Wraps", "Fighters Wraps", 1, 15, 10, 0, 25, 10, 0,'yes', 'uncommon', 'Arms', 'no', 'Leather strips, your father taught you how to reinforce your wrists using them, not a common technique.')
                additem(inv, "Fathers Armor", "Leather Patchwork Armor", 1, 100, 0, 0, 10, 100, 0,'yes', 'common', 'Torso', 'no', 'Old armor your father had in his closet')
                addlesserhealingpotion(6)
                addgold(50)
                starttt = True
            elif spec == "warlock":
                additem(inv, "SON", "Staff of Nature", 1, 100, 9, 100, 20, 0, 0, 'yes', 'uncommon', 'WeaponBoth', 'no', 'A weapon ethically harvested from the branch of an ElderWood Tree.')
                additem(inv, 'ROBE', 'Leaf Robe', 1, 15, 0, 72, 20, 35, 0, 'yes', 'common', 'Torso', 'no', 'A Robe born from leaves and twigs, holds weak magical properties.')
                addlesserhealingpotion(3)
                addlessermanapotion(3)
                addgold(50)
                starttt = True
            elif spec == 'swordsman':
                additem(inv, 'IS', 'Iron Sword', 1, 50, 32, 0, -10, 10, 0, 'yes', 'common', 'WeaponRight', 'yes', 'A sword forged iron, your average adventurer gear')
                additem(inv, 'CM', 'ChainMail', 1, 62, 0, 0, -5, 85, 0, 'yes', 'uncommon', 'Torso', 'no', 'Chains linked together to form a protective layer, useful against slashing attacks.')
                additem(inv, 'PL', 'Padded Leggings', 1, 15, 0, 0, 15, 50, 0, 'yes', 'common', 'Legs', 'no', 'Pants with iron plates inserted for extra protection.')
                additem(inv, 'IG', 'Iron Gloves', 1, 15, 2, 0, -5, 15, 0, 'yes', 'common', 'Hands', 'no', 'Gloves with iron protection, good for paper cuts...')
                addlesserhealingpotion(3)
                addgold(50)
                starttt = True
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
def mildewvillage():#DONT THINK THIS DOES ANYTHING CURRENTLY
    mainplaymenu()
    global location
    global playerlocation
    location = mildewvillage
    playerlocation = mildewvillage

# Start the game
startofgame()
