"""
Filename: Trapped.py
Author: Isshana
Date: 2018-06-08
Description: Text Based Adventure Game
"""
#---------------------------------------------constants

timeOne=1 #Constant

#-----------------------------------------import statements

import random
import time
import os
#---------------------------------------------ASCII functions
     
def oneOClock(): # Clock 1:00
    print(" _____________________________________")
    print("|   _______________________________   |")
    print("|  |  /  \     (  __   )(  __   )  |  |")
    print("|  |  \/) )  _ | (  )  || (  )  |  |  |")
    print("|  |    | | (_)| | /   || | /   |  |  |")
    print("|  |    | |    | (/ /) || (/ /) |  |  |")
    print("|  |    | |  _ |   / | ||   / | |  |  |")
    print("|  |  __) (_(_)|  (__) ||  (__) |  |  |")
    print("|  |  \____/   (_______)(_______)  |  |")
    print("|  |_______________________________|  |")
    print("|_____________________________________|")

     
def twoOClock(): #Clock 2:07
    print(" _____________________________________")
    print("|   _______________________________   |")
    print("|  | _______     _______  _        |  |")
    print("|  |/ ___   )   (  __   )/ ___  \  |  |")
    print("|  |\/   )  | _ | (  )  |\/   )  ) |  |")
    print("|  |    /   )(_)| | /   |    /  /  |  |")
    print("|  |  _/   /    | (/ /) |   /  /   |  |")
    print("|  | /   _/   _ |   / | |  /  /    |  |")
    print("|  |(   (__/\(_)|  (__) | /  /     |  |")
    print("|  |\_______/   (_______) \_/      |  |")
    print("|  |_______________________________|  |")
    print("|_____________________________________|")

def sun(): #sun ascii art
    print("""                   |
                            .   |
                                |
                  \    *        |     *    .  /
                    \        *  |  .        /
                 .    \     ___---___     /    .  
                        \.--         --./     
             ~-_    *  ./               \.   *   _-~
                ~-_   /                   \   _-~     *
           *       ~-/                     \-~        
             .      |                       |      .
                 * |                         | *     
        -----------|                         |-----------
          .        |                         |        .    
                *   |                       | *
                   _-\                     /-_    *
             .  _-~ . \                   /   ~-_     
             _-~       `\               /'*      ~-_  
            ~           /`--___   ___--'\           ~
                   *  /        ---     .  \   jgs
                    /     *     |           \
                  /             |   *         \
                             .  |        .
                                |
                                |""")

def soloShowdown(): #ASCII art Solo showdown
    print("""   \t \t /~~\ /~~\ |  /~~\   /~~\|  | /~~\ |  |  ||~~\  /~~\ |  |  ||\  |
    \t \t `--.|    || |    |  `--.|--||    ||  |  ||   ||    ||  |  || \ |
    \t \t \__/ \__/ |__\__/   \__/|  | \__/  \/ \/ |__/  \__/  \/ \/ |  \|""")

def mountain(): #mountain ascii art
    print("""                                  _
                            .-.      / \        _
                ^^         /   \    /^./\__   _/ \
              _        .--'\/\_ \__/.      \ /    \  ^^  ___
             / \_    _/ ^      \/  __  :'   /\/\  /\  __/   \
            /    \  /    .'   _/  /  \   ^ /    \/  \/ .`'\_/\'
           /\/\  /\/ :' __  ^/  ^/    `--./.'  ^  `-.\ _    _:\' _
          /    \/  \  _/  \-' __/.' ^ _   \_   .'\   _/ \ .  __/ \'
        /\  .-   `. \/     \ / -.   _/ \ -. `_/   \ /    `._/  ^  \
       /  `-.__ ^   / .-'.--'    . /    `--./ .-'  `-.  `-. `.  -  `.
     @/        `.  / /      `-.   /  .-'   / .   .'   \    \  \  .-  \%
     @(88%@)@%% @)&@&(88&@.-_=_-=_-=_-=_-=_.8@% &@&&8(8%@%8)(8@%8 8%@)%
     @88:::&(&8&&8::JGS:&`.~-_~~-~~_~-~_~-~~=.'@(&%::::%@8&8)::&#@8::::
     `::::::8%@@%:::::@%&8:`.=~~-.~~-.~~=..~'8::::::::&@8:::::&8::::::'
      `::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'""")

def loading(): #ascii art loading
    print("""   88                                 88 88                          
    88                                 88 ""                          
    88                                 88                             
    88  ,adPPYba,  ,adPPYYba,  ,adPPYb,88 88 8b,dPPYba,   ,adPPYb,d8  
    88 a8"     "8a ""     `Y8 a8"    `Y88 88 88P'   `"8a a8"    `Y88  
    88 8b       d8 ,adPPPPP88 8b       88 88 88       88 8b       88  
    88 "8a,   ,a8" 88,    ,88 "8a,   ,d88 88 88       88 "8a,   ,d88  
    88  `"YbbdP"'  `"8bbdP"Y8  `"8bbdP"Y8 88 88       88  `"YbbdP"Y8  
                                                          aa,    ,88  
                                                           "Y8bbdP"   """)
def ocean(): #ascii art ocean
    print("""              |
                \ _ /
              -= (_) =-                 
                /   \                          _\/_
                  |                            //o\  _\/_
        _  ___  __  _ __ __ _  _ _  _ _ __  __ _ | __/o\\ _
      =-=-_=-=-_=-=_=-_=_=-_=-_-_=_=-= _=_=-=_,-'|"'""-|-,_ 
       =- _=-=-_=- _=-= _--_ =-= -_=-=_-=_,-"          |
         =- =- =-= =- = -  -===- -= -= ."                 """)

def dancing(): #ascii art dancing
    print("""     |-----------------------------------------------------------------------|
    |    o   \ o /  _ o         __|    \ /     |__        o _  \ o /   o    |
    |   /|\    |     /\   ___\o   \o    |    o/    o/__   /\     |    /|\   |
    |   / \   / \   | \  /)  |    ( \  /o\  / )    |  (\  / |   / \   / \   |
    |-----------------------------------------------------------------------|""")

def dancingTwo(): #ascii art of people dancing
    print("""   _O/                   ,
         \                  /           \O_
         /\_             `\_\        ,/\/
         \  `       ,        \         /
         `       O/ /       /O\        \
                 /\|/\.                `""")
def glider():
    print("\t \t \t   _________")
    print("\t \t \t  /         \'")
    print("\t \t \t / _   _   _ \'")
    print("\t \t \t |/ \ / \ / \|")
    print("\t \t \t  \  | _ |  /")
    print("\t \t \t   o `(_}' o")
    print("\t \t \t    \/.X.\/")
    print("\t \t \t      |_|")
    print("\t \t \t     // \\'")
    print("\t \t \t     \\\ //")
    print("\t \t \t      U U ")

def shoppingCart():
    print("""   _
        \________
     ~   \\######/       
      ~   |####/
     ~    |____.
    ______o____o__________ 
                      \_______""")

def victoryRoyale():
    print("""     __________________________________________________________________________________________________________________________________________________________
    |                                                                                                                                                          |														  |
    |    __________________________________________________________________________________________________________________________________________________    |
    |   |      ___      ___  __     ______  ___________  ______     _______   ___  ___       _______     ______  ___  ___  __      ___       _______       |   |
    |   |     |"  \\    /"  ||" \\   /" _  "\\("     _   ")/    " \\   /"      \\ |"  \\/"  |     /"      \\   /    " \\"  \\/ "  |/""\\    |"  |     /"     "|      |   |
    |   |      \\   \\  //  / ||  | (: ( \\___))__/  \\\\__/// ____  \\ |:        | \\   \\  /     |:        | // ____        \\\\   \\/    \\||  |    (: ______)      |   |
    |   |       \\\\  \\/. ./  |:  |  \\/ \\       \\_ /  /  /    )   :)|_____/   )  \\\\  \\/      |_____/   )/  /    ) :)   \\\\//' /\\  \\  |:  |     \\/    |        |   | 
    |   |        \\.    //   |.  |  //  \\ _     |.  | (: (____/ //  //      /   /   /        //      /(: (____/ // /   /// __ '  \\  \\  |___  // ___)_       |   | 
    |   |         \\\\   /    /\\  |\\(:   _) \\    \\:  |  \\        /  |:  __   \\  /   /        |:  __   \\ \\        / /   //   /  \\\\  \\( \\_|:  \\(:      "|      |   | 
    |   |          \\__/    (__\\_|_)\\_______)    \\__|   \\"_____/   |__|  \\___)|___/         |__|  \\___) \\"_____/ |___/(___/    \\___)\\_______)\\_______)      |   |
    |   |__________________________________________________________________________________________________________________________________________________|   |
    |                                                                                                                                                          |
    |__________________________________________________________________________________________________________________________________________________________|""")

def thanksForPlaying():
    print("""\t \t      ___           ___           ___           ___           ___                    ___         ___           ___     
          ___        /__/\\         /  /\\         /__/\\         /__/|         /  /\\                  /  /\\       /  /\\         /  /\\    
         /  /\\       \\  \\:\\       /  /::\\        \\  \\:\\       |  |:|        /  /:/_                /  /:/_     /  /::\\       /  /::\\   
        /  /:/        \\__\\:\\     /  /:/\\:\\        \\  \\:\\      |  |:|       /  /:/ /\\              /  /:/ /\\   /  /:/\\:\\     /  /:/\\:\\  
       /  /:/     ___ /  /::\\  /  /:/~/::\\   _____\\__\\:\\   __|  |:|      /  /:/ /::\\            /  /:/ /:/  /  /:/  \\:\\   /  /:/~/:/  
      /  /::\\    /__/\\  /:/\\:\\ /__/:/ /:/\\:\\ /__/::::::::\\ /__/\\_|:|____ /__/:/ /:/\\:\          /__/:/ /:/  /__/:/ \\__\\:\\ /__/:/ /:/___
     /__/:/\\:\\   \\  \\:\\/:/__\\/ \\  \\:\\/:/__\\/ \  \\:\\~~\\~~\\/ \\  \\:\\/:::::/ \\  \\:\\/:/~/:/          \\  \\:\\/:/   \\  \\:\\ /  /:/ \\  \\:\\/:::::/
     \\__\\/  \\:\\   \\  \\::/       \\  \\::/       \\  \\:\\  ~~~   \\  \\::/~~~~   \\  \\::/ /:/            \\  \\::/     \\  \\:\\  /:/   \\  \\::/~~~~ 
          \\  \\:\\   \\  \\:\\        \\  \\:\\        \\  \\:\\        \\  \\:\\        \\__\\/ /:/              \\  \\:\\      \\  \\:\\/:/     \\  \\:\\     
           \\__\\/    \\  \\:\\        \\  \\:\\        \\ \\:\\        \\  \\:\\         /__/:/                \\  \\:\\      \\  \\::/       \\  \\:\\    
                     \\__\\/         \\__\\/         \\__\\/         \\__\\/         \\__\\/                  \\__\\/       \\__\\/         \\__\\/    
                                              ___                       ___                                   ___           ___        
                                             /  /\\                     /  /\\          ___       ___          /__/\\         /  /\\       
                                            /  /::\\                   /  /::\\       /__/|     /  /\\         \\  \\:\\       /  /:/_      
                                           /  /:/\\:\\  ___     ___    /  /:/\\:\\      |  |:|    /  /:/          \\  \\:\\     /  /:/ /\\     
                                          /  /:/~/:/ /__/\\   /  /\\  /  /:/~/::\\     |  |:|   /__/::\\      _____\\__\\:\\   /  /:/_/::\\    
                                         /__/:/ /:/  \\  \\:\\ /  /:/ /__/:/ /:/\\:\\  __|__|:|   \\__\\/\\:\\__  /__/::::::::\\ /__/:/__\\/\\:\\   
                                         \\  \\:\\/:/    \\  \\:\\  /:/  \\  \\:\\/:/__\\/ /__/::::\\      \\  \\:\\/\\ \\  \\:\\~~\\~~\\/ \\  \\:\\ /~~/:/   
                                          \\  \\::/      \\  \\:\\/:/    \\  \\::/         ~\\~~\\:\\      \\__\\::/  \\  \\:\\  ~~~   \\  \\:\\  /:/    
                                           \\  \\:\\       \\  \\::/      \\  \\:\\           \\  \\:\\     /__/:/    \\  \\:\\        \\  \\:\\/:/     
                                            \\  \\:\\       \\__\\/        \\  \\:\\           \\__\\/     \\__\\/      \\  \\:\\        \\  \\::/      
                                             \\__\\/                     \\__\\/                                 \\__\\/         \\__\\/""")

def gameOverText():
    print("""     ___    _____         ___    _____  _   _  ___    ___   
    (  _`\ (  _  )/'\_/`\(  _`\ (  _  )( ) ( )(  _`\ |  _`\ 
    | ( (_)| (_) ||     || (_(_)| ( ) || | | || (_(_)| (_) )
    | |___ |  _  || (_) ||  _)_ | | | || | | ||  _)_ | ,  / 
    | (_, )| | | || | | || (_( )| (_) || \_/ || (_( )| |\ \ 
    (____/'(_) (_)(_) (_)(____/'(_____)`\___/'(____/'(_) (_)""")



def playerStatsText():
    print("""      ____  _        _ __   _______ ____    ____ _____  _  _____ ____  
     |  _ \\| |      / \\\\ \\ / / ____|  _ \\  / ___|_   _|/ \|_   _/ ___| 
     | |_) | |     / _ \\ \V /|  _| | |_) | \\___ \\ | | / _ \\ | | \\___ \\ 
     |  __/| |___ / ___ \\| | | |___|  _ <   ___) || |/ ___ \\| |  ___) |
     |_|   |_____/_/   \\_\\_| |_____|_| \\_\\ |____/ |_/_/   \\_\\_| |____/ 
                                                                       """)

def combatText():
    print("""  _________  __  ______  ___ ______
 / ___/ __ \\/  |/  / _ )/ _ /_  __/
/ /__/ /_/ / /|_/ / _  / __ |/ /   
\\___/\\____/_/  /_/____/_/ |_/_/""")


def stageOneText():
    print("""   _____________  _________  ___
  / __/_  __/ _ |/ ___/ __/ <  /
 _\\ \\  / / / __ / (_ / _/   / / 
/___/ /_/ /_/ |_\\___/___/  /_/""")

def stageTwoText():
    print("""   _____________  _________  ___ 
  / __/_  __/ _ |/ ___/ __/ |_  |
 _\\ \\  / / / __ / (_ / _/  / __/ 
/___/ /_/ /_/ |_\\___/___/ /____/ """)

def winWinText():
    print("""    ▓██   ██▓ ▒█████   █    ██     █     █░ ██▓ ███▄    █ 
     ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓█░ █ ░█░▓██▒ ██ ▀█   █ 
      ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒█░ █ ░█ ▒██▒▓██  ▀█ ██▒
      ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░█░ █ ░█ ░██░▓██▒  ▐▌██▒
      ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░░██▒██▓ ░██░▒██░   ▓██░
       ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒    ░ ▓░▒ ▒  ░▓  ░ ▒░   ▒ ▒ 
     ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░      ▒ ░ ░   ▒ ░░ ░░   ░ ▒░
     ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░      ░   ░   ▒ ░   ░   ░ ░ 
     ░ ░         ░ ░     ░            ░     ░           ░ 
     ░ ░                                                  """)

##########################################################################################################################################################################################################

def introTrapped():
    os.system('cls')
    print("\n \n \n \n \n")
    print("_____________________    _____ _______________________________________"  )
    time.sleep(1)
    print("\__    ___/\______   \  /  _  \\______   \______   \_   _____/\______ \ ")
    time.sleep(1)
    print("  |    |    |       _/ /  /_\  \|     ___/|     ___/|    __)_  |    |  \ ")
    time.sleep(1)
    print("  |    |    |    |   \/    |    \    |    |    |    |        \ |    `   \ ")
    time.sleep(1)
    print("  |____|    |____|_  /\____|__  /____|    |____|   /_______  //_______  /")
    time.sleep(1)
    print("                   \/         \/                           \/         \/ ")
    print("\n \n \n")
    print("\t \t  A Fortnite Textbased Adventure Game")
    print("\t \t \t Created by Isshana")
    print("\n \n \n")
    print("\t \t \t START GAME \t [S] \n")
    print("\t \t \t INSTRUCTIONS \t [I] \n")
    navigateIntro()

def navigateIntro(): 
    navigate=input("")
    if (navigate=="s") or (navigate=="S") or (navigate=="start") or (navigate=="Start") or (navigate=="START"):
        print("\n"*15)
    elif (navigate=="i") or (navigate=="I") or (navigate=="instructions") or (navigate=="Instructions") or (navigate=="INSTRUCTIONS"):
        instructions()
    else:
        print("Error")
        navigateIntro()

def instructions():
    os.system('cls')
    print("\n \n")
    print("Trapped is a Text-based Adventure game based on the popular game Fortnite: Battle Royale. You are up late night playing your favourite game of the season ")
    print("knowing very well that you have an important test the next day. You end up falling asleep mid-game only to wake up realizing that you are in the game itself. A")
    print("mysterious voice tells you that the only way to escape the game and return back to reality is to get a Victory Royale. He also informs you that if you get eliminated, ")
    print("that’s the end of your life. You pretty much have no choice but to win the game! Good Luck on your win to survival! \n \n \n")
    print("How to Play: \n")
    print("This is a text-based adventure game, which means that there aren’t necessarily any controls. To play you have to type in the corresponding commands which directed to.\n \n")
    print("\t \t For example:\n")
    print("\t \t \t [1] Hide")
    print("\t \t \t [2] Run \n \n")
    print("\t \t \t >>> 2 \n")
    print("If you type in the input 2, then your character will decide to run. Numbers will ONLY be accepted (unless specified to type characters). Yes or no questions typed in all lowercase. If you type in an invalid command then the game \n will prompt you to enter a valid command.")
    print("\n \n How to Win: \n")
    print("\t To win you simply just have to finish the game! Gain a Victory Royale and you’ll be set-free from this world.")
    print("\n \n What to Expect: \n")
    print("\t You will be expected to get weapons, use meds such as shields and bandages, and battle other players to win. There will be combat rounds where you will have to verse")
    print("\t an opponent, if you get eliminated then you lose the game. You can also get eliminated by the storm if you are caught within it, so think smart.")
    print("\n \n Combat Rounds: \n")
    print("In combat rounds you will have to do as each stage instructs you to do to battle against the other player. This can be done by making")
    print("decisions and entering them when prompted to.\n \n \n")
    print("To return to the main menu type “Main Menu”.")
    promptOne="choose"
    while (promptOne!="Main Menu"):
        promptOne=input("") 
        if (promptOne=="Main Menu"):
            introTrapped()
        else: 
            print("Error\n")



#BEFORE ANY HEALTH LOSS
########################################################################################################################################################################################################

def partOne(): 
    os.system('cls')
    print('"Wow eliminated after 8 kills, AND TOP 7???"')
    time.sleep(timeOne)
    print('"Are you seriously kidding me?"')
    time.sleep(timeOne)
    print("\t You take off your headset and glance at the time")
    print("\n \n \n")
    time.sleep(timeOne)
    oneOClock()
    time.sleep(3)
    print("\n \n \n")
    print('"Shoot, moms totally gonna kill me"')
    time.sleep(timeOne)
    print("\t You know very well that you have your HL Bio exam the next day")
    time.sleep(timeOne)
    print("\t You think to yourself...")
    time.sleep(3)
    print("Should I go to bed ... or keep playing for another 'Victory Royale'?\n \n")
    time.sleep(timeOne)
    print(" [1] Go to bed \n [2] Keep playing \n \n")



def partOneChoiceOne():
        print("\t You turned off your PC and got a glass of water before going off to bed")
        time.sleep(timeOne)
        print("\t You quickly changed into your PJs, brushed your teeth and set the clothes that you need for tomorrow")
        time.sleep(timeOne)
        print("\t You lie down in bed, and try to go to sleep")
        time.sleep(5)
        print("\t You check the time again")
        print("\n \n \n")
        time.sleep(4)
        twoOClock()
        print("\n \n \n")
        time.sleep(4)
        print('"Theres no point in even trying to sleep"')
        time.sleep(timeOne)
        print('"Im probably just gonna play some more fort"')
        time.sleep(timeOne)
        print("\t You got your phone out and opened fortnite")
        time.sleep(timeOne)
        print("\t You know what you were doing was wrong but you could care less to be honest")
        time.sleep(timeOne)
        print("\t You kept playing and before you knew it, you went to sleep")


def partOneChoiceTwo():
        print("You changed your skin and started up another game")
        time.sleep(timeOne)
        print("You were totally into the game")
        time.sleep(timeOne)
        print("You kept on playing, game after game")
        time.sleep(timeOne)
        print("Sadly, no Victory Royale")
        time.sleep(timeOne)
        print("Eventually you just passed out into a deep sleep")


def partOneChoice(): 
    choiceOne="choose" 
    while (choiceOne!="1") or(choiceOne!="sleep") or (choiceOne!="2") or (choiceOne!="Keep playing"):
        choiceOne=input("I think I might \t")
        if (choiceOne=="1"):
            partOneChoiceOne()
            break
        elif (choiceOne=="2"):
            partOneChoiceTwo()
            break
        else:
            print("ERROR \n \n")

def partTwo():
    time.sleep(5)
    os.system('cls')
    time.sleep(timeOne)
    print("\n The Next Morning .", end="")
    time.sleep(timeOne)
    print("\t .", end="")
    time.sleep(timeOne)
    print("\t .", end="")
    time.sleep(timeOne)
    print("\t .", end="")
    time.sleep(timeOne)
    print("\t .", end="")
    time.sleep(timeOne)
    print("\t .")
    time.sleep(3)
    sun()
    print("\n \n \n")
    time.sleep(timeOne)
    print("You get up and look around")
    time.sleep(timeOne)
    print("Where are you...?")
    time.sleep(timeOne)
    print("Everything looks unfamiliar")
    time.sleep(timeOne)
    print("You get up and look around")
    time.sleep(timeOne)
    print("Behind you looks like a foggy forest scene")
    time.sleep(timeOne)
    print("You keep looking around")
    time.sleep(timeOne)
    print("Infront of you, everything looks dark blue")
    time.sleep(timeOne)
    print("This is definitely not your room")
    time.sleep(timeOne)
    print('\t "MOOOOM WHERE ARE YOU???"')
    time.sleep(timeOne)
    print('\t"I have my biology exam today, we have to go to school!!"')
    time.sleep(timeOne)
    print("You keep calling out but no one answers")
    time.sleep(timeOne)
    print("Soon you look under you and you notice that you are standing on a circular platform with the letter V engraved within")
    time.sleep(timeOne)
    print("You think to yourself, all of these things look strikingly familiar to Fortnite's lobby screen")
    time.sleep(timeOne)
    print("Suddenly you hear a voice")
    time.sleep(timeOne)
    print('\t \t \t "Are you a boy or girl?"')
    time.sleep(timeOne)
    print('\t "What?" you reply')
    time.sleep(timeOne)
    print('\t \t \t Answer me, Are you a boy or girl?" \n \n')
    time.sleep(timeOne)

def partThree():
    print('\t"Why do you ask?"')
    time.sleep(3)
    print("The voice goes silent for a moment")
    time.sleep(timeOne)
    print('\t \t \t "What is your name?"')

def partFour(): 
    time.sleep(timeOne)
    print('\t \t \tVery well then', name, '... Choose a skin \n \n')

def partFive(): 
    print('\t \t \t"Looks like your ready."')
    time.sleep(timeOne)
    print('\t \t \t"I will now explain the rules to you."')
    time.sleep(timeOne)      
    print('\t \t \t"The goal is for you to survive the whole game."') 
    time.sleep(timeOne)          
    print('\t \t \t"The rules are the same as any normal game Battle Royale game you would play in Fortnite, including the special modes."')
    time.sleep(timeOne)
    print('\t \t \t"Lets see what game mode you get to play..."')
    time.sleep(3)
    print('\n'*7)
    print('\t'+ "*"*80)
    print("\n")
    soloShowdown()
    print("\n")
    print('\t'+ "*"*80)
    print('\n'*7)
    time.sleep(3)
    print('\t "Bruh, are you for real?"')
    time.sleep(timeOne)
    print("There was no way that I could verse the best of the best")
    time.sleep(timeOne)
    print("Solo Showdown is where the best of best are!")
    time.sleep(timeOne)
    print("How am I supposed to win a game there, I'm wadgering my life on the line")
    time.sleep(timeOne)
    print('\t"Sir isnt there any way that you can make it regular solo?"')
    time.sleep(timeOne)
    print('\t"This is too hard for me to compete in!"')
    time.sleep(timeOne)
    print('\t \t \t"Nope, Im sorry, you can either forfeit now and lose your life or play to win"')
    time.sleep(timeOne)
    print("I guess I have no choice")
    time.sleep(3)
    print('\t"Ok, Im ready"')
    time.sleep(timeOne)
    print('\t"Lets do this!!"')
    time.sleep(5)
    os.system('cls')
    time.sleep(5)
    print("\n \n \n \n \n \n")
    loading()
    print("\n \n \n \n \n \n")
    time.sleep(7)
    print("You've now been transported to the the pre-game lobby")
    time.sleep(timeOne)
    print("It all looks so realistic")
    time.sleep(timeOne)
    print("You start having mixed feeling about the situation that your in...")
    time.sleep(timeOne)
    print('You know that you are risking your life now, and this "Victory Royale" must be acheived')
    time.sleep(timeOne)
    print('At the same time, you feel the adrenaline rushing in. How lucky you are to get this oppurtunity')
    time.sleep(timeOne)
    print("Infront of you are mountains")
    time.sleep(timeOne)
    print("\n \n \n \n")
    mountain()
    print("\n \n \n \n")
    time.sleep(2)
    print("Behind you is the ocean")
    time.sleep(timeOne)
    print("\n \n \n \n")
    ocean()
    print("\n \n \n \n")
    time.sleep(2)
    print("You walk around the map admiring the beauty of the island")
    time.sleep(timeOne)
    print("As you're walking, you see an unordinary skin combo")
    time.sleep(timeOne)
    print("It's a Skull Trooper skin paired with a Brite bag")
    time.sleep(timeOne)
    print("He must be an amazing player, you think to yourself as you admire him from afar")
    time.sleep(timeOne)
    print("Maybe he might be able to give you some tips to win the game")
    time.sleep(timeOne)
    print("\n \n \t \t \t Do you approach him?")
    print("\t \t \t [1] He seems nice, this could definitely be a great oppurtunity! \n \t \t \t [2] He looks pretty rude, maybe I should just mind my own business")

def talkRude():
    print("You go up to him and start the conversation")
    time.sleep(timeOne)
    print('\t"Hey there!')
    time.sleep(timeOne)
    print('\t \t \t "What do you want?!"')
    time.sleep(timeOne)
    print("Looks like he's not really that nice")
    time.sleep(timeOne)
    print('\t \t \t"Can you mind your own business like for gods sake!"')
    time.sleep(timeOne)
    print('\t"Sorry, I think I will just go"')
    time.sleep(timeOne)
    print("He glares at you and you just run away, that wasn't such a nice encounter")
    time.sleep(timeOne)

def talkNice():
    print("You go up to him and start the conversation")
    time.sleep(timeOne)
    print('\t"Hey there!')
    time.sleep(timeOne)
    print('\t \t \t"Oh hi there, whats up?"')
    time.sleep(timeOne)
    print("Looks like he's nice after all, lucky you")
    time.sleep(timeOne)
    print('\t"This is my first time playing this version, do you have any tips?"')
    time.sleep(timeOne)
    print('\t \t \t"Ooh interesting, first time can be a bit nerve-wracking, dont worry though"')

def talkNiceGirl():
        print('\t \t \t"That skin looks really nice on you"')
        time.sleep(timeOne)
        print('\t \t \t"I\'m impressed too, there aren\'t usually many female players"')
        time.sleep(timeOne)
        print("He seems like a really cool guy")
        time.sleep(timeOne)
        print('\t"Wow, I didn\'t know!"')
        time.sleep(timeOne)
        
def talkNiceBoy():
    print('\t \t \t"That skin looks pretty cool"')
    time.sleep(timeOne)
    print('\t \t \t"I\'m impressed, it just came out recently"')
    time.sleep(timeOne)
    print("He seems like a really cool guy")
    time.sleep(timeOne)
    print('\t"Wow, I didn\'t know!"')

def talkNiceTwo():
    print('\t \t \t"I\'ll give you some landing tips"')
    time.sleep(timeOne)
    print('\t \t \t"Landing at Tilted Towers might be a good choice this round"')
    time.sleep(timeOne)
    print('\t \t \t"Dont stress too much though, if you dont win this time, theres always next time!"')
    time.sleep(timeOne)
    print("A next time... I sure wish")

def talkRudeTwo():
    print('\t"Yeah, I think this is the right choice, hes way outta my league"')
    time.sleep(timeOne)
    print('You avoid him')
    time.sleep(timeOne)

def playerStats():
    playerStatsText()
    print("\n \n")
    print("%25s" % "     .  .-+  ._/V\\           ", end="")
    print("%25s" % name +"'s stats")
    print("%25s" % "    / \\/   \\/    /__        ", end="")
    print("%25s" % "Kills:", end="")
    print("%25s" % kills)
    print("%25s" % "   )                -+._z     ",end="")
    print("%25s" % "People Left:", end="")
    print("%25s" % people)
    print("%25s" % '  /                      \\   ', end="")
    print("%25s" % "Distance Travelled:", end="")
    print("%25s" % distanceTravelled+"km")
    print("%25s" % " (     TILTED TOWERS       )  ")
    print("%25s" % "   \\                      /  ")
    print("%25s" % "     \\__                 (   ")
    print("%25s" % "        >_               )    ", end="")
    print("%25s" % "HEALTH:", end="")
    print("%25s" % health)
    print("%25s" % "          \\_. WAILING   /    ", end="")
    print("%25s" % "SHIELD:", end="")
    print("%25s" % shield)
    print("%25s" % "            < WOODS   /       ")
    print("%25s" % "              \\   *  _/      ")
    print("%25s" % "               >    º         ")
    print("%25s" % "              /    /          ")
    print("%25s" % "             <    /           ")
    print("%25s" % "              '^./            ")
    print("\n \n \t \tI N V E N T O R Y:")
    print("%25s" % "Slot 1:", end="")
    print("%25s" % "Pickaxe")
    print("%25s" % "Slot 2:", end="")
    print("%25s" % slotTwo)
    print("%25s" % "Slot 3:",end="")
    print("%25s" % slotThree)
    print("%25s" % "Slot 4:",end="")
    print("%25s" % slotFour)
    print("%25s" %"Slot 5:",end="")
    print("%25s" % slotFive)
    print("%25s" % "Slot 6:",end="")
    print("%25s" % slotSix)
    print("\n \t \t R E S O U R C E S:")
    print("%25s" % "Wood:",end="")
    print("%25s" % wood)
    print("%25s" % "Brick:", end="")
    print("%25s" % brick)
    print("%25s" % "Metal:",end="")
    print("%25s" % metal)
    print("%25s" % "Wall Traps:",end="")
    print("%25s" % traps)
    print("%25s" % "Launch Pad:",end="")
    print("%25s" % launchpad)
    print("\n \n \n")
    
def partSix():
    print('You decide to go towards the group of people dancing')
    time.sleep(timeOne)
    print("\n \n")
    dancing()
    print("\n \n")
    time.sleep(3)
    print("You see them all dancing and they are all so great")
    time.sleep(timeOne)
    print("\n \n")
    dancingTwo()
    print("\n \n")
    time.sleep(3)
    print("You wonder if you can pull it off, so you decide to try")
    time.sleep(timeOne)
    print("Looks like it wasn't as easy as you thought")
    time.sleep(timeOne)
    print("The counter starts which means it's time to get on the Battle Bus")
    time.sleep(timeOne)
    print("Everyone starts rushing towards the bus")
    time.sleep(timeOne)
    print("It starts getting crowded but you've gotten a seat")
    time.sleep(timeOne)
    print("Different people with different skins, back blings, and pickaxes all run onto the bus")
    time.sleep(timeOne)
    print("The bus starts up and flys into the air")
    time.sleep(timeOne)
    print("Everybody gets out their maps and starts planning locations")
    playerStats()

def partSixTwo():
    time.sleep(timeOne)
    print("There are so many locations to land at but it seems as if you are going to choose between two options, Tilted Towers or Wailing Woods?")
    time.sleep(timeOne)

def ttOne():
    print("You wait until the battle bus comes near Tilted Towers")
    time.sleep(timeOne)
    print("The bus gets near and you prepare to jump")
    time.sleep(timeOne)
    print("You check the map")
    time.sleep(timeOne)
    
def ttTwo():
    time.sleep(timeOne)
    print("Its time to jump, you pull out your glider and jump off the bus\n \n")
    time.sleep(timeOne)
    glider()
    time.sleep(timeOne)
    print("\n \n There are lots of people also landing here")
    time.sleep(timeOne)
    print("Which building do you want to land at?")
    print("\t \t \t \n [1] Trump Tower \t \t \t \n [2] Bell Tower")

def tttOne():
    print("You've decided to land at the Trump Tower")
    time.sleep(timeOne)
    print("You navigate your glider towards the Trump Tower")
    time.sleep(timeOne)
    print("You look all over you and there are quite a few other people landing here")
    time.sleep(timeOne)
    print("You land at the Trump Tower")

def tttTwo():
    time.sleep(timeOne)
    print("Looks like you haven't landed alone")
    time.sleep(timeOne)
    print("There are 4 other people at this tower")
    time.sleep(timeOne)
    print("You knew it was the most crowded building but you still decided to land here")
    time.sleep(timeOne)

def tttThree():
    time.sleep(timeOne)
    print("Somehow by miracle")
    time.sleep(timeOne)
    print("You got to the chest first")

def tttFour():
    print("You use your", slotThree, "to eliminate the other 4 players")
    time.sleep(timeOne)
    print("Wow, the game just started and you alerady got 4 kills, pretty impressive")
    time.sleep(timeOne)
    print("You check player stats")
    time.sleep(timeOne)

def tttDeathOne():
    time.sleep(timeOne)
    print("You are lucky and land in the building alone, how rare")
    time.sleep(timeOne)
    print("You start looting and you get quite some loot")
    time.sleep(timeOne)
    print("Just then you hear something")
    time.sleep(timeOne)
    print("You don't mind too much about it")
    time.sleep(timeOne)
    print("A few moments you are shot down")
    time.sleep(timeOne)
    print("Turns out that someone had used a pistol to eliminate you")
    time.sleep(timeOne)
    print("You die")

def tttDeathTwo():
    print("Unfortunately you didn't get the chest")
    time.sleep(timeOne)
    print("One of the other players is shooting while everyone else is pickaxing each other")
    time.sleep(timeOne)
    print("You notice your health going down")
    time.sleep(timeOne)
    ripYou=100
    ripYouu=1
    for x in range (11):
        print("\t"*(ripYouu), ripYou)
        ripYou=ripYou-10
        ripYouu=ripYouu+1
        time.sleep(timeOne)

    
def btOne():
    print("You've decided to land at the Bell Tower")
    time.sleep(timeOne)
    print("You navigate your glider towards the Bell Tower")
    time.sleep(timeOne)
    print("You look all over you and there are quite a few other people landing here")
    time.sleep(timeOne)
    print("You land at the Bell Tower")

def btDeathOne():
    time.sleep(timeOne)
    print("You are lucky and land in the building alone")
    time.sleep(timeOne)
    print("You start looting and you get quite some loot")
    time.sleep(timeOne)
    print("Just then you hear something being broken")
    time.sleep(timeOne)
    print("You don't mind too much about it")
    time.sleep(timeOne)
    print("A few moments later you fall down")
    time.sleep(timeOne)
    print("Turns out that someone had used C4s to break the Bell Tower's base")
    time.sleep(timeOne)
    print("You fall to your death")

def btTwo():
    time.sleep(timeOne)
    print("Looks like you haven't landed alone")
    time.sleep(timeOne)
    print("There are 4 other people at this tower")
    time.sleep(timeOne)
    print("How amazing, 5 people in a 1x1 Bell Tower")
    time.sleep(timeOne)

def btDeathTwo():
    print("Unfortunately you didn't get the chest")
    time.sleep(timeOne)
    print("One of the other players is shooting while everyone else is pickaxing each other")
    time.sleep(timeOne)
    print("You notice your health going down")
    time.sleep(timeOne)
    ripYou=100
    ripYouu=1
    for x in range (11):
        print("\t"*(ripYouu), ripYou)
        ripYou=ripYou-10
        ripYouu=ripYouu+1
        time.sleep(timeOne)
        
def btThree():
    time.sleep(timeOne)
    print("Somehow by miracle")
    time.sleep(timeOne)
    print("You got to the chest first")

def btFour():
    print("You use your", slotTwo, "to eliminate the other 4 players")
    time.sleep(timeOne)
    print("Wow, the game just started and you alerady got 4 kills, pretty impressive")
    time.sleep(timeOne)
    print("You check player stats")
    time.sleep(timeOne)
    
def btFive():
    time.sleep(timeOne)
    print("You carefully run down the building, level by level")
    time.sleep(timeOne)
    print("You make it to the bottom of the building safely")
    time.sleep(timeOne)
    print("You open the door a peak out to see if anybody is nearby")
    time.sleep(timeOne)
    print("There's nobody there and so you decide to run to the little park")
    time.sleep(timeOne)
    print("You get to the park and see that there are apples on the floor")
    time.sleep(timeOne)
    
def btSix():
    print("You see a building behind the area that you are in")
    time.sleep(timeOne)
    print("You remember from all the other games that you've played at home that there is a basement in that building")
    time.sleep(timeOne)
    print("You run over to the building and go to the basement")
    time.sleep(timeOne)
    print("You see another chest! How lucky!")
    time.sleep(timeOne)
    print("You open the chest")

def btSeven():
    print("You finish looting")
    time.sleep(timeOne)
    print("You have nothing to do now because you are safe and are in the circle")
    time.sleep(timeOne)
    print("It doesn't look like any players are coming here for now")
    time.sleep(timeOne)
    print("You also do have the option to go look for combat")
    time.sleep(timeOne)

def llOne():
    print("You won the fight")
    time.sleep(timeOne)
    print("To avoid more danger you decide to leave Tilted Towers")
    time.sleep(timeOne)
    print("You start running towards Loot Lake")
    
def llThree():
    playerStats()
    time.sleep(timeOne)
    print("You make your way towards the house in the middle of Loot Lake")
    time.sleep(timeOne)
    print("You you crouch up the stairs")
    time.sleep(timeOne)
    print("Looks like there's another player there")
    time.sleep(timeOne)

def llTwo():
    time.sleep(5)
    print("After running for a while you've made it to Loot Lake")
    time.sleep(timeOne)
    print("You see a chest")
    time.sleep(timeOne)
    print("It's on one of the boats in the lake but you aren't sure if it's already been opened or not")
    time.sleep(timeOne)

def llFour():
    time.sleep(timeOne)
    print("You check the map for the storm")
    time.sleep(timeOne)
    print("The storm is close")
    time.sleep(timeOne)

def llLaunchpad():
    print("You know you have a launchpad")
    time.sleep(timeOne)
    print("You use the launchpad")
    time.sleep(timeOne)
    print("You build up a ramp high into the sky and place the Launch pad")
    time.sleep(timeOne)
    print("You fly into Dusty Divot without losing any health")
    time.sleep(5)

def llNoLaunchpad():
    time.sleep(timeOne)
    print("You pray and you start running as fast as you can")
    time.sleep(timeOne)
    print("Sadly you aren't fast enough and the storm does damage you")
    
def noRevive():
    print("You decided not to attempt to revive yourself")
    time.sleep(timeOne)
    
def stageOneRules():
    print("To pass stage One you must type out the woods as they are shown (punctuation and capitalization counts) to get a correct answer\n if you make a mistake you will lose health")

def stageTwoRules():
    print('To pass stage Two you must type either "shoot" or "defend" to shoot or defend the other player, if you type anything else you will lose 25 health')
    print("If you shoot and they shoot, then you lose 25 health")
    print("If you defend and they shoot, then the enemy loses 25 health")
    print("If you defend and they defend, the attacks cancel out")
    print("After every round in stage Two, the enemy will lose 10-15 health")

def dustyDivotOne():
    print("After some long and hard-fought battle you've made it to one of the final circles")
    time.sleep(timeOne)
    print("You check the player count and you notice that there are only 5 people left")
    time.sleep(timeOne)
    print("You can do this, just 4 other people besides yourself")
    time.sleep(timeOne)
    print("If you believe in yourself, you can accomplish your goals")
    time.sleep(timeOne)
    print("You decide to run and take cover behind one of the turned-over cars")
    time.sleep(timeOne)



def dustyDivotTwo():    
    print("As you are resting beside you, you see something moving")
    time.sleep(timeOne)
    print("You look closer and it's another player")
    time.sleep(timeOne)
    print("You pull out your gun")
    time.sleep(timeOne)
    print("You aim for a headshot and prepare to shoot")
    time.sleep(timeOne)
    print("You then notice that the player's hands go up")
    time.sleep(timeOne)
    print("He is singaling for surrender but you wonder why he is doing that in a Battle Royale")
    time.sleep(timeOne)
    print("He crouches to your car from behind his")
    time.sleep(timeOne)
    print("As he is coming closer, you look at him a recognize who he is")
    time.sleep(timeOne)
    time.sleep(timeOne)
    print("It's the Skull Trooper!!")
    time.sleep(timeOne)
    if (chat=="1"):
        print('\t"It\'s YOU!! From the pre-game lobby"')
        time.sleep(timeOne)
        print('\t \t \t Oh You were that', skin)
        time.sleep(timeOne)
    print('\t \t \t"Well I was going to ask, if you wanted to team up"')
    time.sleep(timeOne)
    print('\t \t \t"I heard that TSM_Myth and Ninja are playing in this game"')
    time.sleep(timeOne)
    print('\t"Are You for real? How are we supposed to win then?"')
    time.sleep(timeOne)
    print('\t \t \t"We can\'t win alone but we can together"')
    time.sleep(timeOne)
    print("He does have a great idea")
    time.sleep(timeOne)
    print("You guys could work together to win but it's a solo game")
    time.sleep(timeOne)
    print("There can only be one winner")
    time.sleep(timeOne)
    print('\t"But there can only be one winner"')
    time.sleep(timeOne)
    print('\t \t \t"We can teamup until we are the last two alive, then verse eachother for the win"')
    time.sleep(timeOne)
    print("That's a smart idea, you decide to go with it")
    time.sleep(timeOne)
    print('\t"Okay, Let\'s do it!"')
    time.sleep(timeOne)

def partTwelve():
    time.sleep(timeOne)
    print("You check again the number of players and its down to three!")
    time.sleep(timeOne)
    print("That can only mean that there is one other person apart from both of you left in the game")
    time.sleep(timeOne)
    print("You open up Player Stats")

    
def partThirteen():
    playerStats()
    time.sleep(timeOne)
    print("There's only two people left in the game")
    time.sleep(timeOne)
    print("Looks like its you and him")
    time.sleep(timeOne)
    print("This last combat is all it takes")
    time.sleep(timeOne)
    time.sleep(timeOne)
    print("You run around through the buildings and place traps")
    time.sleep(timeOne)
    print("You finally hear a rustle, then you hear footsteps")
    time.sleep(timeOne)
    print("After a moment of silence you start hearing rapid building")
    time.sleep(timeOne)
    print("You think to yourself, it's time for combat")
    time.sleep(timeOne)
    print("You run outside and prepare to fight...")

def partFourteen():
    print("The player goes down and vanishes from the world")
    time.sleep(timeOne)
    print("You are the only one left in the game")
    time.sleep(timeOne)
    print("You did it")
    time.sleep(timeOne)
    print("You won the game")
    time.sleep(timeOne)
    print("Infront of you, the best thing you've seen all day appears" + "\n"*5)
    time.sleep(3)
    victoryRoyale()
    endGameStatsWin()
    time.sleep(3)
    print("\n"*5)
    print("Suddenly everything goes black")
    time.sleep(5)
    print("You open your eyes again to see that you are back into the real world")
    time.sleep(timeOne)
    print("You look around and it seems as if you are in the cafeteria")
    time.sleep(timeOne)
    print("All around you, the other students are preparing to write an exam")
    time.sleep(timeOne)
    print("It takes you a while but then you realize that it's time to write your HL Biology exam")
    time.sleep(timeOne)
    print("You've made it back in time!")
    time.sleep(3)
    print("\n \n \t \t \t \t Gameover \n \t \t \t \t \t You Win!!")
    winWinText()
    endGameStatsWin()

def endGameStatsWin():
    print("\n"*3)
    print("%20s" % "Kills", end="")
    print("%20s" % "=", end="")
    print("%20s" % (kills))
    print("\n")
    print("%20s" % "Placing", end="")
    print("%20s" % "=", end="")
    print("%20s" % "1", end="")
    print("%20s" % "of 100")
    print("\n")
    print("%20s" % "Distance Travelled", end="")
    print("%20s" % "=", end="")
    print("%20s" % "10.79", end="")
    print("%20s" % "km")

def endGameCredits():
    print("\n \n \n")
    thanksForPlaying()
##########################################################################################################################################################################################################


##########################################################################################################################################################################################################
gamePlay="play"
while (gamePlay=="play"):
    gameStop="ALIVE" #This variable determines whether the game continues or stops
    kills=0 #This variable determines the number of kills the user obtains
    health=100 #This variable determines the health of the user, cannot go over 100 or less than 0
    shield=0 #This variable determines the shield that the user has (it is like an extra bar of health) cannot go over 100 or less than 0
    slotTwo="[empty]" #This variable determines what is in inventory slot 2
    slotThree="[empty]" #This variable determines what is in inventory slot 3
    slotFour="[empty]" #This variable determines what is in inventory slot 4
    slotFive="[empty]" #This variable determines what is in inventory slot 5
    slotSix="[empty]" #This variable determines what is in inventory slot 6
    wood=0 #This variable determines how much wood resources the user has
    brick=0 #This variable determines how much brick resources the user has
    metal=0 #This variable determines how much metal the user has
    traps=0 #This variable determines how many traps the user has
    launchpad=0 #This variable determines how many launch pads the user has
    distanceTravelled=0 #This variable determines how much distance the user travelled in the game
    people=100 #This variable determines how many other players are left in the game
    gender="choose" #This variable stores the gender of the user
    skin="choose" #This variable stores the skin that the user chooses
    chat="choose" #This variable determines whether the user wants to talk to the guy in the pre-game lobby or not
    landingLocation="choose" #This variable determines where the user is going to land
    landingBuilding="choose" #This variable determines which building th user wants to land at
    hatThree=random.randrange(2) #This variable determines the path the user chooses to go through
    revive="choose" #This variable is used when the user makes a decision which causes them to die and are given another chance come back into the game
    chaChing="choose" #This variable links the landings of Trump Tower and Bell Tower together
    chestLoot="choose" #This variable determines whether or not the user wants to open the chest
    healDD="choose" #This variable lets the user heal or not if they wish to at Dusty Divot
    apples="choose" #This variable lets the user gain some health back if they have less than 100
    introTrapped() #has the loading screen and the instructions
    partOne() #has the first part to the adventure, contains no choices or decisions
    partOneChoice() #depending on the events of the first part, user can choose a decision to make, contains 2 paths
    partTwo() #has the second part to adventure, contains no choices or decisions
    while(gender!="girl") or (gender!="boy"): #program is asking for gender of the user and stores it as the variable gender
        gender=input('\t Im a \t')
        if (gender=="female") or (gender=="Female") or (gender=="Girl") or (gender=="girl"):
            gender="girl"
            break
        elif (gender=="male") or (gender=="Male") or (gender=="Boy") or (gender=="boy"):
            gender="boy"
            break
        break
    partThree() #Asks user for name
    name=input('\t My name is \t')
    partFour() #Asks user to choose a skin
    if (gender=="girl"): #If gender=girl then the user can choose from the skins listed in this section
        while (skin!="Valor") or (skin!="Shadow Ops") or (skin!="Triple Threat"):
            print("\t \t \t Valor \n \t \t \t Shadow Ops \n \t \t \t Triple Threat \n \t \t \t No Skin")
            skin=input("Skin:")
            if (skin=="no skin") or (skin== "No skin") or (skin=="No Skin"):
                randomizer=random.randrange(2)
                if (randomizer==0):
                    print('\t"What am I? Poor? I think I will choose another skin"')    
                elif (randomizer==1):
                    print("I am definietly not a noob, this is not the skin")
            elif (skin=="Valor") or (skin=="Shadow Ops") or (skin=="Triple Threat"):
                randomizer=random.randrange(3)
                if (randomizer==0):
                    print("Oh yes!", skin, "is totally my type")
                elif (randomizer==1):
                    print("Sickk!", skin, "looks so cool on me")
                elif (randomizer==2):
                    print(skin,"makes me look amazing")
                break
    elif (gender=="boy"): #If gender=boy then the user can choose from the skins listed in this section    
        while (skin!="Omega") or (skin!="Raven") or (skin!="Jumpshot"):
            print("\n \t \t \t Omega \n \t \t \t Raven \n \t \t \t Jumpshot\n \t \t \t No Skin \n \n")
            skin=input("Skin:")
            if (skin=="no skin") or (skin== "No skin") or (skin=="No Skin"):
                randomizer=random.randrange(2)
                if (randomizer==0):
                    print('\t"What am I? Poor? I think I will choose another skin"')    
                elif (randomizer==1):
                    print("I am definietly not a noob, this is not the skin")
            elif (skin=="Omega") or (skin=="Raven") or (skin=="Jumpshot"):
                randomizer=random.randrange(3)
                if (randomizer==0):
                    print("Oh yes!", skin, "is totally my type")
                elif (randomizer==1):
                    print("Sickk!", skin, "looks so cool on me")
                elif (randomizer==2):
                    print(skin,"makes me look amazing")
                break
    partFive() #The mysterious voice explains deeper what is going on, the user is then transported to the pre-game lobby
    while(chat!="1") and (chat!="2"):
        chat=input("I'm going to\t")
        if (chat=="1"):
            if (skin=="Valor") or (skin=="Raven") or (skin=="Omega"):
                talkRude() #The play in the pre-game lobby decides to be mean
            elif (skin=="Shadow Ops") or (skin=="Triple Threat") or (skin=="Jumpshot"):
                talkNice()
                if (gender=="girl"):
                    talkNiceGirl() #The player says something nice specifically if the user is a girl
                elif (gender=="boy"):
                    talkNiceBoy() #The player says something nice specifically if the user is a boy
                talkNiceTwo() #The player recommends a landing spot to the user           
        elif (chat=="2"):
            talkRudeTwo() #The user decides to avoid the player
    partSix() #The user walks away from the player and to some other people
    if (skin=="Shadow Ops") or (skin=="Triple Threat") or (skin=="Jumpshot"): #If the user has these skins they say this
        print("The guy said to land at Tilted Towers it could be a wiser choice")
    partSixTwo() #The user is deciding where to land
    time.sleep(5)
    os.system('cls')
    while (landingLocation!="Tilted Towers"):
            landingLocation=input("I feel like landing at:")
            time.sleep(timeOne)
            if (landingLocation=="Tilted Towers"):
                print("Tilted it is")            
            elif (landingLocation=="Wailing Woods"):
                print("Tilted Towers is the best choice")
                time.sleep(timeOne)
                print("I don't want to go there")

    ttOne() #The user describes the place they are coming to
    ttTwo() #The user describes Tilted
    while (landingBuilding!="Bell Tower") and (landingBuilding!="Trump Tower") and (landingBuilding!="1") and (landingBuilding!="2"):
        landingBuilding=input('"I\'m going to land at the"')
    while (gameStop!="DEAD"):
        if (landingBuilding=='1') or (landingBuilding=="Trump Tower"):
            tttOne
            if (hatThree==0):
                tttDeathOne()
                health=0
                while (revive!="yes") and (revive!="no"):
                    revive=input("Do you want to revive yourself?")
                if (revive=="yes"):
                    reviveCheck=int(3)
                    print("Type the following words exactly as shown")
                    for x in range(5):
                        if (reviveCheck>0):
                            reviveWords=random.randrange(4)
                            if (reviveWords==0):
                                print("stairs")
                                reviveResponse=input("")
                                if (reviveResponse!="stairs"):
                                    reviveCheck=reviveCheck-1
                                    print("You typed it wrong")
                                    print("Revival Attempts",reviveCheck)
                            elif (reviveWords==1):
                                print("Roof!")
                                reviveResponse=input("")
                                if (reviveResponse!="Roof!"):
                                    reviveCheck=reviveCheck-1
                                    print("You typed it wrong")
                                    print("Revival Attempts",reviveCheck)
                            elif (reviveWords==2):
                                print("wall.")       
                                reviveResponse=input("")
                                if (reviveResponse!="wall."):
                                    reviveCheck=reviveCheck-1
                                    print("You typed it wrong")
                                    print("Revival Attempts",reviveCheck)
                            elif (reviveWords==3):
                                print("Floor")
                                reviveResponse=input("")
                                if (reviveResponse!="Floor"):
                                    reviveCheck=reviveCheck-1
                                    print("You typed it wrong")
                                    print("Revival Attempts",reviveCheck)
                    if (reviveCheck<1):
                        print("You died")
                        gameStop="DEAD"
                        break
                    if(reviveCheck>0):
                        print("you have been revived, you have 30 health")
                        health=30
                        chaChing="process"
                        time.sleep(5)
                        break
                elif(revive=="no"):
                    noRevive()
                    print("You have been eliminated by noScope1313")
                    gameStop="DEAD"
                    break
                break
            elif (hatThree==1):
                tttTwo()
                hatFour=random.randrange(2)
                if (hatFour==0):
                    tttDeathTwo()
                    health=0
                    while (revive!="yes") and (revive!="no"):
                        revive=input("Do you want to revive yourself?")
                        if (revive=="yes"):
                            reviveCheck=int(3)
                            print("Type the following words exactly as shown")
                            for x in range(5):
                                if (reviveCheck>0):
                                    reviveWords=random.randrange(4)
                                    if (reviveWords==0):
                                        print("stairs")
                                        reviveResponse=input("")
                                        if (reviveResponse!="stairs"):
                                            reviveCheck=reviveCheck-1
                                            print("You typed it wrong")
                                            print("Revival Attempts",reviveCheck)
                                    elif (reviveWords==1):
                                        print("Roof!")
                                        reviveResponse=input("")
                                        if (reviveResponse!="Roof!"):
                                            reviveCheck=reviveCheck-1
                                            print("You typed it wrong")
                                            print("Revival Attempts",reviveCheck)
                                    elif (reviveWords==2):
                                        print("wall.")       
                                        reviveResponse=input("")
                                        if (reviveResponse!="wall."):
                                            reviveCheck=reviveCheck-1
                                            print("You typed it wrong")
                                            print("Revival Attempts",reviveCheck)
                                    elif (reviveWords==3):
                                        print("Floor")
                                        reviveResponse=input("")
                                        if (reviveResponse!="Floor"):
                                            reviveCheck=reviveCheck-1
                                            print("You typed it wrong")
                                            print("Revival Attempts",reviveCheck)
                            if (reviveCheck<1):
                                print("You died")
                                gameStop="DEAD"
                                break
                            if(reviveCheck>0):
                                print("you have been revived, you have 30 health")
                                health=30
                                time.sleep(5)
                                chaChing="process"
                                break
                        elif(revive=="no"):
                            noRevive()
                            print("You have been eliminated by noScope1313")
                            gameStop="DEAD"
                            break
                        break
                if (hatFour==1):
                    tttThree()
                    people=86
                    chest=random.randrange(4)
                    if (chest==0):
                        itemOne="Green Assault Rifle"
                        itemTwo="Blue Pump Shotgun"
                        itemThree="Big Shield x2"
                        wood=wood+60
                        pickUp="choose"
                        pickUpThree="choose"
                        pickUpFive="choose"
                        print("You got 60 wood!")
                        while (pickUp!="yes") and (pickUp!="no"):
                            pickUp=input("Would you like to pick up the Green Assault Rifle?")
                            if (pickUp=="yes"):
                                if(slotTwo!="[empty]"):
                                    print("Are you sure you want to replace", slotTwo,"with a", itemOne,"?")
                                    pickUpTwo=input("")
                                    if (pickUpTwo=="yes"):
                                        slotTwo=itemOne
                                    elif (pickUpTwo=="no"):
                                        slotTwo=slotTwo
                                        break
                                else:
                                    slotTwo=itemOne
                                    break
                            elif (pickUp=="no"):
                                if(slotTwo=="[empty]"):
                                    print("Are you sure you dont want to pick up", itemOne, "?")
                                    pickUpTwo=input("")
                                    if (pickUpTwo=="yes"):
                                        slotTwo=slotTwo
                                    elif (pickUpTwo=="no"):
                                        slotTwo=itemOne
                                        break
                                    break
                        while (pickUpThree!="yes") and (pickUpThree!="no"):
                            pickUpThree=input("Would you like to pick up the Blue Pump Shotgun?")
                            if (pickUpThree=="yes"):
                                if(slotThree!="[empty]"):
                                    print("Are you sure you want to replace", slotThree,"with a", itemTwo)
                                    pickUpFour=input("")
                                    if (pickUpFour=="yes"):
                                        slotThree=itemTwo
                                    elif(pickUpThree=="no"):
                                        slotThree=slotThree
                                        break
                                else:
                                    slotThree=itemTwo
                                    break
                            elif (pickUpThree=="no"):
                                if(slotThree=="[empty]"):
                                    print("Are you sure you don't want to pick up", itemTwo,"?")
                                    pickUpFour=input("")
                                    if (pickUpFour=="yes"):
                                        slotThree=slotThree
                                    elif (pickUpFour=="no"):
                                        slotThree=itemTwo
                                        break
                                    break
                        while (pickUpFive!="yes") and (pickUpFive!="no"):
                            pickUpFive=input("Would you like to pick up the Big Shields x2?")
                            if (pickUpFive=="yes"):
                                if(slotFour!="[empty]"):
                                    print("Are you sure you want to replace", slotFour,"with a", itemThree,"?")
                                    pickUpSix=input("")
                                    if (pickUpSix=="yes"):
                                        slotFour=itemThree
                                    elif(pickUpSix=="no"):
                                        slotFour=slotFour
                                        break
                                else:
                                    slotFour=itemThree
                                    break
                            elif (pickUpFive=="no"):
                                if(slotFour=="[empty]"):
                                    print("Are you sure you don't want to pick up", itemThree,"?")
                                    pickUpSix=input("")
                                    if (pickUpFour=="yes"):
                                        slotFour=slotFour
                                    elif (pickUpSix=="no"):
                                        slotFour=itemThree
                                        break
                                    break
                    elif (chest==1):
                        itemOne="Legendary Scar"
                        itemTwo="Heavy Shotgun"
                        itemThree="Chug Jug"
                        wood=wood+60
                        brick=brick+60
                        pickUp="choose"
                        pickUpThree="choose"
                        pickUpFive="choose"
                        print("You got +60 wood!")
                        time.sleep(timeOne)
                        print("You got +60 brick")
                        while (pickUp!="yes") and (pickUp!="no"):
                            pickUp=input("Would you like to pick up the Legendary Scar?")
                            if (pickUp=="yes"):
                                if(slotTwo!="[empty]"):
                                    print("Are you sure you want to replace", slotTwo,"with a", itemOne,"?")
                                    pickUpTwo=input("")
                                    if (pickUpTwo=="yes"):
                                        slotTwo=itemOne
                                    elif (pickUpTwo=="no"):
                                        slotTwo=slotTwo
                                        break
                                else:
                                    slotTwo=itemOne
                                    break
                            elif (pickUp=="no"):
                                if(slotTwo=="[empty]"):
                                    print("Are you sure you dont want to pick up", itemOne, "?")
                                    pickUpTwo=input("")
                                    if (pickUpTwo=="yes"):
                                        slotTwo=slotTwo
                                    elif (pickUpTwo=="no"):
                                        slotTwo=itemOne
                                        break
                                    break
                        while (pickUpThree!="yes") and (pickUpThree!="no"):
                            pickUpThree=input("Would you like to pick up the Heavy Shotgun?")
                            if (pickUpThree=="yes"):
                                if(slotThree!="[empty]"):
                                    print("Are you sure you want to replace", slotThree,"with a", itemTwo)
                                    pickUpFour=input("")
                                    if (pickUpFour=="yes"):
                                        slotThree=itemTwo
                                    elif(pickUpThree=="no"):
                                        slotThree=slotThree
                                        break
                                else:
                                    slotThree=itemTwo
                                    break
                            elif (pickUpThree=="no"):
                                if(slotThree=="[empty]"):
                                    print("Are you sure you don't want to pick up", itemTwo,"?")
                                    pickUpFour=input("")
                                    if (pickUpFour=="yes"):
                                        slotThree=slotThree
                                    elif (pickUpFour=="no"):
                                        slotThree=itemTwo
                                        break
                                    break
                        while (pickUpFive!="yes") and (pickUpFive!="no"):
                            pickUpFive=input("Would you like to pick up the Chug Jug?")
                            if (pickUpFive=="yes"):
                                if(slotFour!="[empty]"):
                                    print("Are you sure you want to replace", slotFour,"with a", itemThree,"?")
                                    pickUpSix=input("")
                                    if (pickUpSix=="yes"):
                                        slotFour=itemThree
                                    elif(pickUpSix=="no"):
                                        slotFour=slotFour
                                        break
                                else:
                                    slotFour=itemThree
                                    break
                            elif (pickUpFive=="no"):
                                if(slotFour=="[empty]"):
                                    print("Are you sure you don't want to pick up", itemThree,"?")
                                    pickUpSix=input("")
                                    if (pickUpFour=="yes"):
                                        slotFour=slotFour
                                    elif (pickUpSix=="no"):
                                        slotFour=itemThree
                                        break
                                    break
                    elif (chest==2):
                        itemOne="Grey Burst Assault Rifle"
                        itemTwo="Grey Tactical Shotgun"
                        itemThree="Bandages x5"
                        wood=wood+30
                        pickUp="choose"
                        pickUpThree="choose"
                        pickUpFive="choose"
                        print("You got +30 wood!")
                        time.sleep(timeOne)
                        while (pickUp!="yes") and (pickUp!="no"):
                            pickUp=input("Would you like to pick up the Grey Assault Rifle?")
                            if (pickUp=="yes"):
                                if(slotTwo!="[empty]"):
                                    print("Are you sure you want to replace", slotTwo,"with a", itemOne,"?")
                                    pickUpTwo=input("")
                                    if (pickUpTwo=="yes"):
                                        slotTwo=itemOne
                                    elif (pickUpTwo=="no"):
                                        slotTwo=slotTwo
                                        break
                                else:
                                    slotTwo=itemOne
                                    break
                            elif (pickUp=="no"):
                                if(slotTwo=="[empty]"):
                                    print("Are you sure you dont want to pick up", itemOne, "?")
                                    pickUpTwo=input("")
                                    if (pickUpTwo=="yes"):
                                        slotTwo=slotTwo
                                    elif (pickUpTwo=="no"):
                                        slotTwo=itemOne
                                        break
                                    break
                        while (pickUpThree!="yes") and (pickUpThree!="no"):
                            pickUpThree=input("Would you like to pick up the Grey Tactical Shotgun?")
                            if (pickUpThree=="yes"):
                                if(slotThree!="[empty]"):
                                    print("Are you sure you want to replace", slotThree,"with a", itemTwo)
                                    pickUpFour=input("")
                                    if (pickUpFour=="yes"):
                                        slotThree=itemTwo
                                    elif(pickUpThree=="no"):
                                        slotThree=slotThree
                                        break
                                else:
                                    slotThree=itemTwo
                                    break
                            elif (pickUpThree=="no"):
                                if(slotThree=="[empty]"):
                                    print("Are you sure you don't want to pick up", itemTwo,"?")
                                    pickUpFour=input("")
                                    if (pickUpFour=="yes"):
                                        slotThree=slotThree
                                    elif (pickUpFour=="no"):
                                        slotThree=itemTwo
                                        break
                                    break
                        while (pickUpFive!="yes") and (pickUpFive!="no"):
                            pickUpFive=input("Would you like to pick up bandages x5?")
                            if (pickUpFive=="yes"):
                                if(slotFive!="[empty]"):
                                    print("Are you sure you want to replace", slotFive,"with a", itemThree,"?")
                                    pickUpSix=input("")
                                    if (pickUpSix=="yes"):
                                        slotFive=itemThree
                                    elif(pickUpSix=="no"):
                                        slotFive=slotFive
                                        break
                                else:
                                    slotFive=itemThree
                                    break
                            elif (pickUpFive=="no"):
                                if(slotFive=="[empty]"):
                                    print("Are you sure you don't want to pick up", itemThree,"?")
                                    pickUpSix=input("")
                                    if (pickUpFive=="yes"):
                                        slotFive=slotFive
                                    elif (pickUpSix=="no"):
                                        slotFive=itemThree
                                        break
                                    break
                    elif (chest==3):
                        itemOne="Blue Assault Rifle"
                        itemTwo="Blue Tactical Shotgun"
                        itemThree="Medkit"
                        wood=wood+60
                        pickUp="choose"
                        pickUpThree="choose"
                        pickUpFive="choose"
                        print("You got +60 wood!")
                        time.sleep(timeOne)
                        while (pickUp!="yes") and (pickUp!="no"):
                            pickUp=input("Would you like to pick up the Blue Assault Rifle?")
                            if (pickUp=="yes"):
                                if(slotTwo!="[empty]"):
                                    print("Are you sure you want to replace", slotTwo,"with a", itemOne,"?")
                                    pickUpTwo=input("")
                                    if (pickUpTwo=="yes"):
                                        slotTwo=itemOne
                                    elif (pickUpTwo=="no"):
                                        slotTwo=slotTwo
                                        break
                                else:
                                    slotTwo=itemOne
                                    break
                            elif (pickUp=="no"):
                                if(slotTwo=="[empty]"):
                                    print("Are you sure you dont want to pick up", itemOne, "?")
                                    pickUpTwo=input("")
                                    if (pickUpTwo=="yes"):
                                        slotTwo=slotTwo
                                    elif (pickUpTwo=="no"):
                                        slotTwo=itemOne
                                        break
                                    break
                        while (pickUpThree!="yes") and (pickUpThree!="no"):
                            pickUpThree=input("Would you like to pick up the Blue Tactical Shotgun?")
                            if (pickUpThree=="yes"):
                                if(slotThree!="[empty]"):
                                    print("Are you sure you want to replace", slotThree,"with a", itemTwo)
                                    pickUpFour=input("")
                                    if (pickUpFour=="yes"):
                                        slotThree=itemTwo
                                    elif(pickUpThree=="no"):
                                        slotThree=slotThree
                                        break
                                else:
                                    slotThree=itemTwo
                                    break
                            elif (pickUpThree=="no"):
                                if(slotThree=="[empty]"):
                                    print("Are you sure you don't want to pick up", itemTwo,"?")
                                    pickUpFour=input("")
                                    if (pickUpFour=="yes"):
                                        slotThree=slotThree
                                    elif (pickUpFour=="no"):
                                        slotThree=itemTwo
                                        break
                                    break
                        while (pickUpFive!="yes") and (pickUpFive!="no"):
                            pickUpFive=input("Would you like to pick up a medkit?")
                            if (pickUpFive=="yes"):
                                if(slotFive!="[empty]"):
                                    print("Are you sure you want to replace", slotFive,"with a", itemThree,"?")
                                    pickUpSix=input("")
                                    if (pickUpSix=="yes"):
                                        slotFive=itemThree
                                    elif(pickUpSix=="no"):
                                        slotFive=slotFive
                                        break
                                else:
                                    slotFive=itemThree
                                    break
                            elif (pickUpFive=="no"):
                                if(slotFive=="[empty]"):
                                    print("Are you sure you don't want to pick up", itemThree,"?")
                                    pickUpSix=input("")
                                    if (pickUpFive=="yes"):
                                        slotFive=slotFive
                                    elif (pickUpSix=="no"):
                                        slotFive=itemThree
                                        break
                                    break
                    kills=kills+4
                    health=health-25
                    playerStats()
                    tttFour()
                    chaChing="process"
                    break
                break
            break
                           
        elif (landingBuilding=="2") or (landingBuilding=="Bell Tower"): ###########################################################
            btOne()
            chatThree=random.randrange(2)
            if (chatThree==0):
                btDeathOne()
                health=0
                while (revive!="yes") and (revive!="no"):
                    revive=input("Do you want to revive yourself?")
                    if (revive=="yes"):
                        reviveCheck=int(3)
                        print("Type the following words exactly as shown")
                        for x in range(5):
                            if (reviveCheck>0):
                                reviveWords=random.randrange(4)
                                if (reviveWords==0):
                                    print("stairs")
                                    reviveResponse=input("")
                                    if (reviveResponse!="stairs"):
                                        reviveCheck=reviveCheck-1
                                        print("You typed it wrong")
                                        print("Revival Attempts",reviveCheck)
                                elif (reviveWords==1):
                                    print("Roof!")
                                    reviveResponse=input("")
                                    if (reviveResponse!="Roof!"):
                                        reviveCheck=reviveCheck-1
                                        print("You typed it wrong")
                                        print("Revival Attempts",reviveCheck)
                                elif (reviveWords==2):
                                    print("wall.")       
                                    reviveResponse=input("")
                                    if (reviveResponse!="wall."):
                                        reviveCheck=reviveCheck-1
                                        print("You typed it wrong")
                                        print("Revival Attempts",reviveCheck)
                                elif (reviveWords==3):
                                    print("Floor")
                                    reviveResponse=input("")
                                    if (reviveResponse!="Floor"):
                                        reviveCheck=reviveCheck-1
                                        print("You typed it wrong")
                                        print("Revival Attempts",reviveCheck)
                        if (reviveCheck<1):
                            print("You died")
                            gameStop="DEAD"
                            break
                        if(reviveCheck>0):
                            print("you have been revived, you have 30 health")
                            health=30
                            chaChing="process"
                            time.sleep(5)
                            break
                    elif(revive=="no"):
                        noRevive()
                        print("You have been eliminated by noScope1313")
                        gameStop="DEAD"
                        break
                    break
                break

            elif (chatThree==1):
                btTwo()
                chatFour=random.randrange(2)
                if (chatFour==0):
                    btDeathTwo()
                    health=0
                    while (revive!="yes") and (revive!="no"):
                        revive=input("Do you want to revive yourself?")
                        if (revive=="yes"):
                            reviveCheck=int(3)
                            print("Type the following words exactly as shown")
                            for x in range(5):
                                if (reviveCheck>0):
                                    reviveWords=random.randrange(4)
                                    if (reviveWords==0):
                                        print("stairs")
                                        reviveResponse=input("")
                                        if (reviveResponse!="stairs"):
                                            reviveCheck=reviveCheck-1
                                            print("You typed it wrong")
                                            print("Revival Attempts",reviveCheck)
                                    elif (reviveWords==1):
                                        print("Roof!")
                                        reviveResponse=input("")
                                        if (reviveResponse!="Roof!"):
                                            reviveCheck=reviveCheck-1
                                            print("You typed it wrong")
                                            print("Revival Attempts",reviveCheck)
                                    elif (reviveWords==2):
                                        print("wall.")       
                                        reviveResponse=input("")
                                        if (reviveResponse!="wall."):
                                            reviveCheck=reviveCheck-1
                                            print("You typed it wrong")
                                            print("Revival Attempts",reviveCheck)
                                    elif (reviveWords==3):
                                        print("Floor")
                                        reviveResponse=input("")
                                        if (reviveResponse!="Floor"):
                                            reviveCheck=reviveCheck-1
                                            print("You typed it wrong")
                                            print("Revival Attempts",reviveCheck)
                            if (reviveCheck<1):
                                print("You died")
                                gameStop="DEAD"
                                break
                            if(reviveCheck>0):
                                print("you have been revived, you have 30 health")
                                health=30
                                chaChing="process"
                                time.sleep(5)
                                break
                        elif(revive=="no"):
                            noRevive()
                            print("You have been eliminated by Ninja")
                            gameStop="DEAD"
                            break
                        break
                    break
                elif (chatFour==1):
                    btThree()
                    chest=random.randrange(4)
                    print(" \n \n \n")
                    if (chest==0):
                        itemOne="Green Assault Rifle"
                        itemTwo="Blue Pump Shotgun"
                        itemThree="Big Shield x2"
                        wood=wood+60
                        pickUp="choose"
                        pickUpThree="choose"
                        pickUpFive="choose"
                        print("You got 60 wood!")
                        while (pickUp!="yes") and (pickUp!="no"):
                            pickUp=input("Would you like to pick up the Green Assault Rifle?")
                            if (pickUp=="yes"):
                                if(slotTwo!="[empty]"):
                                    print("Are you sure you want to replace", slotTwo,"with a", itemOne,"?")
                                    pickUpTwo=input("")
                                    if (pickUpTwo=="yes"):
                                        slotTwo=itemOne
                                    elif (pickUpTwo=="no"):
                                        slotTwo=slotTwo
                                        break
                                else:
                                    slotTwo=itemOne
                                    break
                            elif (pickUp=="no"):
                                if(slotTwo=="[empty]"):
                                    print("Are you sure you dont want to pick up", itemOne, "?")
                                    pickUpTwo=input("")
                                    if (pickUpTwo=="yes"):
                                        slotTwo=slotTwo
                                    elif (pickUpTwo=="no"):
                                        slotTwo=itemOne
                                        break
                                    break
                        while (pickUpThree!="yes") and (pickUpThree!="no"):
                            pickUpThree=input("Would you like to pick up the Blue Pump Shotgun?")
                            if (pickUpThree=="yes"):
                                if(slotThree!="[empty]"):
                                    print("Are you sure you want to replace", slotThree,"with a", itemTwo)
                                    pickUpFour=input("")
                                    if (pickUpFour=="yes"):
                                        slotThree=itemTwo
                                    elif(pickUpThree=="no"):
                                        slotThree=slotThree
                                        break
                                else:
                                    slotThree=itemTwo
                                    break
                            elif (pickUpThree=="no"):
                                if(slotThree=="[empty]"):
                                    print("Are you sure you don't want to pick up", itemTwo,"?")
                                    pickUpFour=input("")
                                    if (pickUpFour=="yes"):
                                        slotThree=slotThree
                                    elif (pickUpFour=="no"):
                                        slotThree=itemTwo
                                        break
                                    break
                        while (pickUpFive!="yes") and (pickUpFive!="no"):
                            pickUpFive=input("Would you like to pick up the Big Shields x2?")
                            if (pickUpFive=="yes"):
                                if(slotFour!="[empty]"):
                                    print("Are you sure you want to replace", slotFour,"with a", itemThree,"?")
                                    pickUpSix=input("")
                                    if (pickUpSix=="yes"):
                                        slotFour=itemThree
                                    elif(pickUpSix=="no"):
                                        slotFour=slotFour
                                        break
                                else:
                                    slotFour=itemThree
                                    break
                            elif (pickUpFive=="no"):
                                if(slotFour=="[empty]"):
                                    print("Are you sure you don't want to pick up", itemThree,"?")
                                    pickUpSix=input("")
                                    if (pickUpFour=="yes"):
                                        slotFour=slotFour
                                    elif (pickUpSix=="no"):
                                        slotFour=itemThree
                                        break
                                    break
                    elif (chest==1):
                        itemOne="Legendary Scar"
                        itemTwo="Heavy Shotgun"
                        itemThree="Chug Jug"
                        wood=wood+60
                        brick=brick+60
                        pickUp="choose"
                        pickUpThree="choose"
                        pickUpFive="choose"
                        print("You got +60 wood!")
                        time.sleep(timeOne)
                        print("You got +60 brick")
                        while (pickUp!="yes") and (pickUp!="no"):
                            pickUp=input("Would you like to pick up the Legendary Scar?")
                            if (pickUp=="yes"):
                                if(slotTwo!="[empty]"):
                                    print("Are you sure you want to replace", slotTwo,"with a", itemOne,"?")
                                    pickUpTwo=input("")
                                    if (pickUpTwo=="yes"):
                                        slotTwo=itemOne
                                    elif (pickUpTwo=="no"):
                                        slotTwo=slotTwo
                                        break
                                else:
                                    slotTwo=itemOne
                                    break
                            elif (pickUp=="no"):
                                if(slotTwo=="[empty]"):
                                    print("Are you sure you dont want to pick up", itemOne, "?")
                                    pickUpTwo=input("")
                                    if (pickUpTwo=="yes"):
                                        slotTwo=slotTwo
                                    elif (pickUpTwo=="no"):
                                        slotTwo=itemOne
                                        break
                                    break
                        while (pickUpThree!="yes") and (pickUpThree!="no"):
                            pickUpThree=input("Would you like to pick up the Heavy Shotgun?")
                            if (pickUpThree=="yes"):
                                if(slotThree!="[empty]"):
                                    print("Are you sure you want to replace", slotThree,"with a", itemTwo)
                                    pickUpFour=input("")
                                    if (pickUpFour=="yes"):
                                        slotThree=itemTwo
                                    elif(pickUpThree=="no"):
                                        slotThree=slotThree
                                        break
                                else:
                                    slotThree=itemTwo
                                    break
                            elif (pickUpThree=="no"):
                                if(slotThree=="[empty]"):
                                    print("Are you sure you don't want to pick up", itemTwo,"?")
                                    pickUpFour=input("")
                                    if (pickUpFour=="yes"):
                                        slotThree=slotThree
                                    elif (pickUpFour=="no"):
                                        slotThree=itemTwo
                                        break
                                    break
                        while (pickUpFive!="yes") and (pickUpFive!="no"):
                            pickUpFive=input("Would you like to pick up the Chug Jug?")
                            if (pickUpFive=="yes"):
                                if(slotFour!="[empty]"):
                                    print("Are you sure you want to replace", slotFour,"with a", itemThree,"?")
                                    pickUpSix=input("")
                                    if (pickUpSix=="yes"):
                                        slotFour=itemThree
                                    elif(pickUpSix=="no"):
                                        slotFour=slotFour
                                        break
                                else:
                                    slotFour=itemThree
                                    break
                            elif (pickUpFive=="no"):
                                if(slotFour=="[empty]"):
                                    print("Are you sure you don't want to pick up", itemThree,"?")
                                    pickUpSix=input("")
                                    if (pickUpFour=="yes"):
                                        slotFour=slotFour
                                    elif (pickUpSix=="no"):
                                        slotFour=itemThree
                                        break
                                    break
                    elif (chest==2):
                        itemOne="Grey Burst Assault Rifle"
                        itemTwo="Grey Tactical Shotgun"
                        itemThree="Bandages x5"
                        wood=wood+30
                        pickUp="choose"
                        pickUpThree="choose"
                        pickUpFive="choose"
                        print("You got +30 wood!")
                        time.sleep(timeOne)
                        while (pickUp!="yes") and (pickUp!="no"):
                            pickUp=input("Would you like to pick up the Grey Assault Rifle?")
                            if (pickUp=="yes"):
                                if(slotTwo!="[empty]"):
                                    print("Are you sure you want to replace", slotTwo,"with a", itemOne,"?")
                                    pickUpTwo=input("")
                                    if (pickUpTwo=="yes"):
                                        slotTwo=itemOne
                                    elif (pickUpTwo=="no"):
                                        slotTwo=slotTwo
                                        break
                                else:
                                    slotTwo=itemOne
                                    break
                            elif (pickUp=="no"):
                                if(slotTwo=="[empty]"):
                                    print("Are you sure you dont want to pick up", itemOne, "?")
                                    pickUpTwo=input("")
                                    if (pickUpTwo=="yes"):
                                        slotTwo=slotTwo
                                    elif (pickUpTwo=="no"):
                                        slotTwo=itemOne
                                        break
                                    break
                        while (pickUpThree!="yes") and (pickUpThree!="no"):
                            pickUpThree=input("Would you like to pick up the Grey Tactical Shotgun?")
                            if (pickUpThree=="yes"):
                                if(slotThree!="[empty]"):
                                    print("Are you sure you want to replace", slotThree,"with a", itemTwo)
                                    pickUpFour=input("")
                                    if (pickUpFour=="yes"):
                                        slotThree=itemTwo
                                    elif(pickUpThree=="no"):
                                        slotThree=slotThree
                                        break
                                else:
                                    slotThree=itemTwo
                                    break
                            elif (pickUpThree=="no"):
                                if(slotThree=="[empty]"):
                                    print("Are you sure you don't want to pick up", itemTwo,"?")
                                    pickUpFour=input("")
                                    if (pickUpFour=="yes"):
                                        slotThree=slotThree
                                    elif (pickUpFour=="no"):
                                        slotThree=itemTwo
                                        break
                                    break
                        while (pickUpFive!="yes") and (pickUpFive!="no"):
                            pickUpFive=input("Would you like to pick up bandages x5?")
                            if (pickUpFive=="yes"):
                                if(slotFive!="[empty]"):
                                    print("Are you sure you want to replace", slotFive,"with a", itemThree,"?")
                                    pickUpSix=input("")
                                    if (pickUpSix=="yes"):
                                        slotFive=itemThree
                                    elif(pickUpSix=="no"):
                                        slotFive=slotFive
                                        break
                                else:
                                    slotFive=itemThree
                                    break
                            elif (pickUpFive=="no"):
                                if(slotFive=="[empty]"):
                                    print("Are you sure you don't want to pick up", itemThree,"?")
                                    pickUpSix=input("")
                                    if (pickUpFive=="yes"):
                                        slotFive=slotFive
                                    elif (pickUpSix=="no"):
                                        slotFive=itemThree
                                        break
                                    break
                    elif (chest==3):
                        itemOne="Blue Assault Rifle"
                        itemTwo="Blue Tactical Shotgun"
                        itemThree="Medkit"
                        wood=wood+60
                        pickUp="choose"
                        pickUpThree="choose"
                        pickUpFive="choose"
                        print("You got +60 wood!")
                        time.sleep(timeOne)
                        while (pickUp!="yes") and (pickUp!="no"):
                            pickUp=input("Would you like to pick up the Blue Assault Rifle?")
                            if (pickUp=="yes"):
                                if(slotTwo!="[empty]"):
                                    print("Are you sure you want to replace", slotTwo,"with a", itemOne,"?")
                                    pickUpTwo=input("")
                                    if (pickUpTwo=="yes"):
                                        slotTwo=itemOne
                                    elif (pickUpTwo=="no"):
                                        slotTwo=slotTwo
                                        break
                                else:
                                    slotTwo=itemOne
                                    break
                            elif (pickUp=="no"):
                                if(slotTwo=="[empty]"):
                                    print("Are you sure you dont want to pick up", itemOne, "?")
                                    pickUpTwo=input("")
                                    if (pickUpTwo=="yes"):
                                        slotTwo=slotTwo
                                    elif (pickUpTwo=="no"):
                                        slotTwo=itemOne
                                        break
                                    break
                        while (pickUpThree!="yes") and (pickUpThree!="no"):
                            pickUpThree=input("Would you like to pick up the Blue Tactical Shotgun?")
                            if (pickUpThree=="yes"):
                                if(slotThree!="[empty]"):
                                    print("Are you sure you want to replace", slotThree,"with a", itemTwo)
                                    pickUpFour=input("")
                                    if (pickUpFour=="yes"):
                                        slotThree=itemTwo
                                    elif(pickUpThree=="no"):
                                        slotThree=slotThree
                                        break
                                else:
                                    slotThree=itemTwo
                                    break
                            elif (pickUpThree=="no"):
                                if(slotThree=="[empty]"):
                                    print("Are you sure you don't want to pick up", itemTwo,"?")
                                    pickUpFour=input("")
                                    if (pickUpFour=="yes"):
                                        slotThree=slotThree
                                    elif (pickUpFour=="no"):
                                        slotThree=itemTwo
                                        break
                                    break
                        while (pickUpFive!="yes") and (pickUpFive!="no"):
                            pickUpFive=input("Would you like to pick up a medkit?")
                            if (pickUpFive=="yes"):
                                if(slotFive!="[empty]"):
                                    print("Are you sure you want to replace", slotFive,"with a", itemThree,"?")
                                    pickUpSix=input("")
                                    if (pickUpSix=="yes"):
                                        slotFive=itemThree
                                    elif(pickUpSix=="no"):
                                        slotFive=slotFive
                                        break
                                else:
                                    slotFive=itemThree
                                    break
                            elif (pickUpFive=="no"):
                                if(slotFive=="[empty]"):
                                    print("Are you sure you don't want to pick up", itemThree,"?")
                                    pickUpSix=input("")
                                    if (pickUpFive=="yes"):
                                        slotFive=slotFive
                                    elif (pickUpSix=="no"):
                                        slotFive=itemThree
                                        break
                                    break
            
    if (chaChing=="process"):
        btFive()
        if (health<100):
            print("Do you want to eat the apples to incerase your health?")
            time.sleep(timeOne)
            while (apples!="yes") and (apples!="no"):
                apples=input("")
                if (apples=="yes"):
                    for x in range (3):
                        if (health>100):
                            health=100
                            break
                        elif(health<100):
                            print("+5 health")
                            health=health+5
                    print("Health:", health)
                                                  
                elif (apples=="no"):
                    print("You decide not to eat the apples")
                    break
                break
        elif (health==100):
            print("You already have max health so you don't need to consume the apples")
            time.sleep(timeOne)
        print("You open up PLAYER STATS to check your stats at the moment")
        people=people-17
        distanceTravelled=distanceTravelled+0.5
        playerStats()
        btSix()
        chest=random.randrange(4)
        print("\n \n \n")
        if (chest==0):
            itemOne="Green Assault Rifle"
            itemTwo="Blue Pump Shotgun"
            itemThree="Big Shield x2"
            wood=wood+60
            pickUp="choose"
            pickUpThree="choose"
            pickUpFive="choose"
            print("You got 60 wood!")
            while (pickUp!="yes") and (pickUp!="no"):
                pickUp=input("Would you like to pick up the Green Assault Rifle?")
                if (pickUp=="yes"):
                    if(slotTwo!="[empty]"):
                        print("Are you sure you want to replace", slotTwo,"with a", itemOne,"?")
                        pickUpTwo=input("")
                        if (pickUpTwo=="yes"):
                            slotTwo=itemOne
                        elif (pickUpTwo=="no"):
                            slotTwo=slotTwo
                            break
                    else:
                        slotTwo=itemOne
                        break
                elif (pickUp=="no"):
                    if(slotTwo=="[empty]"):
                        print("Are you sure you dont want to pick up", itemOne, "?")
                        pickUpTwo=input("")
                        if (pickUpTwo=="yes"):
                            slotTwo=slotTwo
                        elif (pickUpTwo=="no"):
                            slotTwo=itemOne
                            break
                        break
            while (pickUpThree!="yes") and (pickUpThree!="no"):
                pickUpThree=input("Would you like to pick up the Blue Pump Shotgun?")
                if (pickUpThree=="yes"):
                    if(slotThree!="[empty]"):
                        print("Are you sure you want to replace", slotThree,"with a", itemTwo)
                        pickUpFour=input("")
                        if (pickUpFour=="yes"):
                            slotThree=itemTwo
                        elif(pickUpThree=="no"):
                            slotThree=slotThree
                            break
                    else:
                        slotThree=itemTwo
                        break
                elif (pickUpThree=="no"):
                    if(slotThree=="[empty]"):
                        print("Are you sure you don't want to pick up", itemTwo,"?")
                        pickUpFour=input("")
                        if (pickUpFour=="yes"):
                            slotThree=slotThree
                        elif (pickUpFour=="no"):
                            slotThree=itemTwo
                            break
                        break
            while (pickUpFive!="yes") and (pickUpFive!="no"):
                pickUpFive=input("Would you like to pick up the Big Shields x2?")
                if (pickUpFive=="yes"):
                    if(slotFour!="[empty]"):
                        print("Are you sure you want to replace", slotFour,"with a", itemThree,"?")
                        pickUpSix=input("")
                        if (pickUpSix=="yes"):
                            slotFour=itemThree
                        elif(pickUpSix=="no"):
                            slotFour=slotFour
                            break
                    else:
                        slotFour=itemThree
                        break
                elif (pickUpFive=="no"):
                    if(slotFour=="[empty]"):
                        print("Are you sure you don't want to pick up", itemThree,"?")
                        pickUpSix=input("")
                        if (pickUpFour=="yes"):
                            slotFour=slotFour
                        elif (pickUpSix=="no"):
                            slotFour=itemThree
                            break
                        break
        elif (chest==1):
            itemOne="Legendary Scar"
            itemTwo="Heavy Shotgun"
            itemThree="Chug Jug"
            wood=wood+60
            brick=brick+60
            pickUp="choose"
            pickUpThree="choose"
            pickUpFive="choose"
            print("You got +60 wood!")
            time.sleep(timeOne)
            print("You got +60 brick")
            while (pickUp!="yes") and (pickUp!="no"):
                pickUp=input("Would you like to pick up the Legendary Scar?")
                if (pickUp=="yes"):
                    if(slotTwo!="[empty]"):
                        print("Are you sure you want to replace", slotTwo,"with a", itemOne,"?")
                        pickUpTwo=input("")
                        if (pickUpTwo=="yes"):
                            slotTwo=itemOne
                        elif (pickUpTwo=="no"):
                            slotTwo=slotTwo
                            break
                    else:
                        slotTwo=itemOne
                        break
                elif (pickUp=="no"):
                    if(slotTwo=="[empty]"):
                        print("Are you sure you dont want to pick up", itemOne, "?")
                        pickUpTwo=input("")
                        if (pickUpTwo=="yes"):
                            slotTwo=slotTwo
                        elif (pickUpTwo=="no"):
                            slotTwo=itemOne
                            break
                        break
            while (pickUpThree!="yes") and (pickUpThree!="no"):
                pickUpThree=input("Would you like to pick up the Heavy Shotgun?")
                if (pickUpThree=="yes"):
                    if(slotThree!="[empty]"):
                        print("Are you sure you want to replace", slotThree,"with a", itemTwo)
                        pickUpFour=input("")
                        if (pickUpFour=="yes"):
                            slotThree=itemTwo
                        elif(pickUpThree=="no"):
                            slotThree=slotThree
                            break
                    else:
                        slotThree=itemTwo
                        break
                elif (pickUpThree=="no"):
                    if(slotThree=="[empty]"):
                        print("Are you sure you don't want to pick up", itemTwo,"?")
                        pickUpFour=input("")
                        if (pickUpFour=="yes"):
                            slotThree=slotThree
                        elif (pickUpFour=="no"):
                            slotThree=itemTwo
                            break
                        break
            while (pickUpFive!="yes") and (pickUpFive!="no"):
                pickUpFive=input("Would you like to pick up the Chug Jug?")
                if (pickUpFive=="yes"):
                    if(slotFour!="[empty]"):
                        print("Are you sure you want to replace", slotFour,"with a", itemThree,"?")
                        pickUpSix=input("")
                        if (pickUpSix=="yes"):
                            slotFour=itemThree
                        elif(pickUpSix=="no"):
                            slotFour=slotFour
                            break
                    else:
                        slotFour=itemThree
                        break
                elif (pickUpFive=="no"):
                    if(slotFour=="[empty]"):
                        print("Are you sure you don't want to pick up", itemThree,"?")
                        pickUpSix=input("")
                        if (pickUpFour=="yes"):
                            slotFour=slotFour
                        elif (pickUpSix=="no"):
                            slotFour=itemThree
                            break
                        break
        elif (chest==2):
            itemOne="Grey Burst Assault Rifle"
            itemTwo="Grey Tactical Shotgun"
            itemThree="Bandages x5"
            wood=wood+30
            pickUp="choose"
            pickUpThree="choose"
            pickUpFive="choose"
            print("You got +30 wood!")
            time.sleep(timeOne)
            while (pickUp!="yes") and (pickUp!="no"):
                pickUp=input("Would you like to pick up the Grey Assault Rifle?")
                if (pickUp=="yes"):
                    if(slotTwo!="[empty]"):
                        print("Are you sure you want to replace", slotTwo,"with a", itemOne,"?")
                        pickUpTwo=input("")
                        if (pickUpTwo=="yes"):
                            slotTwo=itemOne
                        elif (pickUpTwo=="no"):
                            slotTwo=slotTwo
                            break
                    else:
                        slotTwo=itemOne
                        break
                elif (pickUp=="no"):
                    if(slotTwo=="[empty]"):
                        print("Are you sure you dont want to pick up", itemOne, "?")
                        pickUpTwo=input("")
                        if (pickUpTwo=="yes"):
                            slotTwo=slotTwo
                        elif (pickUpTwo=="no"):
                            slotTwo=itemOne
                            break
                        break
            while (pickUpThree!="yes") and (pickUpThree!="no"):
                pickUpThree=input("Would you like to pick up the Grey Tactical Shotgun?")
                if (pickUpThree=="yes"):
                    if(slotThree!="[empty]"):
                        print("Are you sure you want to replace", slotThree,"with a", itemTwo)
                        pickUpFour=input("")
                        if (pickUpFour=="yes"):
                            slotThree=itemTwo
                        elif(pickUpThree=="no"):
                            slotThree=slotThree
                            break
                    else:
                        slotThree=itemTwo
                        break
                elif (pickUpThree=="no"):
                    if(slotThree=="[empty]"):
                        print("Are you sure you don't want to pick up", itemTwo,"?")
                        pickUpFour=input("")
                        if (pickUpFour=="yes"):
                            slotThree=slotThree
                        elif (pickUpFour=="no"):
                            slotThree=itemTwo
                            break
                        break
            while (pickUpFive!="yes") and (pickUpFive!="no"):
                pickUpFive=input("Would you like to pick up bandages x5?")
                if (pickUpFive=="yes"):
                    if(slotFive!="[empty]"):
                        print("Are you sure you want to replace", slotFive,"with a", itemThree,"?")
                        pickUpSix=input("")
                        if (pickUpSix=="yes"):
                            slotFive=itemThree
                        elif(pickUpSix=="no"):
                            slotFive=slotFive
                            break
                    else:
                        slotFive=itemThree
                        break
                elif (pickUpFive=="no"):
                    if(slotFive=="[empty]"):
                        print("Are you sure you don't want to pick up", itemThree,"?")
                        pickUpSix=input("")
                        if (pickUpFive=="yes"):
                            slotFive=slotFive
                        elif (pickUpSix=="no"):
                            slotFive=itemThree
                            break
                        break
        elif (chest==3):
            itemOne="Blue Assault Rifle"
            itemTwo="Blue Tactical Shotgun"
            itemThree="Medkit"
            wood=wood+60
            pickUp="choose"
            pickUpThree="choose"
            pickUpFive="choose"
            print("You got +60 wood!")
            time.sleep(timeOne)
            while (pickUp!="yes") and (pickUp!="no"):
                pickUp=input("Would you like to pick up the Blue Assault Rifle?")
                if (pickUp=="yes"):
                    if(slotTwo!="[empty]"):
                        print("Are you sure you want to replace", slotTwo,"with a", itemOne,"?")
                        pickUpTwo=input("")
                        if (pickUpTwo=="yes"):
                            slotTwo=itemOne
                        elif (pickUpTwo=="no"):
                            slotTwo=slotTwo
                            break
                    else:
                        slotTwo=itemOne
                        break
                elif (pickUp=="no"):
                    if(slotTwo=="[empty]"):
                        print("Are you sure you dont want to pick up", itemOne, "?")
                        pickUpTwo=input("")
                        if (pickUpTwo=="yes"):
                            slotTwo=slotTwo
                        elif (pickUpTwo=="no"):
                            slotTwo=itemOne
                            break
                        break
            while (pickUpThree!="yes") and (pickUpThree!="no"):
                pickUpThree=input("Would you like to pick up the Blue Tactical Shotgun?")
                if (pickUpThree=="yes"):
                    if(slotThree!="[empty]"):
                        print("Are you sure you want to replace", slotThree,"with a", itemTwo)
                        pickUpFour=input("")
                        if (pickUpFour=="yes"):
                            slotThree=itemTwo
                        elif(pickUpThree=="no"):
                            slotThree=slotThree
                            break
                    else:
                        slotThree=itemTwo
                        break
                elif (pickUpThree=="no"):
                    if(slotThree=="[empty]"):
                        print("Are you sure you don't want to pick up", itemTwo,"?")
                        pickUpFour=input("")
                        if (pickUpFour=="yes"):
                            slotThree=slotThree
                        elif (pickUpFour=="no"):
                            slotThree=itemTwo
                            break
                        break
            while (pickUpFive!="yes") and (pickUpFive!="no"):
                pickUpFive=input("Would you like to pick up a medkit?")
                if (pickUpFive=="yes"):
                    if(slotFive!="[empty]"):
                        print("Are you sure you want to replace", slotFive,"with a", itemThree,"?")
                        pickUpSix=input("")
                        if (pickUpSix=="yes"):
                            slotFive=itemThree
                        elif(pickUpSix=="no"):
                            slotFive=slotFive
                            break
                    else:
                        slotFive=itemThree
                        break
                elif (pickUpFive=="no"):
                    if(slotFive=="[empty]"):
                        print("Are you sure you don't want to pick up", itemThree,"?")
                        pickUpSix=input("")
                        if (pickUpFive=="yes"):
                            slotFive=slotFive
                        elif (pickUpSix=="no"):
                            slotFive=itemThree
                            break
                        break

        btSeven()
        print("\n \n \n \n")
        os.system('cls')
        combatText()
        enemyHealth=100
        stageOneText()
        stageOneRules
        print("\t \t \t STAGE ONE START\n \n \n")
        time.sleep(timeOne)
        print("Your Health:", health)
        time.sleep(timeOne)
        print("\t Type the following words to build:")
        for x in range(10):
            if (health>0):
                stageOneWords=random.randrange(4)
                if (stageOneWords==0):
                    print("stairs")
                    stageOneResponse=input("")
                    if (stageOneResponse!="stairs"):
                        health=health-5
                        print("You typed it wrong")
                        print("Health:",health)
                elif (stageOneWords==1):
                    print("Roof!")
                    stageOneResponse=input("")
                    if (stageOneResponse!="Roof!"):
                        health=health-5
                        print("You typed it wrong")
                        print("Health:",health)
                elif (stageOneWords==2):
                    print("wall.")       
                    stageOneResponse=input("")
                    if (stageOneResponse!="wall."):
                        health=health-5
                        print("You typed it wrong")
                        print("Health:",health)
                elif (stageOneWords==3):
                    print("Floor")
                    stageOneResponse=input("")
                    if (stageOneResponse!="Floor"):
                        health=health-5
                        print("You typed it wrong")
                        print("Health:",health)
        if (health<1):
            print("You died")
        if(health>0):
            print("you passed stage one with", health,"heatlh")
            time.sleep(5)
        stageTwoText()
        stageTwoRules()
        print("\t \t \t STAGE TWO START\n \n \n")
        time.sleep(timeOne)
        print("Your Health:", health)
        time.sleep(timeOne)
        while (health>0):
            if (enemyHealth>0):
                print("Enemy Health:", enemyHealth,"\n \n \n")
                print("Health:", health,"\n \n \n")
                print("\t What do you want to do: 'shoot' or 'defend'")
                stageTwoAction=input("")
                enemyAction=random.randrange(10)
                if (stageTwoAction=="defend") and (enemyAction>=2) and (enemyAction<=4):
                    print("You protected yourself, the enemy's health declined")
                    enemyHealth=enemyHealth-25
                elif (stageTwoAction=="defend") and (enemyAction>=0) and (enemyAction<=1):
                    print("Your defense wasn't strong enough, the enemy broke through")
                    health=health-10
                elif (stageTwoAction=="shoot") and (enemyAction>=7) and (enemyAction<=9):
                    print("The enemy shot you!, you lost health")
                    health=health-10
                elif (stageTwoAction=="shoot") and (enemyAction<7):
                    print("You got a great shot at the enemy, their health decreased")
                    enemyHealth=enemyHealth-25
                elif (stageTwoAction=="defend") and (enemyAction>=5) and (enemyAction<=9):
                    print("Both of you defended, the attacks cancel out")
                
                elif (stageTwoAction!="shoot") and (stageTwoAction!="defend"):
                    print("You hesitated and the enemy shot you!, you lost health")
                    health=health-10
            else:
                break
        if (health>0) and (enemyHealth<1):
            print("You defeated the enemy")
            kills=kills+1
            chaChing="processTwo"
        elif (health<1) and (enemyHealth>0):
            print("You have been deafeated by Kiingg_L")
            gameStop="DEAD"


    if (chaChing=="processTwo"): #User gets to the second stage
        llOne()
        distanceTravelled=distanceTravelled+3.5
        llTwo()
        while (chestLoot!="yes") and (chestLoot!="no"):
            chestLoot=input("Do you want to check the chest?")
            if (chestLoot=="yes"):
                print("You go into the lake to see if the chest is looted")
                chestOpen=random.randrange(2)
                if (chestOpen==0):
                    print("Sadly the chest was already looted by someone else")
                elif (chestOpen==1):
                    print("Looks like the chest wasn't opened!")
                    time.sleep(timeOne)
                    print("The three items that come out are a Legendary Scar, a Launch pad, and a Chug Jug \n You also get some wood and brick")
                    itemOne="Legendary Scar"
                    itemThree="Chug Jug"
                    launchpad=launchpad+1
                    wood=wood+60
                    brick=brick+60
                    print("You got +60 wood!")
                    time.sleep(timeOne)
                    print("You got +60 brick")
                    time.sleep(timeOne)
                    print("You got +1 Launchpad")
                    pickUp="choose"
                    pickUpFive="choose"
                    while (pickUp!="yes") and (pickUp!="no"):
                        pickUp=input("Would you like to pick up the Legendary Scar?")
                        if (pickUp=="yes"):
                            if(slotTwo!="[empty]"):
                                print("Are you sure you want to replace", slotTwo,"with a", itemOne,"?")
                                pickUpTwo=input("")
                                if (pickUpTwo=="yes"):
                                    slotTwo=itemOne
                                elif (pickUpTwo=="no"):
                                    slotTwo=slotTwo
                                    break
                            else:
                                slotTwo=itemOne
                                break
                        elif (pickUp=="no"):
                            if(slotTwo=="[empty]"):
                                print("Are you sure you dont want to pick up", itemOne, "?")
                                pickUpTwo=input("")
                                if (pickUpTwo=="yes"):
                                    slotTwo=slotTwo
                                elif (pickUpTwo=="no"):
                                    slotTwo=itemOne
                                    break
                                break
                    while (pickUpFive!="yes") and (pickUpFive!="no"):
                        pickUpFive=input("Would you like to pick up the Chug Jug?")
                        if (pickUpFive=="yes"):
                            if(slotFour!="[empty]"):
                                print("Are you sure you want to replace", slotFour,"with a", itemThree,"?")
                                pickUpSix=input("")
                                if (pickUpSix=="yes"):
                                    slotFour=itemThree
                                elif(pickUpSix=="no"):
                                    slotFour=slotFour
                                    break
                            else:
                                slotFour=itemThree
                                break
                        elif (pickUpFive=="no"):
                            if(slotFour=="[empty]"):
                                print("Are you sure you don't want to pick up", itemThree,"?")
                                pickUpSix=input("")
                                if (pickUpFour=="yes"):
                                    slotFour=slotFour
                                elif (pickUpSix=="no"):
                                    slotFour=itemThree
                                    break
                                break
                            break
                        break
                    break
                break
            elif (chestLoot=="no"):
                print("You decide to not check the chest")    
        llThree()
        enemyHealth=100
        combatText()
        stageOneText()
        stageOneRules
        print("\t \t \t STAGE ONE START\n \n \n")
        time.sleep(timeOne)
        print("Your Health:", health)
        time.sleep(timeOne)
        print("\t Type the following words to build:")
        for x in range(17):
            if (health>0):
                stageOneWords=random.randrange(11)
                if (stageOneWords==0):
                    print("stairs")
                    stageOneResponse=input("")
                    if (stageOneResponse!="stairs"):
                        health=health-5
                        print("You typed it wrong")
                        print("Health:",health)
                elif (stageOneWords==1):
                    print("Roof!")
                    stageOneResponse=input("")
                    if (stageOneResponse!="Roof!"):
                        health=health-5
                        print("You typed it wrong")
                        print("Health:",health)
                elif (stageOneWords==2):
                    print("wall.")       
                    stageOneResponse=input("")
                    if (stageOneResponse!="wall."):
                        health=health-5
                        print("You typed it wrong")
                        print("Health:",health)
                elif (stageOneWords==3):
                    print("Floor")
                    stageOneResponse=input("")
                    if (stageOneResponse!="Floor"):
                        health=health-5
                        print("You typed it wrong")
                        print("Health:",health)
                elif (stageOneWords==4):
                    print("Pickaxe...")
                    stageOneResponse=input("")
                    if (stageOneResponse!="Pickaxe..."):
                        health=health-5
                        print("You typed it wrong")
                        print("Health:",health)
                elif (stageOneWords==5):
                    print("Wu Kong!!")
                    stageOneResponse=input("")
                    if (stageOneResponse!="Wu Kong!!"):
                        health=health-5
                        print("You typed it wrong")
                        print("Health:",health)
                elif (stageOneWords==6):
                    print("storm")
                    stageOneResponse=input("")
                    if (stageOneResponse!="storm"):
                        health=health-5
                        print("You typed it wrong")
                        print("Health:",health)
                elif (stageOneWords==7):
                    print("Bolt Action sniper")
                    stageOneResponse=input("")
                    if (stageOneResponse!="Bolt Action sniper"):
                        health=health-5
                        print("You typed it wrong")
                        print("Health:",health)
                elif (stageOneWords==8):
                    print("Battle Pass")
                    stageOneResponse=input("")
                    if (stageOneResponse!="Battle Pass"):
                        health=health-5
                        print("You typed it wrong")
                        print("Health:",health)
                elif (stageOneWords==9):
                    print("Lucky Landing :))")
                    stageOneResponse=input("")
                    if (stageOneResponse!="Lucky Landing :))"):
                        health=health-5
                        print("You typed it wrong")
                        print("Health:",health)
                elif (stageOneWords==10):
                    print("solo showdown")
                    stageOneResponse=input("")
                    if (stageOneResponse!="solo showdown"):
                        health=health-5
                        print("You typed it wrong")
                        print("Health:",health)
        if (health<1):
            print("You died")
        if(health>0):
            print("you passed stage one with", health,"heatlh")
            time.sleep(5)
        stageTwoText()
        stageTwoRules()
        print("\t \t \t STAGE TWO START\n \n \n")
        time.sleep(timeOne)
        print("Your Health:", health)
        time.sleep(timeOne)
        while (health>0):
            if (enemyHealth>0):
                print("Enemy Health:", enemyHealth,"\n \n \n")
                print("Health:", health,"\n \n \n")
                print("\t What do you want to do: 'shoot' or 'defend'")
                stageTwoAction=input("")
                enemyAction=random.randrange(10)
                if (stageTwoAction=="defend") and (enemyAction==3):
                    print("You protected yourself, the enemy's health declined")
                    enemyHealth=enemyHealth-25
                elif (stageTwoAction=="defend") and (enemyAction>=0) and (enemyAction<=2):
                    print("Your defense wasn't strong enough, the enemy broke through")
                    health=health-15
                elif (stageTwoAction=="shoot") and (enemyAction>=6) and (enemyAction<=9):
                    print("The enemy shot you!, you lost health")
                    health=health-15
                elif (stageTwoAction=="shoot") and (enemyAction<6):
                    print("You got a great shot at the enemy, their health decreased")
                    enemyHealth=enemyHealth-25
                elif (stageTwoAction=="defend") and (enemyAction>=4) and (enemyAction<=9):
                    print("Both of you defended, the attacks cancel out")
                elif (stageTwoAction!="shoot") and (stageTwoAction!="defend"):
                    print("You hesitated and the enemy shot you!, you lost health")
                    health=health-15
            else:
                break
        if (health>0) and (enemyHealth<1):
            print("You defeated the enemy")
            chaChing="processTwoOne"
            kills=kills+1
        elif (health<1) and (enemyHealth>0):
            print("You have been deafeated by Kiingg_L")
            gameStop="DEAD"

    if (chaChing=="processTwoOne"):
        llFour()
        if (launchpad>0):
            llLaunchpad()
            launchpad=launchpad-1
            chaChing="processThree"
        else:
            llNoLaunchpad()
            for x in range (7):
                if (health>0):
                    health=health-2
                    print("Health:", health)
                if (health<1):
                    health=0
                    print("You died")
                    while (revive!="yes") and (revive!="no"):
                        revive=input("Do you want to revive yourself?")
                        if (revive=="yes"):
                            reviveCheck=3
                            for x in range(5):
                                if (reviveCheck>0):
                                    reviveWords=random.randrange(4)
                                    if (reviveWords==0):
                                        print("stairs")
                                        reviveResponse=input("")
                                        if (reviveResponse!="stairs"):
                                            reviveCheck=reviveCheck-1
                                            print("You typed it wrong")
                                            print("Revival Attempts",reviveCheck)
                                    elif (reviveWords==1):
                                        print("Roof!")
                                        reviveResponse=input("")
                                        if (reviveResponse!="Roof!"):
                                            reviveCheck=reviveCheck-1
                                            print("You typed it wrong")
                                            print("Revival Attempts",reviveCheck)
                                    elif (reviveWords==2):
                                        print("wall.")       
                                        reviveResponse=input("")
                                        if (reviveResponse!="wall."):
                                            reviveCheck=reviveCheck-1
                                            print("You typed it wrong")
                                            print("Revival Attempts",reviveCheck)
                                    elif (reviveWords==3):
                                        print("Floor")
                                        reviveResponse=input("")
                                        if (reviveResponse!="Floor"):
                                            reviveCheck=reviveCheck-1
                                            print("You typed it wrong")
                                            print("Revival Attempts",reviveCheck)
                            if (reviveCheck<1):
                                print("You died")
                            if(reviveCheck>0):
                                print("you have been revived, you have 30 health")
                                health=30
                                reviveCheck=5
                                time.sleep(5)
                        if (revive=="no"):
                            noRevive()
                            print("You have been eliminated by the Storm")
                            gameStop="DEAD"
                            break
                        break
                else:
                    chaChing="processThree"
                      
    if (chaChing=="processThree"): # The user gets to the last stage
        dustyDivotOne()
        if (health<100):
            if (slotFour=="Chug Jug"):
                print("You use the Chug Jug to return to full health and shield")
                health=100
                shield=100
                slotFour="[empty]"
            elif (slotFive=="Medkit"):
                print("You use the medkit to return to full health")
                health=100
                slotFive="[empty]"
            elif (slotFour=="bandages x5"):
                if (health<75):
                    print("You used your bandages to bring your health to 75")
                else:
                    print("Your bandages were ineffective")
            elif (healDD=="no"):
                print("You decide not to heal")
            if(health==100):
                print("You have max health")
        playerStats()
        dustyDivotTwo()
        people=3
        playerStats()
        partTwelve()
        people=2
        partThirteen()
        print("\n \n \n \n")
        enemyHealth=100
        combatText()
        stageOneText()
        stageOneRules
        print("\t \t \t STAGE ONE START\n \n \n")
        time.sleep(timeOne)
        print("Your Health:", health)
        time.sleep(timeOne)
        print("\t Type the following words to build:")
        for x in range(35):
            if (health>0):
                stageOneWords=random.randrange(11)
                if (stageOneWords==0):
                    print("stairs")
                    stageOneResponse=input("")
                    if (stageOneResponse!="stairs"):
                        health=health-5
                        print("You typed it wrong")
                        print("Health:",health)
                elif (stageOneWords==1):
                    print("Roof!")
                    stageOneResponse=input("")
                    if (stageOneResponse!="Roof!"):
                        health=health-5
                        print("You typed it wrong")
                        print("Health:",health)
                elif (stageOneWords==2):
                    print("wall.")       
                    stageOneResponse=input("")
                    if (stageOneResponse!="wall."):
                        health=health-5
                        print("You typed it wrong")
                        print("Health:",health)
                elif (stageOneWords==3):
                    print("Floor")
                    stageOneResponse=input("")
                    if (stageOneResponse!="Floor"):
                        health=health-5
                        print("You typed it wrong")
                        print("Health:",health)
                elif (stageOneWords==4):
                    print("Pickaxe...")
                    stageOneResponse=input("")
                    if (stageOneResponse!="Pickaxe..."):
                        health=health-5
                        print("You typed it wrong")
                        print("Health:",health)
                elif (stageOneWords==5):
                    print("Wu Kong!!")
                    stageOneResponse=input("")
                    if (stageOneResponse!="Wu Kong!!"):
                        health=health-5
                        print("You typed it wrong")
                        print("Health:",health)
                elif (stageOneWords==6):
                    print("storm")
                    stageOneResponse=input("")
                    if (stageOneResponse!="storm"):
                        health=health-5
                        print("You typed it wrong")
                        print("Health:",health)
                elif (stageOneWords==7):
                    print("Bolt Action sniper")
                    stageOneResponse=input("")
                    if (stageOneResponse!="Bolt Action sniper"):
                        health=health-5
                        print("You typed it wrong")
                        print("Health:",health)
                elif (stageOneWords==8):
                    print("Battle Pass")
                    stageOneResponse=input("")
                    if (stageOneResponse!="Battle Pass"):
                        health=health-5
                        print("You typed it wrong")
                        print("Health:",health)
                elif (stageOneWords==9):
                    print("Lucky Landing :))")
                    stageOneResponse=input("")
                    if (stageOneResponse!="Lucky Landing :))"):
                        health=health-5
                        print("You typed it wrong")
                        print("Health:",health)
                elif (stageOneWords==10):
                    print("solo showdown")
                    stageOneResponse=input("")
                    if (stageOneResponse!="solo showdown"):
                        health=health-5
                        print("You typed it wrong")
                        print("Health:",health)
        if (health<1):
            print("You died")
        if(health>0):
            print("you passed stage one with", health,"heatlh")
            time.sleep(5)
        stageTwoText()
        stageTwoRules()
        print("\t \t \t STAGE TWO START\n \n \n")
        time.sleep(timeOne)
        print("Your Health:", health)
        time.sleep(timeOne)
        while (health>0):
            if (enemyHealth>0):
                print("Enemy Health:", enemyHealth,"\n \n \n")
                print("Health:", health,"\n \n \n")
                print("\t What do you want to do: 'shoot' or 'defend'")
                stageTwoAction=input("")
                enemyAction=random.randrange(10)
                if (stageTwoAction=="defend") and (enemyAction==3):
                    print("You protected yourself, the enemy's health declined")
                    enemyHealth=enemyHealth-25
                elif (stageTwoAction=="defend") and (enemyAction>=0) and (enemyAction<=2):
                    print("Your defense wasn't strong enough, the enemy broke through")
                    health=health-15
                elif (stageTwoAction=="shoot") and (enemyAction>=6) and (enemyAction<=9):
                    print("The enemy shot you!, you lost health")
                    health=health-15
                elif (stageTwoAction=="shoot") and (enemyAction<6):
                    print("You got a great shot at the enemy, their health decreased")
                    enemyHealth=enemyHealth-25
                elif (stageTwoAction=="defend") and (enemyAction>=4) and (enemyAction<=9):
                    print("Both of you defended, the attacks cancel out")
                elif (stageTwoAction!="shoot") and (stageTwoAction!="defend"):
                    print("You hesitated and the enemy shot you!, you lost health")
                    health=health-15
            else:
                break
        if (health>0) and (enemyHealth<1):
            print("You defeated the enemy")
            chaChing="processFour"
            kills=kills+1
        elif (health<1) and (enemyHealth>0):
            print("You have been deafeated by Kiingg_L")
            gameStop="DEAD"
        gamePlay="no"


    if(chaChing=="processFour"): # If the user wins it shows here
        partFourteen()
        endGameCredits()
        print("Do you want to play again? (Type play if yes)")
        gamePlayy=input("")
        if (gamePlayy=="yes"):
            gamePlay="yes"
            continue
        else:
            gamePlay="no"
        

    if (gameStop=="DEAD"): #The user loses it shows here
        print("You died")
        endGameCredits()
        print("Do you want to play again? (Type play if yes)")
        gamePlayy=input("")        
        if (gamePlayy=="yes"):
            gamePlay="yes"
            continue
        else:
            gamePlay="no"
    continue
