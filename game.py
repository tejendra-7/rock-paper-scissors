import random

li_1 = ['rock','paper','scissors'] 
# list of choices

while True:
    player = input("Enter rock , paper or scissors :").lower()
    #taking input from the user
    if player not in li_1:
            print("Please enter a valid input")
            continue
    computer = random.choice(li_1)
    #randomizing the computer value using choice in the random module to select different values from li_1 each time
    print("The choice of the computer is : ",computer)    
    
    # writing the logic for who wins
    
    if player == computer:
        print("It is a tie")
    elif player == "rock" and computer == "scissors" or \
        player == "paper" and computer == "rock" or \
        player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("Computer wins!")
    
    play_again = input("Do you want to play again? (Y/N)").lower()
    if play_again !="y":
        break

print("Thanks for playing")








