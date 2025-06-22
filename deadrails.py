import random

plr = "____________"
plrm = " held item "
plrt = "------------"
mainhand = ""

print("1.Tank- -2 damage from attackers +25 start hp")
print("2. +1 damage from enemies but each fight that ends you get 1 random item")
plrclass = input("pick a class using numbers")

visiblebuild = "Nothing"

slot1 = "none"
slot2 = "none"
slot3 = "none"
slot4 = "none"
slot5 = "none"
slot6 = "none"
hp = 100
if plrclass == "1":
	hp += 25
enemy = "none"

wining = False

# important lists

items = [
    "Gasoline Can",
    "Pistol",
    "Rifle",
    "Loaded Magazine",
    "Unloaded Magazine",
    "Rifle Ammo",
    "Empty Rifle Casing",
    "Sand",
    "Stick",
    "Dynamite",
    "Health Pack",
    "none"
]
enemies = [
    "Zombie",
    "Outlaw",
    "Speedy Zombie",
    "none"
]
events = [
    "Flaming House",
    "Bank",
    "Train Station",
    "Thunder Storm",
    "Nothing"
]
amitems = 0
miles = 0
for i,v in enumerate(items):
    amitems += 1

slots = [slot1, slot2, slot3, slot4, slot5, slot6]


amevents = 0
for i,v in enumerate(events):
    amevents += 1
def event():
    global amevents
    global visiblebuild
    global events
    eventtopick = random.randint(0,amevents)
    visiblebuild = events[eventtopick - 1]
    return visiblebuild

def pin():
    global visiblebuild
    global mainhand
    print(plr)
    print(plrm, " ", mainhand)
    print(plrt)
    print(hp)

    for i, v in enumerate(slots):
        print("slot: ",i,slots[i])
    print("")
    print("equip item? if so select slot else say n")
    answer = input("item? ")
    if answer == "n":
        print("no item equiping")
    else:
        itemfound = False
        for i,v in enumerate(slots):
            if slots[i] == answer:
                itemfound = True
        if itemfound:
            mainhand = answer
    print("")
    print("|visible thing|")
    print(visiblebuild)
    print("")

    print("Drop an item?")
    answer2 = input("y/n")
    if answer2 == "y":
        droped = input("item?")
        for i, v in enumerate(slots):
            if slots[i] == droped:
                slots[i] = "none"
                break
    print("")
    event()


def give(item):
    for i,v in enumerate(slots):
        if v == "none":
            slots[i] = item
            print("")
            print("you got a ",item)
            print("")
            return item
def removeitem(item):
    global mainhand
    global slots
    for i, v in enumerate(slots):
        if v == item:
            if mainhand == item:
                mainhand = "none"
            slots[i] = "none"
            return
def harm(damagemsg,min,max):
    global hp
    losehp = random.randint(min, max)
    hp -= losehp
    if losehp > 0:
        print(damagemsg," ",losehp)
        print(hp)
def giverandom():
    global amitems
    global items
    randomitem = random.randint(0, amitems - 1)
    give(items[randomitem])
while True:
    #Main Loop
    visible = event()
    pin()
    if input("Would you like to loot visible buildings? y/n: ") == "y":
        print("")
        if visible == "Nothing":
            print("you can only see the sand ahead")
        if visible == "Flaming House":
            print("Ahead lies a flaming house maybe you can loot inside it")
            giverandom()
            harm("You Suffered Burns Looting",0,10)
        if visible == "Bank":
            print("You look for the combination to the vault code?")
            print("use held item instead?")
            if input("y/n") == "y" and mainhand == "Dynamite":
                removeitem("Dynamite")
            if random.randint(1,3) == 1:
                print("You found the code")
                giverandom()
        if visible == "Train Station":
            print("There are no trains, very odd for a train station despite the ruined world its just odd for there not to be any trains")
            if random.randint(1,2) == 1:
                giverandom()
        if visible == "Thunder Storm":
            print("You are caught in a thunder storm you may get struck by lightning while looting the area")
            if random.randint(1,8) == 1:
                harm("You have been struck by lightning",10,20)
            giverandom()
            print("")
        if random.randint(1,3) == 1:
            enemy = enemies[random.randint(0,len(enemies) - 1)]
        if wining:
            enemy = "Outlaw"
        if not enemy == "none":
            #Enemy Fighting
            print("You come accross a ",enemy)
            enemyhp = 100
            while enemyhp > 0:
                ran = False
                picked = input("1 = Attack,2 = Use Item, 3 = Equip item, 4 = Run")
                if picked == "1":
                    print("You attack the ",enemy)
                    if mainhand == "Dynamite":
                        removeitem("Dynamite")
                        enemyhp -= random.randint(10,20)
                    if mainhand == "Stick":
                        enemyhp -= random.randint(4,7)
                    if mainhand == "Pistol":
                        for i, v in enumerate(slots):
                            if slots[i] == "Loaded Magazine":
                                slots[i] = "Unloaded Magazine"
                                enemyhp -= random.randint(15, 30)
                                break
                    if mainhand == "Rifle":
                        for i, v in enumerate(slots):
                            if slots[i] == "Rifle Ammo":
                                slots[i] = "Empty Rifle Casing"
                                enemyhp -= random.randint(45, 65)
                                break
                    if mainhand == "Sand":
                        removeitem("Sand")
                        enemyhp -= random.randint(1, 2)
                if picked == "2":
                    item = "none"
                    for i, v in enumerate(slots):
                        print("slot: ", i, slots[i])
                    chosen = input("Chosen item: ")
                    for i, v in enumerate(slots):
                        print("Slot :",i," ",v)
                        if v == chosen:
                            item = v
                    if not item in ["Health Pack","Dynamite","Gasoline Can","Sand"]:
                        print("Non usable item")
                        print("Items usable are Dynamite, Gasoline Can, Sand, Health Pack")
                    else:
                        if item == "Dynamite":
                            print("You throw dynamite at the ",enemy)
                            enemyhp -= random.randint(10,20)
                            removeitem("Dynamite")
                        if item == "Sand":
                            removeitem("Sand")
                            enemyhp -= random.randint(1,2)
                        if item == "Gasoline Can":
                            totdmg = 0
                            removeitem("Gasoline Can")
                            burning = True
                            while burning:
                                totdmg += random.randint(4,5)
                                if random.randint(1,4) == 1:
                                    burning = False
                            print("Damage Dealt: ",totdmg)
                            enemyhp -= totdmg
                            print("enemy hp: ",enemyhp)
                        if item == "Health Pack":
                            hp += 15
                            removeitem("Health Pack")

                if picked == "3":
                    item = "none"
                    for i, v in enumerate(slots):
                        print("slot: ", i, slots[i])
                    chose = input("Chosen item: ")
                    for i,v in enumerate(slots):
                        if v == chose:
                            item = slots[i]
                    if not item == "none":
                        mainhand = item
                if picked == "4":
                    if random.randint(1,5) == 1:
                        print("You attempt to flee but failed you stubbed your toe and tripped so you lost your turn")
                    else:
                        print("you managed to run away the ",enemy," stubbed its toe and you ran safely")
                        enemyhp = 0
                if enemyhp > 0:
                    if enemy == "Zombie":
                        hp -= random.randint(6,10)
                        print("the zombie scratched you")
                    if enemy == "Outlaw":
                        hp -= random.randint(15,30)
                        print("the outlaw shot you")
                    if enemy == "Speedy Zombie":
                        hp -= random.randint(6,10)
                        if random.randint(1,2) == 1:
                            print("the zombie attacked a seccond time")
                            hp -= random.randint(5,9)
                        print("You have been scratched by the zombie")
                    print("hp: ",hp)
                    print("enemy hp: ",enemyhp)
                    if plrclass == "1":
                    	hp += 2
                    	print("you easily recovered from the attack")
                    	if plrclass == "2":
                    		hp -= 1
                    		print("you feel weaker and more vulnerable")
                if enemyhp <= 0:
                    if not ran:
                        if plrclass == "2":
                        	giverandom()
                        if wining:
                            print("You escaped the wastelands!")
                            break
                if hp <= 0:
                    break
    miles += 0.10
    if miles == 35:
        print("You traveled 35 miles")
        print("")
        wining = True
    print("Miles Traveled: ",miles)
    if hp <= 0:
        hp = 0
        print("yur like ded")
        break
input("")