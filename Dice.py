import random

def roll_dice():
    """Rolls a six-sided dice and returns the result."""
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Roller!")
    while True:
        input("Press Enter to roll the dice (or 'q' to quit): ")
        roll_result = roll_dice()
        print(f"You rolled: {roll_result}\n")
        quit_input = input("Would you like to quit? (y/n): ")
        if quit_input.lower() == 'y':
            break

    print("Thank you for playing!")

if __name__ == '__main__':
    main()
