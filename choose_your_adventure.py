name = input("Type your name: ")
print("Welcome", name, "to this adventure! ")

answer = input("\nYou are on a dirt road, it has come to an end and you can go left or right. \nwhich way would you like to go? ").lower()

if answer == "left":
    answer = input("\nYou reached a river. You can walk around it or swim across the river. \nType walk to walk around or swim to swim across the river: ").lower()

    if answer == 'swim':
        print("\nYou swam across the river and were eaten by crocodiles.\nYou lost the game.")
    elif answer == 'walk':
        print("\nYou walked for many miles, and ran out of water.\nYou lost the game.")
    else:
        print("\nNot a valid option. You lose.")

elif answer == "right":
    answer = input("\nYou come to a bridge. It looks wobbly.\nDo you want to cross or head back? (cross / back): ").lower()

    if answer == 'cross':
        answer = input("\nYou cross the bridge and meet a stranger.\nDo you want to talk to them? (yes/no): ").lower()
        if answer == 'yes':
            print("\nYou talked to the stranger. You escaped to the city.\nYou won !!!")
        elif answer == 'no':
            print("\nYou ignored the stranger and got lost in the forest. \nYou lose.")
        else:
            print("\nNot a valid option. You lose.")
    elif answer == 'back':
        print("\nYou go back and lose.")
    else:
        print("\nNot a valid option. You lose.")
else:
    print("\nNot a valid option. You lose.")

print("\nThank you for trying,",name)