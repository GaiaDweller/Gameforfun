stamina = 100
name = input("what is your name traveler? ")
print("hello " + name + " welcome to your journey, a warning for you, always type in lowercase.")
family = input("do you have a family " + name + "? ")
fam = False
while fam != True:
    if family == "yes":
        print("no longer my friend")
        fam = True
    elif family == "no":
        print("my condolences " + name)
        fam = True
    else:
        print("invalid answer, yes or no.")
        continue
choice = False
while choice != True:
    spec = input(" im sorry for your loss, but we need to move along, your family was killed by an evil wizard, what class will you choose to avenge your family? (warlock,brawler,swordsman,necromancer) ")
    if spec == "warlock":
        power = 5
        stamina = 60
        mana = 200
        health = 115
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
        power = 1
        stamina = 75
        mana = 250
        health = 105
        choice = True
    else:
        print("invalid input")
        continue
if choice == True: 
    print("you have chosen: " + spec)
    print("power is " + str(power))
    print("stamina is " + str(stamina))
    print("mana is " + str(mana))
    print("health is " + str(health))
