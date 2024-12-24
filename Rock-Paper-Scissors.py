import random
def get_computer_choice():
    """Randomly choose between Rock, Paper, Scissors."""
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)
def determine_winner(player, computer):
    """Determine the winner based on the player's and computer's choices."""
    if player == computer:
        return "It's a tie!"
    elif (player == "Rock" and computer == "Scissors") or (player == "Scissors" and computer == "Paper") or (player == "Paper" and computer == "Rock"):
        return "You Win!"
    else:
        return "Computer Wins!"
def main():
    print("Welcome to Rock-Paper-Scissors Game!")
    print("Type 'Rock', 'Paper', or 'Scissors' to play. Type 'Quit' to exit.")
    while True:
        player_choice = input("\nYour choice: ").capitalize()
        if player_choice == "Quit":
            print("Thanks for playing! Goodbye!")
            break
        elif player_choice not in ["Rock", "Paper", "Scissors"]:
            print("Invalid choice. Please try again.")
            continue
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(player_choice, computer_choice)
        print(result)
# Directly calling the main function to run the program
main()
