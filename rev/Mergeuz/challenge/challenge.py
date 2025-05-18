# Kollll w Wakkkellll
import random

def final(win: list, money: int) -> None: 
    if ''.join(win) == "merguez" and money == 40:
        print("\n🎉 Bou3rada says: 'Thank you so much for helping me today!'" )
        print("Even if I broke some plates... at least I got my pizza! 🍕😅")
        print("See you next time for a new adventure!\n")
        print("Spark{Fake_Flag}\n")
    else:
        print("Yedi bou3rada yheb lmergeuzzz!\n")

def ma3oun(win: list, money: int) -> int:
    print("\nBou3rada takes a dishwashing job to earn some money...")
    print("He starts washing... but suddenly *CRASH!* 💥")
    print("Bou3rada broke some plates")
    print("The manager is furious and makes him PAY 15 dinars for the damage!")
    money -= 5

    print("\nNow that the dishwashing situation is over, Bou3rada has two choices:")
    print("1. Go pay for the pizza 🍕")
    print("2. Check other things 🧐")
    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        win[5] = 'e'
        money += 25
        final(win, money)
    elif choice == '2':
        win[5] = 'e'
        money += 20
        restaurant(win, money)
    else:
        print("Invalid choice. Try again later.")
    return money


def distributor(win: list, money: int) -> int:
    money -= 5  # taxi cost
    print("\nBou3rada inserts the card")
    print("What should he do?")
    print("1. Withdraw all")
    print("2. Withdraw 25 dt")
    choice = input("Enter your choice (1-2): ")
    if choice == '1':
        win[4] = 'u'
        money += 30
        restaurant(win, money)
    elif choice == '2':
        win[4] = 'u'
        money += 25
        restaurant(win, money)
    else:
        print("Invalid choice. Please restart the game and choose between 1-2.")
    return money


def restaurant(win: list, money: int) -> int:
    money -= 5  # taxi cost
    print("\nBou3rada enters the restaurant...")
    if money >= 0 :
        win[2] = 'r'
        print("pizza price is 40")
        print("But, Bou3rada still doesn't have enough money to buy it.")
        print("What should he do?")
        print("1. Look for a distributor.")
        print("2. Yaghsel ma3oun.")
        print("3. Khales ye moudir.")
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            win[3] = 'g'
            return_value = distributor(win, money)
            return return_value
        elif choice == '2':
            win[3] = 'g'
            return ma3oun(win, money)
        elif choice == '3':
            win[6] = 'z'
            final(win, money)
            return money
        else:
            print("Invalid choice. Please restart the game and choose between 1-3.")
    else : 
        print("Bara rawah.")
    return money


def home(win: list, money: int) -> int:
    print("\nBou3rada: I forgot where I put the pocket, let's search where I left it...")
    print("Where should Bou3rada search?")
    print("1. On the couch")
    print("2. In the kitchen")
    print("3. In his bedroom")
    print("4. In his jeans from yesterday")
    choice = input("Enter your choice (1-4): ")
    if choice in ['1', '2', '3']:
        messages = {
            '1': "Bou3rada searched the couch... just found some crumbs.",
            '2': "Bou3rada looked in the kitchen... nope, just leftover pizza.",
            '3': "Bou3rada checked the bedroom... still nothing."
        }
        print(f"\n{messages[choice]}")
    elif choice == '4':
        win[1] = 'e'
        money += 20
        print("\nBou3rada checked his old jeans... YES! The money is there!")
        return restaurant(win, money)
    else:
        print("Invalid place. Bou3rada gave up for now...")
    return money


def challenge():
    random.seed()
    win = list("#######")
    money = 0
    win[0]='m'
    print("=== Welcome to the Pizza Maze Challenge ===")
    print("Objective: Help Bou3rada navigate the maze to eat the pizza!\n")

    print("First problem: Bou3rada checks his pockets and realizes he forgot his money!")
    print("1. Go back home to get the money.")
    print("2. Look for a distributor.")
    print("3. Go to restaurant without money.")
    choice = input("Enter your choice (1-3): ")
    if choice == '1':
        money = home(win, money)
    elif choice == '2':
        money = distributor(win, money)
    elif choice == '3':
        money = restaurant(win, money)
    else:
        print("Invalid choice. Please restart the game and choose between 1-3.")
        return

    # Continue based on restaurant return for ATM or dishwashing
    if money == 1 or money == 2:
        # handle returned signals; but restaurant returns money now
        pass

if __name__ == "__main__":
    challenge()
