"""
import another_module
print(another_module.another_variable)

# https://docs.python.org/3/library/turtle.html
# import turtle
# timmy = turtle.Turtle()
# from turtle import Turtle, Screen

from turtle import *

# we create an object.Class
timmy = Turtle()
print(timmy)

# here, we can see how we call method using object.method
timmy.shape("turtle")
timmy.color("Blue")
timmy.forward(100)


my_screen = Screen()
# tap into the attribute using object.attributes
print(my_screen.canvheight)
my_screen.exitonclick()

"""

"""
pypi.org

Find, install and publish Python package index
which is a bunch of software created and published by the Python community

let's have a look at ASCII table formatting library example
https://pypi.org/project/prettytable/

first, we'll need to install the package

    1. PyCharm Preferences (click on our project interpreter and then search for the package and install.
"""


# To see the implementation, right click -> Go to -> Implementation

from prettytable import PrettyTable

# Create a new object "table" from the pretty table
table = PrettyTable()
print(table)


# tap into the method.
table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])
table.align = "l"
print(table)


















