def hailstone(n):
  if n == 1:
    return 1
  elif n%2 == 0 :
    hailstone(n/2)
  else:
    hailstone(3*n+1)
  print(n)

hailstone(5)