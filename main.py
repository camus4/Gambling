import sys
import time
import random

def for_loop():
    end_oracle = random.randint(0, 10)
    for i in range(end_oracle):
        time.sleep(0.35)
        print(i)

def first_round():

    def ask_nextRound():
        print(f"your balance: {balance}")
        bet_2 = int(input("new bet: "))

        for_loop()
        if bet_2 < end_oracle:
            print(f"won! your balance: {balance * bet_2}")

        if bet_2 >= end_oracle:
            new_balance = balance - bet_2
            print(f"lost! your balance: {new_balance}")
            print(f"NEW BALANCE: {balance - bet_2}")

    balance = int(input("balance: "))
    bet = int(input("bet: "))

    end_oracle = random.randint(0, 10)
    for i in range(end_oracle):
        time.sleep(0.35)
        print(i)

    if bet < end_oracle:
        print(f"won! balance: {balance * bet}")
        balance = balance * bet
        ask = input("do you want to play the next round? y for yes and n for no: ")
        if ask.lower() == "y":
            print("Next round...")
            ask_nextRound()

    elif bet >= 0:
        print(f"lost! balance: {balance - bet}")
        balance = balance - bet
        if balance <= 0:
            print("goodbye! ")
            sys.exit()

first_round()

