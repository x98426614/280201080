for i in range(1, 11,2):
  print(i**2)


#New example

x = 2

while x <20:
  print(x)
  x = x**2

#New example

n = int(input("Please enter an integer: "))

for a in range(1,11):
  print(n, "x",a, "=", n*1 )


#New example

a = int(input("how many numbers:"))
even = 0
numbers = 0
while a >0 :
  a -= 1
  numbers += 1
  c= int(input("Your number:"))
  if a ==0:
    break

  if c %2 == 0:
    even +=1
print((even/numbers)*100)


#New example

