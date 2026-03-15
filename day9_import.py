# Example 1: Importing a module
import math

# Now you can use functions from the 'math' module
print(math.sqrt(25)) #Output: 5.0


# Example 2: Importing specific items from a module
from random import randint
# Now you can use the 'radint' function directly
random_number = randint(1,10)
print(random_number)

# Example 3: Importing with an alias
import datetime as dt
# Now you can use 'dt' as an alias for the 'datetime' module
current_time = dt.datetime.now()
print(current_time)