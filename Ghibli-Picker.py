import os
import time
import random
import sys
import json


def clear(): os.system("clear")


def sleep(x): time.sleep(x)


MovieDict = {
    '0': "When Marnie Was There",
    '1': "The Tale of The Princess Kaguya",
    '2': "The Wind Rises",
    '3': "From Up on Poppy Hill",
    '4': "The Secret World of Arrietty",
    '5': "Ponyo",
    '6': "Tales from Earthsea",
    '7': "Howl's Moving Castle",
    '8': "The Cat Returns",
    '9': "Spirited Away",
    '10': "My Neighbors the Yamadas",
    '11': "Princess Mononoke",
    '12': "Whisper of the Heart",
    '13': "Pom Poko",
    '14': "Ocean Waves",
    '15': "Porco Rosso",
    '16': "Only Yesterday",
    '17': "Kiki's Delivery Service",
    '18': "Grave of the Fireflies",
    '19': "My Neighbor Totoro",
    '20': "Castle in the Sky",
    '21': "Nausicaä of the Valley of the Wind",
    '22': "The Boy and the Heron"
}


def mainmenu():
    while True:
        print("\tStudio Ghibli Picker by calciume\n-----------------------------------------------")
        sleep(.5)
        print("Option 1: Pick a movie for me!")
        sleep(.1)
        print("Option 2: Exclude a movie from being picked")
        sleep(.1)
        print("Option 3: Save")
        sleep(.1)
        print("Option 4: Load")
        sleep(.1)
        print("Option 5: Exit")
        sleep(.1)

        mainmenuinput = str(input("Input: "))

        match mainmenuinput:
            case '1':
                option1()
            case '2':
                option2()
            case '3':
                option3()
            case '4':
                option4()
            case '5':
                option5()
            case _:
                print("Invalid input, try again.")
                sleep(1)
                clear()


def option1():
    clear()
    choice = random.choice(list(MovieDict.values()))
    print("Drumroll...")
    sleep(.5)
    print(".")
    sleep(.5)
    print(".")
    sleep(.5)
    print(".")
    sleep(.5)
    print(f"And the winner is...{choice}!")
    sleep(1)
    input("Press enter to continue...")
    clear()
    mainmenu()


def option2():
    while True:
        clear()
        print("Exclude what movie?")
        sleep(.1)
        for count, i in enumerate(MovieDict.values()):
            print(count, i)
        try:
            option2input = str(input("Input: "))
            MovieDict.pop(option2input)
        except KeyError:
            print("Invalid movie number. Try again.")
            sleep(1)
            clear()
            option2()
        print("Excluded!")
        sleep(1)
        clear()
        mainmenu()


def option3():
    print("This will override your existing save file. \n Are you sure you want to proceed?")
    sleep(.5)
    while True:
        overrideinput = input("Y/N: ")
        if overrideinput == "Y" or "y":
            fileexists = os.path.exists("save.json")  # Check if save file exists
            if fileexists is False:
                makefile = open("save.json", "x")  # Make the save file
                makefile.close()
            with open("save.json", "w") as json_save:  # Open the file for saving
                json.dump(MovieDict, json_save)  # Dump the dictionary to a .json
                print("Saved!")
                sleep(1)
                break
        elif overrideinput == "N" or "n":
            break
        else:
            print("Answer Y for yes or N for no")
            sleep(1)
    clear()
    mainmenu()


def option4():
    print("This will override any current exclusions. \nAre you sure you want to proceed?")
    sleep(.5)
    while True:
        overrideinput = input("Y/N: ")
        if overrideinput == "Y" or "y":
            try:  # Check if a save file exists
                with open("save.json") as json_load:  # Open the save file for loading
                    global MovieDict
                    MovieDict = json.load(json_load)  # Load the .json into the dictionary
                    print("Loaded save file!")
                    sleep(1)
                    break
            except FileNotFoundError:
                print("No save file found! Try saving first.")
                sleep(2)
                clear()
                mainmenu()

        elif overrideinput == "N" or "n":
            break
        else:
            (print("Answer Y for yes or N for no"))
            sleep(1)
    clear()
    mainmenu()


def option5():
    clear()
    sys.exit()


mainmenu()
