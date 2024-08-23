import random
import time

# Random sleep durations
sleep_short = random.uniform(1, 2)
sleep_duration = random.uniform(2, 4)
sleep_long = random.uniform(5, 7)

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
spec = "none"
name = ""
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
        print("Invalid input, please type the item's name.")




def quests():
    print("You currently have no quests")
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

def town():
    print("town")
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
            stats()
            selectedinmenu = True
        elif navigateinv == "l":
            town()
            selectedinmenu = True
        elif navigateinv == 'g':
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
                additem(inv, "BHstaff", "TestBoth", 1, 100, 5, 15, 5, 0, 0,'yes', 'uncommon', 'WeaponBoth', 'no')
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
