#a = -2
#b = a**2+1
#print(a,b)
#c= b**3//2
#d = c%b
#print(c,d)
#if a+d !=0:
#  a+=3
#else:
#  a -=3
#  c += 1
#print(a,b,c,d)

#for i in range(3):
  #print("Hello")
#print("Goodbye")

#list = ["Mad max","Interstellar","Whiplash","Endgame","The Prestige"]
#for i in range(len(list)):
  #print(list[i])

a = int(input("Please enter a number: "))

b = a%10
c = (a%100)//10
d = int(b) + int(c)

print("Sum of last two digits is: ",d)

#New example

year =int(input("Enter a year: "))

if year % 100 == 0: #Century
  if year % 400 != 0:
    print("Not leap.")
  else:
    print("Leap")
else:
  if year % 4 == 0:
    print("Leap year.")
  else:
    print("Not leap")

#New example

list = [5, 3, 2 ,1 ,7]
a = sum(list)
print(a)

#New example

n = int(input("Please enter the number"))
f = 1 
for i in range(1,n+1):
  f *= i
print(f)

