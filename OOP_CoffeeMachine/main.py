from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

"""
Coffee Machine - Object Oriented Programming Version

Pretend we are using packages and ain't allowed to touch other file apart from the main
Use the PDF as your guide

1. Print reports
2. Check resources sufficient
3. Process coins sufficient
4. Check Transaction successful
5. Make Coffee
"""

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

is_on = True
menu = Menu()

drink_total = 0

# Increment the count for the specific drink
# In the PDF, "name" is used to access the name of the drink object
drink_name = {drink.name: 0 for drink in menu.menu}

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()
  
    if choice == "off":
        is_on = False
      
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
        print(f"Number of drink sold: {drink_total}")
      
    elif choice == "sales":
        print(drink_name)

    #modified the coffee maker to have the refill option
    elif choice == "refill":
        coffee_maker.refill_resources()
        print("Resources have been refilled.")
    else:
        drink = menu.find_drink(choice)
        if drink and coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink) 
                drink_total += 1
                drink_name[drink.name] += 1 # Increment the count for the specific drink

"""
Challenge
Add a feature to the coffee machine program that tracks how many drinks have been sold.

Requirements:
Track Sales: Each time a drink is successfully made, increment a counter that tracks the number of drinks sold.

Sales Report: Add an option to the menu input (sales) that prints out the total number of each type of drink sold.

Class Modification: You might need to add new attributes and methods to your classes to track and report the sales.
"""