#Python Slot Machine
import random

def spin_row():
    symbols = ['🍒', '🍉', '🍇', '🔔', '⭐']

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):

    print("-------------")
    print(" | ".join(row))
    print("-------------\n")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 5
        elif row[0] == '🍇':
            return bet * 7
        elif row[0] == '🔔':
            return bet * 15
        elif row[0] == '⭐':
            return bet * 25

    else:
        return 0


def main():
    balance = 100

    print("*************************")
    print("Welcome to Python Slots ")
    print("Symbols:🍒 🍉 🍇 🔔 ⭐")
    print("*************************\n")

    while balance > 0:
        print(f"Current balance: ${balance}\n")


        bet = input("How much you want to bet: ")
        print("*************************\n")

        if not bet.isdigit():
            print("*************************")
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("*************************")
            print("You can't bet more than you have")
            continue

        if bet <= 0:
            print("*************************")
            print("Bet must be greater than 0")
            continue

        balance -= bet
        row = spin_row()
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won ${payout}\n")
            balance += payout
        else:
            print("You lost! Good luck next time\n")

        play_again = input("Would you like to play again? (y/n): \n").lower()
        if play_again != 'y':
            print("****************************************")
            print(f"  Game over! Your final balance is ${balance}")
            print("****************************************")
            break

if __name__ == "__main__":
    main()