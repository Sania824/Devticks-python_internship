# Rock, Papers, Scissor game
import random

list_of_options = ['Rock', 'Paper', 'Scissor']

# Function that takes user input
def user_input():
    U_input = input("Choose amongst Rock, Paper & Scissor: ")
    return U_input

# Function that takes computer input, it randomly chooses from the list_of_options
def computer_input():
    C_input = random.choice(list_of_options)
    print("Computer Chooses: ", C_input)
    return C_input

# A wrapped up function of all functionality
def game():
    print("\nThe Game Begins: Human VS Computer")
    print("Remember to write with the correct spellings: Rock, Paper, Scissor\n")

    continue_playing = "y"
    while continue_playing == "y":
        input1 = user_input()
        input2 = computer_input()

        if (input1 == 'Rock') and (input2 == 'Scissor'):
            print("You won this round!")
        elif (input1 == 'Rock') and (input2 == 'Paper'): (
            print("You won this round!"))
        elif input1 == input2:
            print("Its a draw")
        elif (input1 == 'Scissor') and (input2 == 'Rock'):
            print("Computer Wins")
        elif (input1 == 'Scissor') and (input2 == 'Paper'):
            print("You won this round!")
        elif input1 == input2:
            print("Its a draw")
        elif (input1 == 'Paper') and (input2 == 'Rock'):
            print("Computer Wins")
        elif (input1 == 'Paper') and (input2 == 'Scissor'):
            print("Computer Wins")
        elif input1 == input2:
            print("Its a draw")
        else:
            print("Invalid Input")

        continue_playing = input("\nIf you want to play again Type y, if not then n: ")

        #return input1, input2

game()
