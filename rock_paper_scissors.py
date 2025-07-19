import random

def get_user_choice():
    print("\nChoose one:")
    print(" - Rock")
    print(" - Paper")
    print(" - Scissors")
    choice = input("Enter your choice: ").strip().lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("❌ Invalid input. Please choose rock, paper, or scissors.")
        choice = input("Enter your choice: ").strip().lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    print(f"\n🧑 You chose: {user.capitalize()}")
    print(f"💻 Computer chose: {computer.capitalize()}")

    if user == computer:
        print("🤝 It's a tie!")
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        print("✅ You win this round!")
        return "user"
    else:
        print("❌ Computer wins this round!")
        return "computer"

def play_game():
    print("🎮 Welcome to Rock, Paper, Scissors!")
    print("🔁 You can play as many rounds as you like.")
    
    user_score = 0
    computer_score = 0
    round_number = 1

    while True:
        print(f"\n----- Round {round_number} -----")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        winner = determine_winner(user_choice, computer_choice)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"\n📊 Current Score - You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("\n👋 Thanks for playing!")
            print(f"🏁 Final Score - You: {user_score} | Computer: {computer_score}")
            if user_score > computer_score:
                print("🎉 Congratulations! You won the game!")
            elif user_score < computer_score:
                print("😢 You lost the game. Better luck next time!")
            else:
                print("🤝 It's a tie overall!")
            break
        round_number += 1

play_game()
