def hailstone(n):
  n = int(n)
  print(n)
  if n == 1:
    return 1
  elif n%2 == 0 :
    hailstone(n/2)
  else:
    hailstone(3*n+1)
  

hailstone(5)

#New example

def sum_of_list(n):
  sum = 0
  if len(n) == 0:
    return sum
  else:
    return sum + n[0] + sum_of_list(n[1::])

print(sum_of_list([1,2,3]))

#New example == pascal triangle == imposible

