import random
# Computers choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Determining winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "player"
    else:
        return "computer"

def play_game():
    # Score initialization
    player_score = 0
    computer_score = 0
    ties = 0

    print("Rock, Paper, Scissors Game!")

    while True:
        # Player's choice
        player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Wrong choice. Please choose rock, paper, or scissors.")
            continue

        # Computer's choice
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        # Determining winner
        result = determine_winner(player_choice, computer_choice)

        if result == "tie":
            ties += 1
            print("It is a tie")
        elif result == "player":
            player_score += 1
            print("You won this round!")
        else:
            computer_score += 1
            print("You lost this round!")

        # Show current scores
        print(f"Scores: You {player_score} - Computer {computer_score} - Ties {ties}")

        # Player input to play again 
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            print(f"Final Scores: You {player_score} - Computer {computer_score} - Ties {ties}")
            break

# Start playing the game
if __name__ == "__main__":
    play_game()