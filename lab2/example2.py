# int -> 3, 5, 123
# float -> 3.0, 5.1, 123.582
# string -> "Hakan", 'Deniz', '32', "41"
# boolean -> True or False 

# + addition - substraction * multiplication / float division // integer division ** exponentiation % remainder
year = int(input("When did you born:"))
print("So you are",2020 - year, "years old")

# New example

animals = 10
roosters = 6
chickens = animals - roosters
print(chickens)

# New example

a = int(input("What is the tempeture in celcius? "))
b = a*1.8 + 32
print("So tempeture is",b,"in fahrenheit")

#New example

a = int(input("Please enter a side: "))
b = int(input("Please enter a side: "))
c = (a**2 + b**2)**0.5
print("So hypotenuse is", c)