import random
import time

# Random sleep durations
sleep_short = random.uniform(1, 2)
sleep_duration = random.uniform(2, 4)
sleep_long = random.uniform(5, 7)
sleep_huge = random.uniform(7, 12)

class Color:
    RED = '\033[91m'   # red
    GREEN = '\033[92m' # green
    YELLOW = '\033[93m'# yellow
    BLUE = '\033[94m'  # blue
    MAGENTA = '\033[95m'# purple
    WHITE = '\033[97m' # white
    END = '\033[0m'

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

def additem(inv, item_id, name, quantity, value, power, mana, stamina, health, summonslots, equipable, rarity, slot, consumable):
    color_code = colorcode(rarity)
    if item_id in inv:
        inv[item_id]['quantity'] += quantity
        print(f"Added {quantity} more of {color_code}{name}{Color.END}.")
    else:
        inv[item_id] = {
            'name': name, 'quantity': quantity, 'value': value, 'power': power, 'mana': mana,
            'stamina': stamina, 'health': health, 'summonslots': summonslots, 'equipable': equipable,
            'rarity': rarity, 'slot': slot, 'consumable' : consumable
        }
        print(f"Picked up a new item: {color_code}{name}{Color.END}")

def removeitem(inv, item_id, quantity):
    if item_id in inv:
        if inv[item_id]['quantity'] >= quantity:
            rarity = inv[item_id]['rarity']
            color_code = colorcode(rarity)
            inv[item_id]['quantity'] -= quantity
            if inv[item_id]['quantity'] == 0:
                del inv[item_id]
            print(f"Used {quantity} of {color_code}{inv[item_id]['name']}{Color.END}.")
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
    

# Global variables
health = 0
stamina = 0
mana = 0
power = 0
summonslots = 0
currenthealth = 0
currentstamina = 0
currentmana = 0
opensummonslots = 0
firsttimeinmildew = 0
firsttimeinjohns = 0
spec = "none"
name = ""
town = ""
againinjohns = ""
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

def equipitems():
    global equipeditems, inv
    for item_id, details in inv.items():
        if details.get('equipable') == 'yes':
            color_code = colorcode(details.get('rarity', 'common'))
            print(f'{color_code}{details.get("name", "Unknown")}{Color.END}')
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

def unequipitems():
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

                    print(f'{color_code}{name}{Color.END}')

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

                print(f'{color_code}{name}{Color.END}')

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




def inventory():
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
        color_code = colorcode(rarity)  # Get the color code for the rarity
        
        print(f"Name: {color_code}{name}{Color.END}, Quantity: {quantity}, Value: {value}, Rarity: {rarity}")
    while True:
        invquestion = input("Would you like to 'Go (B)ack', '(E)quip Gear', '(U)nequip Gear', or '(USE) Item'").lower().strip()
        
        if invquestion == "b":
            mainplaymenu()
            
        elif invquestion == "e":
            equipitems()
            
        elif invquestion == "u":
            unequipitems()
            
        elif invquestion == "use":
            useitem()
        else:
            print("invalid input, 'Go Back', 'Equip', or 'Use'")
def useitem():
    global currenthealth, currentstamina, currentmana
    
    for item_id, details in inv.items():
        if details.get('consumable') == 'yes':
            color_code = colorcode(details.get('rarity', 'common'))
            print(f'{color_code}{details.get("name", "Unknown")}{Color.END}')
            display_item_stats(details)
            print(f'A {details.get("slot", "unknown")} Equipable')
    
    whatwantuse = input('What would you like to use?').lower().strip()
    
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




def quests():
    if len(currentquests) > 0:
        for questname, details in currentquests.items():
            description = details['Description']
            town = details['Location']
            print(f'{questname}: {description} in {town}')
    else:
        print('You have no quests currently')

    mainplaymenu()
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
        returnfromstats = input("Type 'yes' if you have read your stats")
        if returnfromstats == 'yes':
            mainplaymenu()
            jsajsdajklsajkl = True
        if returnfromstats == 'adminadminadminnocheatingguys':
            mainplaymenu()
            jsajsdajklsajkl = True
        else:
            print("invalid input, type 'yes' if you would like to return")
def currenttown():
    global town, firsttimeinmildew
    if town == 'Mildew':
        if firsttimeinmildew > 0:
            mildewvillagesquare()
        if firsttimeinmildew == 0:
            firsttimeinmildew += 1
            mildewvillagetownstart()

def mildewvillagesquare():
    mildewgoto = True
    while mildewgoto:
        time.sleep(sleep_duration)
        print("(J)ohn's Butcher Shop, (A)lley, (S)mall garden, (O)ld Widow Edna's House, (F)orest, (P)layer Menu")
        wheregoinmildew = input("Where do you go?").lower().strip()
        
        if wheregoinmildew == 'j':
            mildewgoto = False
            Johnmildewshop()
        elif wheregoinmildew == 'a':
            mildewgoto = False
            mildewalley()
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
def johnsdadjokes():
    pickjoke = random.randint(1,5)
    if pickjoke == 1:
        print('What kind of underpants do lawyers wear?')
        time.sleep(sleep_short)
        print('BRIEFS!!! HOH HOH HOH!!')
        time.sleep(sleep_short)
        Johnmildewshop()
    if pickjoke == 2:
        print('What do you call it when a cow grows facial hair?')
        time.sleep(sleep_short)
        print('A MOOOOOO-STACHE! HOH HOH HOH!')
        time.sleep(sleep_short)
        Johnmildewshop()
    if pickjoke == 3:
        print('Did you hear about the two rowboats that got into an argument?')
        time.sleep(sleep_short)
        print('it was a real OAR DEAL! HOH HOH!')
        time.sleep(sleep_short)
        Johnmildewshop()
    if pickjoke == 4:
        print("There are only two things I don't eat for breakfast")
        time.sleep(sleep_short)
        print('Lunch and Dinner! HOH HOH HOH!')
        time.sleep(sleep_short)
        Johnmildewshop()
    if pickjoke == 5:
        print('I adopted a dog from a blacksmith')
        time.sleep(sleep_short)
        print('As soon as i brought him home he made a bolt for the door... HOH HOH HOH!')
        time.sleep(sleep_short)
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
            print('John: The Blessing of Power, The Blessing of Health, The Blessing of Endurance, The Blessing of Intelect')
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
            print('Blessing of (P)ower, Blessing of (H)ealth, Blessing of (E)ndurance, Blessing of (I)ntelect')
            if spec == 'necromancer':
                print('(C)urse of a Black Heart')
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
                print('John: Smart ass.. HOH HOH!')
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
def johnquest():
    if 'Slime Hunting' not in currentquests and 'Slime Hunting' not in completedquests:
        print('John: Matter of fact... Ive been needing some slime chunks for my furnace to cook the meat properly')
        time.sleep(sleep_duration)
        print('John: Would you mind gathering me 5 slime chunks? Ill pay you for it.')
        acceptjohnquest = input('(Y)es or (N)o').strip().lower()
        if acceptjohnquest == 'y':
            addquest('Slime Hunting', 'John needs 5 slime chunks for his furnace', 'Mildew Village')
            print('John: HOH! HOH! THANKS KID! YOURE A LIFE SAVER!')
            time.sleep(sleep_duration)
            Johnmildewshop()
        if acceptjohnquest == 'n':
            print('John: Well alrighty then, ill get another young chap to do it, offer still stands though')
            time.sleep(sleep_duration)
            Johnmildewshop()
    elif 'Slime Hunting' in currentquests and 'Slime Hunting' not in completedquests:
        pass
    else:
        print('John: Thanks for those slime chunks, I dont have anything else I need right now')



def Johnmildewshop():
    askquestionjohn = True
    checkcurrentstats()
    while askquestionjohn:
        global firsttimeinjohns
        if firsttimeinjohns == 0:
            print("You enter John's Butcher Shop, this man is like a second father to you, he would always keep you fed when you were hungry and saved your life on multiple occasions.")
            firsttimeinjohns += 1
            time.sleep(sleep_long)
        
        print("John: HOH! HOH! HOH!")
        time.sleep(sleep_duration)
        print("John: What cen I du you fer kid?")
        johnquestion = input("(W)anna talk?, (A)nything you need done?, (T)ell me a joke please, (G)oodbye").strip().lower()
        
        if johnquestion == 'w':
            talkingtojohn()
            askquestionjohn = False
        elif johnquestion == 'a':
            johnquest()
            askquestionjohn = False
        elif johnquestion == 't':
            johnsdadjokes()
            askquestionjohn = False
        elif johnquestion == 'g':
            print("Yer always welcome, see ya kid")
            currenttown()
            askquestionjohn = False
        else:
            print("What was that kid? My ears aren't the same as they used to be... HOH HOH!")
def mildewalley():
    pass
def mildewsmallgarden():
    pass
def ednashome():
    pass
def mildewforest():
    pass

def mildewvillagetownstart():
    global spec
    color_code_red = colorcode('mythic')
    color_code_purple = colorcode('quest')
    if spec == 'necromancer':
        print(f"I could revive them, but it wouldnt fix it, they would just be {color_code_red}empty husks{Color.END} of themselves that follow my every order, it would be wrong")
        time.sleep(sleep_long)
    print(f'''You exit your previously happy family home, that is now {color_code_red}tainted with the blood of your dead family members{Color.END}.
           {color_code_purple}You lock the door and throw away the key{Color.END}, {color_code_red}never{Color.END} to return again.''')
    time.sleep(sleep_huge)
    print(f'You take a deep breath and take the first steps of your new life, a life of revenge, you look into the village square and see the faces of your young neighbors, {color_code_red}happy{Color.END}, you used to be like them.')
    time.sleep(sleep_long)
    print('You enter the village square, maybe you could earn some money before beginning your journey.')
    mildewvillagesquare()
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
            
def mainplaymenu():
    main = ("(I)nventory", "(Q)uests", "(S)tats", "(L)ook around", "(G)ear")
    print(main)
    selectedinmenu = False
    while selectedinmenu is not True:
        navigateinv = input("where would you like to go?").strip().lower()
        if navigateinv == "i":
            inventory()
            update_weapon_slots()
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
    global health, stamina, mana, power, summonslots, spec, town, firsttimeinmildew
    health = 100
    stamina = 100
    mana = 100
    power = 0
    summonslots = 0
    town = 'Mildew'
    firsttimeinmildew = 0
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
    global choice, health, stamina, mana, power, summonslots, spec, currenthealth, opensummonslots, currentstamina, currentmana
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
        print("This is the start of your journey, are you sure you want that class for the rest of it?")#inv, item_id, name, quantity, value, power, mana, stamina, health, summonslots, equiped, equipable, rarity
        finalizeclass = input("Yes or No ").strip().lower()
        if finalizeclass == "yes":
            if spec == "necromancer":
                additem(inv, "SHstaff", "Minor Staff of the Undead", 1, 100, 5, 15, 5, 0, 0,'yes', 'uncommon', 'WeaponLeft', 'no')
                additem(inv, "robe", "Shoddy Black Robe", 1, 15, 0, 50, 5, 50, 0,'yes', 'common', 'Torso', 'no')
                additem(inv, "SHtome", "Common Tome of Necromancy", 1, 0, 0, 10, 0, 0, 1,'yes', 'common', 'WeaponRight', 'no')
                additem(inv, "LMPotion", "Lesser Mana Potion", 3, 25, 0, 50, 0, 0, 0,'no', 'uncommon', 'none', 'yes')
                additem(inv, "LHPotion", "Lesser Healing Potion", 2, 20, 0, 0, 0, 50, 0,'no', 'common', 'none', 'yes')
                starttt = True
            elif spec == "brawler":
                additem(inv, "BHweapon", "Cracked Stone Cestus", 1, 12, 25, 0, -12, 15, 0,'yes', 'common', 'WeaponBoth', 'no')
                additem(inv, "Arms", "Fighters Wraps", 1, 15, 10, 0, 25, 10, 0,'yes', 'uncommon', 'Arms', 'no')
                additem(inv, "Armor", "Leather Patchwork Armor", 1, 100, 0, 0, 10, 100, 0,'yes', 'common', 'Torso', 'no')
                additem(inv, "LHPotion", "Lesser Healing Potion", 5, 20, 0, 0, 0, 50, 0,'no', 'common', 'none', 'yes')
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
