def square(n):
  return n*n

print(square(2))

print(square(square(square(2)))) # It's not same

#New example 

def add(x, y, z):
  return x + y + z

def multiply(x, y):
  return x*y

def f(a,b):
  return add(multiply(multiply(a,a),a), multiply(a,b), b)

print(f(3,2))

#New example

import random

def roll_die():
  return random.randint(1,6)

def roll_die_until_lucky_value(lucky_value):
  value = roll_die()
  if value == lucky_value:
    print("Found!")
  else:
    print(value)
    return roll_die_until_lucky_value(lucky_value)
  
roll_die_until_lucky_value(5)
