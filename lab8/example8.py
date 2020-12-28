def square_of_numbers(lists):
  count = 0
  for num in lists:
    count += num
  value = count ** 2
  return value
a_list = [12, -7, 5, -89.4, 3, 27, 56, 57.3]
print(square_of_numbers(a_list))

#New example


def is_prime(n):
  if n < 2 :
    return False
  elif n == 2 :
    return True
  else:
    for i in range(2,n):
      if n%i == 0:
        return False
    return True

for num in range(2,101):
  if is_prime(num):
    print(num)