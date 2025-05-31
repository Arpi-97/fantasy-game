#Basic fantasy minigame adventure

#Random module used for random number generator. OS to use system commands if needed
import random
import os

#Character creation
choice = 0
#While loop. This is used of the player wants to recreate his character
while choice != 1:
    character_name = input("What's the name of your character?: ").capitalize()
    
    #Validation for class name
    valid_class = False;
    while valid_class != True:
        print("What class is you character? Choose between this values: ")
        print("Barbarian, Bard, Cleric, Druid, Warlock, Wizard")
        character_class = input("Make your choice: ").capitalize()
        if character_class in ["Barbarian", "Bard", "Cleric", "Druid", "Warlock", "Wizard"]:
            valid_class = True
        else:
            print("Invalid class name")
            input("Press a button to reinsert the class...")
            continue #Continue to repeat the loop because the class name is invalid
    
    #Character name and classes are capitalized
    #Input validation by checking if the class name is valid. Also gives the class a starting gear and starting stats
    #Barbarian class
    if character_class == "Barbarian":
        character_class = "Barbarian"
        weapon = "big axe"
        damage = random.randint(1, 10)
        armor = "leather armor"
        health = 20
        strength = 17
        dexterity = 10
        constitution = 15
        intelligence = 8
        wisdom = 10
        charisma = 8
        boots = "leather boots"
        accessory = "health potion"
    #bard class
    elif character_class == "Bard":
        character_class = "Bard"
        weapon = "knife"
        damage = random.randint(1, 4)
        armor = "colored robes"
        health = 12
        strength = 8
        dexterity = 12
        constitution = 10
        intelligence = 16
        wisdom = 14
        charisma = 18
        boots = "colored shoes"
        valid_instrument = False
        # Instrument validation input
        while valid_instrument != True:
            print("What instrument do you want to play? Choose between these: ")
            print("violin, flute, guitar")
            accessory = input("Make your choice: ").capitalize()
            if not accessory in ["Violin", "Flute", "Guitar"]:
                print("Invalid instrument. Please choose between violin, flute and guitar.")
                input("Press a button to reinsert the instrument...")
                continue
            else:
                valid_instrument = True
        if accessory == "violin":
            accessory = "violin"
        elif accessory == "flute":
            accessory = "flute"
        elif accessory == "lute":
            accessory = "lute"
        else:
            print("Invalid instrument")
    #Cleric class
    elif character_class == "Cleric":
        character_class = "Cleric"
        weapon = "mace"
        damage = random.randint(1, 7)
        armor = "chain mail"
        health = 14
        strength = 12
        dexterity = 8
        constitution = 10
        intelligence = 14
        wisdom = 18
        charisma = 8
        boots = "heavy boots"
        accessory = "scroll of healing"
    #Druid class
    elif character_class == "Druid":
        character_class = "Druid"
        weapon = "wood stick"
        damage = random.randint(1, 5)
        armor = "leaf cloak"
        health = 13
        strength = 10
        dexterity = 12
        constitution = 8
        intelligence = 16
        wisdom = 20
        charisma = 8
        boots = "sandals"
        accessory = "tome of nature"
    #Warlock class
    elif character_class == "Warlock":
        character_class = "Warlock"
        weapon = "light saber"
        damage = random.randint(1, 8)
        armor = "dark robes"
        health = 13
        strength = 11
        dexterity = 14
        constitution = 8
        intelligence = 9
        wisdom = 16
        charisma = 13
        boots = "dark boots"
        accessory = "dark wand"
    #Wizard class
    elif character_class == "Wizard":
        character_class = "Wizard"
        weapon = "staff"
        damage = random.randint(1, 6)
        armor = "wizard robes"
        health = 10
        strength = 8
        dexterity = 8
        constitution = 10
        intelligence = 20
        wisdom = 15
        charisma = 12
        boots = "wizard shoes"
        accessory = "spell book"
    else:
        print("Invalid class name")
        
    #Character layout and stats
    os.system('clear')  # Clear the console for better readability. The function is used on the other lines too
    print("You character is:")
    print(f'Name: {character_name}')
    print(f'Class: {character_class}')
    print("The character has the following equipment:")
    print(f'Weapon: {weapon}\nYour weapon does {damage}\nArmor: {armor}\nBoots: {boots}\nAccessory: {accessory}')
    print("The character has the following stats:")
    print(f"Health: {health}\nStrength: {strength}\nDexterity: {dexterity}\nConstitution: {constitution}\nIntelligence: {intelligence}\nWisdom: {wisdom}\nCharisma: {charisma}")
    
    #Ask the player if the character is valid. If not, return to the creation
    choice = int(input("Is this character valid? 1 for yes, 0 for no: "))
    if choice == 0:
        print("Character creation cancelled")
        input("Press a button to continue...")
        os.system('clear')
        
#Game start
print(f"{character_name}, your adventure begins now!")
input("Press a button to continue...")
os.system('clear')
print("Welcome to the fantasy minigame adventure!")
print("Where do you want to go? Choose between these options:")
print("1. The Cold Dungeon")
#print("2. The Dark Forest") Future feature
#print("3. The Capital City") Future feature
choice = int(input("Make your choice: "))
# Input validation for the choice of adventure
while choice > 3:
    print("Invalid choice. Please choose between 1, 2 and 3.")
    choice = int(input("Make your choice: "))
os.system('clear')  

#Choices
if choice == 1:
    validChoice = False
    print("You have chosen The Cold Dungeon. Prepare for a chilling adventure!")
    print("This dungeon is known for its intricate complex and its dark and narrow lairs. Be careful, as many monsters lurk in the shadows.")
    print("You enter the dungeon and find yourself in a dark corridor. The air is dry and cold ant the light is dim.")
    print("You can hear the sound of water dripping from the ceiling and the sound of your own footsteps echoing in the distance.")
    print("As you walk through the corridor, you see a light at the end of the tunnel. You walk towards it and find yourself in a large room.")
    input("Press a button to continue...")
    os.system('clear')
    print("You see a chest in the middle of the room, and the two other ways to go, one to the left and the other to the right.")
    print("What do you want to do?")
    print("1. Open the chest")
    print("2. Go left")
    #print("3. Go right") TO DO
    choiceRoom = int(input("Make your choice: "))
    while validChoice != True:
        if choiceRoom == 1:
            print("You open the chest and find a treasure! You gain 50 gold coins and a magical sword!")
            validChoice = True # Terminate the loop if the chest is opened
        elif choiceRoom == 2:
            wraithHealth = 12
            wraithAttack = random.randint(1, 6)
            print("You go left and find a wraith! It attacks you!")
            print("You attack first.")
            input("Press a button to continue...")
            while wraithHealth > 0 or health > 0:
                attack = random.randint(1, damage)
                print(f"You attack the wraith and deal {attack} damage.")
                wraithHealth = wraithHealth - attack
                print(f"The wraith has {wraithHealth} health left.")
                if wraithHealth <= 0:
                    print("You have defeated the wraith!")
                    print("You gain 20XP.")
                    validChoice = True # Terminate the loop if the wraith is defeated
                    break
                input("The fight continues. Press a button to continue...")
                
                #Wraith attacks
                print("The wraith attacks you with its ghostly sword!")
                attack = random.randint(1, wraithAttack)
                print(f"The wraith deals {attack} damage to you.")
                health = health - attack
                print(f"Your health is now {health}.")
                if health <= 0:
                    print("You have been defeated by the wraith! The darkness takes you.")
                    print("Game over.")
                    validChoice = True # Terminate the loop if the player is defeated
                    break
                input("The fight continues. Press a button to continue...")
        #elif choiceRoom == 3:
        else:
            print("Invalid choice. Please choose beetween 1, 2 and 3.")
            input("Press a button to continue...")
            continue