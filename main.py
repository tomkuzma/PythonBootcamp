from day_15 import day15
from day_16 import day16

day = int(input("Which day would you like to load? "))

match day:
    case 15:
        day15.run()
    case 16:
        day16.run()
    case _:
        print("Not an option")