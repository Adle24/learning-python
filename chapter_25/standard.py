from operator import itemgetter
from decimal import Decimal
import math


my_list = ["a", "b", "c", "d", "e"]
f = itemgetter(2)
print(f(my_list))

f = itemgetter(3, 2, 1)
print(f(my_list))

netsted_list = [["x", "y", "z"], ["d", "e", "f"], ["a", "b", "c"]]
sorted_list = sorted(netsted_list, key=itemgetter(1))
print(sorted_list)

print(f"pi valie: {math.pi}")
print(math.fabs(-2))
print(math.floor(233.3))
print(math.ceil(233.3))
print(math.factorial(10))
print(math.log(3))
print(math.sqrt(100))
print(math.radians(180.0))

price = Decimal(3.14)
tax = Decimal(0.2)
total = price + (price * tax)
print(total)
