import random
def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors: ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You choose {player}, computer choose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors you win!"
    else:
        return "Paper covers rock you lose!"

    elif player == "paper"
    if computer == "rock":
         return "Paper covers rock! You win!"
    else:
        return "Scissors cut paper. You lose."

    elif player == "scissors"
    if computer == "paper":
      return "Scissors paper! You win!"
     else:
        return "Rock smashes scissors. You lose."

    choices = get_choices()

