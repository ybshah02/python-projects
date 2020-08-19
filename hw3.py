# PART A:

#==============================================
# Purpose: The following function prints out the string "Who needs loops?" 5 times
# Input Parameter(s): None
# Return value(s): None
#==============================================

def print_p1():
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")

#==============================================
# Purpose: The following function calls function print_p1 6 times, which
# prints 30 lines of "Who needs loops?"
# Input Parameter(s): None
# Return value(s): None
#==============================================

def print_p2():
    print_p1()
    print_p1()
    print_p1()
    print_p1()
    print_p1()
    print_p1()

#==============================================
# Purpose: The following function calls print_p2 4 times, which prints 120 lines
# of "Who needs Loops?" and then prints one more line of the "Who needs loops?" to attain
# 121 lines of "Who needs loops?"
# Input Parameter(s): None
# Return value(s): None
#==============================================

def print_121():
    print_p2()
    print_p2()
    print_p2()
    print_p2()
    print("Who needs loops?")

# PART B:

#==============================================
# Purpose: The folloing function defines a text adventure game that takes in 4
# string values to develop a prompt and 3 choices for a player to manually choose
# Input Parameter(s):
# text - the text of the prompt
# optionA - text of option choice A
# optionB - text of option choice B
# optionC - text of option choice C
# Return value(s): The chosen option by a player
#==============================================

def choice(text, optionA, optionB, optionC):
    print(text + "\n A. " + optionA + "\n B. " + optionB + "\n C. " + optionC)
    option_chosen = input("Choose A, B, or C: ")
    if option_chosen == "A":
        return 'A'
    elif option_chosen == "B":
        return 'B'
    elif option_chosen == "C":
        return 'C'
    else:
        print("Invalid Option, defaulting to A")
        return 'A'

# PART C:

#==============================================
# Purpose: The folloing function defines an adventure with Rick and Morty, to which the player explores the universe.
# The player goes through sequences of prompts in which they decide their fate based off 3 choices, and based on those choices
# they move on to the next sequence, make it home safe, or die.
# Input Parameter(s): None
# Return value(s): True if the player makes it home safe, False if the player dies
#==============================================

def adventure():
    state = 1
    print("Welcome to the life of Rick and Morty. Today we will experience one of Rick and Morty's adventure through the Universe!")
    path1 = choice("\nTo begin, pick a portal", "Portal A", "Portal B", "Portal C")
    if path1 == 'A':
        print("This one appears to be safe. Rick says you're on the planet, Cronenberg.")
        state = 2
    elif path1 == 'B':
        print("Oh shoot. Rick misprogrammed the portal gun to the wrong destination; you just landed into a pit of lava and died. Oops. ")
        return False
    elif path1 == 'C':
        print("This one appears to be safe. Rick says you're on the cob planet, in which everything around you is mutated with a corn on the cob. ")
        state = 3

    if state == 2:
        print("\nNevermind, this is not so safe. Cronenbergs are savages and they begin to chase after you. ")
        path2 = choice("\nChoose a portal to escape", "Portal A", "Portal B", "Portal C")
        if path2 == 'A':
            print("Phew. You all made it home safe.")
            return True
        elif path2 == 'B':
            print("You make it home safe.. at least that's what you think. ")
            state = 4
        elif path2 == 'C':
            print("Phew. This one appears to be safe. Rick says you're on the cob planet, in which everything around you is mutated with a corn on the cob.")
            state = 3

    if state == 3:
        print("\nAs you're exploring the planet, you begin to get creeped out and want to go home.")
        path3 = choice("\nChoose a portal to escape", "Portal A", "Portal B", "Portal C")
        if path3 == 'A':
            print("Oh shoot. Rick misprogrammed the portal gun to the wrong destination; you just landed into a pit of lava and died. Oops. ")
            return False
        elif path3 == 'B':
            print("You make it home safe.. at least that's what you think. ")
            state = 4
        elif path3 == 'C':
            print("Phew. You all made it home safe.")
            return True

    if state == 4:
        print("\nJust as you think that you are safe, you begin to realize this is not your Earth. You then realize that this world is one of the infinite versions of Earth in which the entire world is under Nazi rule.")
        path4 = choice("\nOne of the Nazi's catches you lurking around and pulls out their ray gun. Choose a portal to escape", "Portal A", "Portal B", "Portal C")
        if path4 == 'A':
            print("Phew. You all made it home safe.")
            return True
        elif path4 == 'B':
            print("Phew. You all made it home safe.")
            return True
        elif path4 == 'C':
            print("Oh shoot. Rick misprogrammed the portal gun to the wrong destination; you just landed into a pit of lava and died. Oops.")
            return False
