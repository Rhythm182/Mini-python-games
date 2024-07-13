import random  # we need random values

MAX_LINES = 3  # const
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
# want more user interaction, ask them:
# do u want to spin? Y or N
# if they put Y, then call the get_spin + printing spin functions
# if N then they won't play, game over


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines



def get_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):  # generate a column for every column we have
        # pick random values
        column = []
        current_symbols = all_symbols[:]  # copy of all_symbols
        for _ in range(rows):  # num of values we need to generate
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():  # gets the deposit from the user
    while True:  # if the deposit value is valid
        amount = input("What would you like to deposit? $")  # value is string
        if amount.isdigit():  # checks if all elements in the string are digits
            amount = int(amount)  # want numeric value
            if amount > 0:
                break
            else:
                print("Why tf r u betting on 0 bet higher.")
        else:
            print("Bruh enter a number.")
    return amount

# ask num of lines
def get_num_lines():
    while True:  # if the deposit value is valid
        lines = input("Enter the num of lines u wanna bet on: (1-" + str(MAX_LINES) + ")? ")  # value is string
        if lines.isdigit():  # check is num
            lines = int(lines)  # want numeric value
            if 1 <= lines <= MAX_LINES:  # in the actual range
                break
            else:
                print("enter num of lines in the range 1 - 3")
        else:
            print("Bruh enter a number.")
    return lines

def get_bet():
    while True:  # if the deposit value is valid
        amount = input("What would you like to bet on each line? $")  # value is string
        if amount.isdigit():  # checks if all elements in the string are digits
            amount = int(amount)  # want numeric value
            if MIN_BET <= amount <= MAX_BET:  # checking range
                break
            else:  # telling them to put in right range
                print(f'put amount between ${MIN_BET} and ${MAX_BET}')
        else:
            print("Bruh enter a number.")
    return amount

def spin(balance):  # method is wrong for when u win
    lines = get_num_lines()
    while True:  # check if total_bet is within deposit amount
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f'You do not have enough to bet that amount, your current balance is: ${balance}')
        else:
            break
    print(f'You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}')
    slots = get_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f'You won ${winnings}!')
    balance = balance + winnings
    print(f'You won on lines:', *winning_lines)
    return winnings - total_bet

def main():  # actual game code, can play repeatedly
    print("Welcome to Rhythm's virtual slot machine where u can gamble w ur virtual money!")
    print("First, here are some basic things to know: ")
    print("The maximum u can bet is $100, and there are only 3 lines you can bet on.")
    print("The value for A is $5, B is $4, C is $3, D is $2")
    print("Have fun")
    balance = deposit()
    while True:
        print(f"Current balance is: ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)  # this line

    print(f"You left with ${balance}")

main()