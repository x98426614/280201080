gpa = float(input("Please enter your GPA: "))

if gpa >= 3:
  print("Welcome to IZTECH")
else:
  print("Work harder")

#New example

num1 = input("Please enter number 1 ")
num2 = input("Please enter number 2 ")
num3 = input("Please enter number 3 ")

if num1 > num2 and num2 > num3:
  print("Minimum of your numbers is", num3)
elif num1> num2 or num3>num1:
  print("Minimum of your numbers is", num2)
elif num1 < num2 or num2 < num3:
  print("Minimum of your numbers is", num1)
# Couldn't manage to do a min code without using min funciton

#New example

gpa = float(input("Please enter your gpa: "))
lectures = int(input("Please enter your number of lectures: "))

if gpa >= 2 and lectures >= 47:
  print("Congratulations, you are graduated")
elif gpa < 2 and lectures >= 47:
  print("You need a higher gpa")
elif gpa >= 2 and lectures < 47:
  print("You need more lectures")
else:
  print("You need a higher gpa and number of lectures") 

# New example

age = int(input("Please enter your age:"))

if age < 6 or age >60:
  print("Ticket is free") 
elif age >= 6 and age <= 18:
  print("Ticket price is 1.5")
else:
  print("Ticket price is 3")

# New example

day = int(input("Please enter the day: "))
month = int(input("Please enter the month:"))

if month >= 3 and month <= 6:
  if month == 3 and day >= 20:
    print("It's spring.")
  if month == 6 and day <= 21:
    print("It's spring")
elif month >= 6 and month <= 9:
  if month == 6 and day <= 21:
    print("It's summer")
  if month == 9 and day <= 22:
    print("It's summer")
elif month >= 9 and month <= 12:
  if month == 9 and day >= 22:
    print("It's fall")
  if month == 12 and day <=21:
    print("It's fall")
else:
  print("It's winter")
# Couldn't handled that

#New example

print("Representation of quadratic equalition is ax^2 + bx + c")
a = float(input("Please enter a: "))
b = float(input("Please enter b: "))
c = float(input("Please enter c: "))

delta = (b**2) - (4*a*c)

if delta > 0:
  print("This equalition has two real roots")
elif delta == 0:
  print("This delta has one real root")
else:
  print("This delta has two complex roots")





