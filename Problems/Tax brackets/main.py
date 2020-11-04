import math

income = int(input())
tax = 0


def calc(incomes, taxi):
    calculated = round(incomes * (taxi / 100))
    print(f"The tax for {incomes} is {taxi}%. That is {calculated} dollars!")


if income in range(0, 15528):
    tax = 0
    calc(income, tax)
elif income in range(15528, 42708):
    tax = 15
    calc(income, tax)
elif income in range(42708, 132407):
    tax = 25
    calc(income, tax)
else:
    tax = 28
    calc(income, tax)
    math.s
