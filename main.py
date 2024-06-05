import random

MAX_BET = 100
MIN_BET = 1

COLS = 3
ROWS = 3

fruit_count = {
    "A": 4,
    "B": 6,
    "C": 8,
    "D": 10
}

fruit_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_bet(columns, bet, values):
    winnings = 0
    fruit = columns[0][1]
    for column in columns:
        fruit_to_check = column[1]
        if fruit != fruit_to_check:
            break
    else:
        winnings += values[fruit] * bet
        
    return winnings

def get_slot_spin(rows, cols, symbols):
    all_fruit = []
    for fruit, fruit_count in symbols.items():
        for _ in range(fruit_count):
            all_fruit.append(fruit)
    
    columns = []
    for _ in range(cols):
        column = []
        current_fruit = all_fruit[:]
        for _ in range(rows):
            value = random.choice(current_fruit)
            current_fruit.remove(value)
            column.append(value)
        columns.append(column)      
    
    return columns  

def draw_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a number greater than 0.")
        else:
            print("Please enter a number.")
    return amount   
            
def get_bet():
    while True:
        bet = input(f"How much would you like to bet (${MIN_BET} - ${MAX_BET})? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print("Please enter a valid bet.")
        else:
            print("Please enter a number.")
    return bet  

def spin(balance):
    while True:
        bet_amount = get_bet()
        if bet_amount > balance:
            print(f"You are trying to bet with more than you have! Your balance is: ${balance}")
        else:
            break
    slots = get_slot_spin(ROWS, COLS, fruit_count)
    
    while True:
        slots = get_slot_spin(ROWS, COLS, fruit_count)
        draw_slot_machine(slots)
        winnings = check_bet(slots, bet_amount, fruit_value)
        print(f"You won ${winnings}!")
        return winnings - bet_amount

def main():
    balance = deposit()
    while True:
        print(f"Your current balance is ${balance}")
        if balance < 1:
            print("You need to top up in order to bet again.")
            balance = deposit()
        play = input("Press enter to spin, or q to quit. ")
        if play.lower() == "q":
            break
        balance += spin(balance)
    print(f"You escaped the casino with ${balance}")
        
    
    
    
if __name__ == "__main__":
    main()
        