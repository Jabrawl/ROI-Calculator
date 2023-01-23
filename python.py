# Here we assume that we have a client coming to us asking for an automated Rental Property Calculator. Our client's name is Brandon from a company called "Bigger Pockets". Below, you will find a video of what Brandon usually does to calculate his Rental Property ROI.

# Using Visual Studio Code/Jupyter Notebook, and Object Oriented Programming create a program that will calculate the Return on Investment(ROI) for a rental property.

# This project will be completed individually, though you can feel free to share ideas with your fellow students.

# Once completed, commit the project to github and submit the link to this assignment.

# For an added challenge store each user in a dictionary and associate specific properties with that user. You can also add your calculations to the property as well.

# BUT WAIT THERES MORE!
# If you're thinking, "wow simple math? This is easy peasy lemon squeazy" Try taking a user input and matching it to the gross median rent by state. You might be able to grab it with some regex. That might make it a bit more difficult difficult lemon difficult.

# (Revenue - Cost) = cash flow (monthly basis)
# Initial investment = How much money user put down on the house and how much they invested in renovating it
# Initial Investment / (cash flow * 12)

import re
from decimal import Decimal

class Calculator:
    def __init__(self):
        self.rental_income = None
        self.expenses = None
        self.users = {}

    def check_input(self):
        amount = input("$")
        if not re.match("^\d+(\.\d{2})?$", amount):
            print("\nThat is not a valid input, please enter a number (5, 30.00, 100, 2000.00, 421.68, etc.)")
            return self.check_input()
        else:
            amount = Decimal(amount).quantize(Decimal('0.00'))
            return amount
            

    def calculate_roi(self):
        name = input("What is your name? ").title()
        if name in self.users:
            print(f"\nWelcome back {name}! Here are your previous properties:")
            for key, value in self.users[name].items():
                print(f"{key} has an ROI of {value}%")
            while True:    
                new_prop = input("\nWhat would you like us to refer to this new property as: ").title()
                if new_prop in self.users[name]:
                    print("You've already used that nickname!")
                    continue
                else:
                    self.users[name][new_prop] = 0
                    print("Alright, let's get started!\n")
                    break

        else:
            self.users[name] = {} 
            new_prop = input(f"Welcome {name}! What name would you like us to refer to your first property as: ").title()
            self.users[name][new_prop] = 0
            print("Alright, let's get started!\n")


        print("What is the monthly rental income on the property:")
        self.rental_income = self.check_input()
        self.expenses = self.calculate_expenses()
        cash_flow = self.rental_income - self.expenses
        print("\nNow we have the expenses, just need the total investment on the property!\n")
        print("What is the down payment on the property:")
        down_payment = self.check_input()
        print("What are the closing costs:")
        closing_costs = self.check_input()
        print("What is the rehab budget:")
        rehab_budget = self.check_input()
        while True:
            if_extra_fees = input("Are there any more fees for the property? Yes / No: ").lower()
            if if_extra_fees == "n" or if_extra_fees == "no":
                extra_fees = 0
                break
            elif if_extra_fees == "y" or if_extra_fees == "yes":
                print("What is the total of these extra fees:")
                extra_fees = self.check_input()
                break
            else:
                print("That is not a valid input, try again (Yes, No, Y, N)\n")
                continue
        total_investment = down_payment + closing_costs + rehab_budget + extra_fees
        roi = ((cash_flow * 12) / total_investment) * 100
        roi = Decimal(roi).quantize(Decimal('0.00'))
        print(f"""----------~~~~~~~~~~===~~~~~~~~~~----------
        
       The ROI for {next(iter(self.users[name]))} is...   {roi}% !!!!!
        
----------~~~~~~~~~~===~~~~~~~~~~----------
        """)
        self.users[name][new_prop] = roi 
        while True:
            keep_going = input("\nWould you like to keep going? Yes / No: ").lower()
            if keep_going == "n" or keep_going == "no":
                print("Thanks for using our calculator!")
                return
            elif keep_going == "y" or keep_going == "yes":
                return self.calculate_roi()
            else:
                print("That is not a valid input, try again (Yes, No, Y, N)\n")
                continue

    def calculate_expenses(self):
        print("What is the tax rate in your area (This is the percentage of your monthly rental income that the government steals):")
        tax = input("%")
        if not re.match("^(100|[0-9]?[0-9](\.[0-9]+)?)$", tax):
            print("\nThat is not a valid input, please enter a percentage  that is 0 - 100 (5, 10.1, 20.20 42.0, etc.)")
            return self.calculate_expenses()
        tax = Decimal(tax)
        tax = self.rental_income * (tax / 100)
        tax = Decimal(tax).quantize(Decimal('0.00'))
        print("What is the monthly insurance cost of your property:")
        insurance = self.check_input()
        while True:
            if_utilities = input("Does the renter pay utilities? Yes / No: ").lower()
            if if_utilities == "y" or if_utilities == "yes":
                utilities = 0
                print("Sweet, more money for us!\n")
                break
            elif if_utilities == "n" or if_utilities == "no":
                print("What is the monthly cost of the utilities:")
                utilities = self.check_input()
                break
            else:
                print("That is not a valid input, try again (Yes, No, Y, N)\n")
                continue
        print("What is your monthly mortgage payment:")
        mortgage = self.check_input()
        while True:
            if_extra_money = input("Are there any extra monthly expenses and / or would you like to set money aside? Yes / No: ").lower()
            if if_extra_money == "n" or if_extra_money == "no":
                extra_money = 0
                break
            elif if_extra_money == "y" or if_extra_money == "yes":
                print("What is the total of these extra expenses:")
                extra_expenses = self.check_input()
                print("How much money would you like to set aside:")
                set_aside = self.check_input()
                extra_money = extra_expenses + set_aside
                break
            else:
                print("That is not a valid input, try again (Yes, No, Y, N)\n")
                continue
        return tax + insurance + utilities + mortgage + extra_money
        





calc = Calculator()
calc.calculate_roi()