rps = ["rock", "paper", "scissors"]

def play_rps():
    import random
    while True:
        play_game = input("Do you want to play Rock, Paper, Scissors? (y/n): ").lower()
        if play_game == 'y' or play_game == 'yes':

            cpu_choice = random.choice(rps)
            user_choice = input("Type your choice, Rock, Paper or Scissors: ").lower()
            
            if user_choice in rps:
                print(f"You chose {user_choice}. The computer chose {cpu_choice}.")
            
                if (user_choice == "rock" and cpu_choice == "scissors") or (
                        user_choice == "scissors" and cpu_choice == "paper") or (
                        user_choice == "paper" and cpu_choice == "rock") :
                            print("You win!")
            
                elif (user_choice == "rock" and cpu_choice == "paper") or (
                        user_choice == "scissors" and cpu_choice == "rock") or (
                        user_choice == "paper" and cpu_choice == "scissors") :
                            print("You lose!")
            
                else :
                            print("It's a tie!")
            
            else :
                        print("Not a valid choice, please choose Rock, Paper or Scissors.")

        elif play_game == 'n' or play_game == 'no':
            print("Okay, maybe next time!")
            break
        else :
            print("Invalid input. Please enter 'y' or 'n'.")

play_rps()        