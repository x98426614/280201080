def harmonic_recursive(n):
    if n == 1:
        return 1
    else:
        return harmonic_recursive(n-1) + 1/n

def harmonic_iterative(n):
    total = 0
    for i in range(1,n+1):
        total += 1/i
    return total

a = 5

print(harmonic_iterative(a))
print(harmonic_recursive(a))

#New example

def get_reversed(n):
  if len(n) == 1:
    return n
  else:
    return [n[-1]] + get_reversed(n[0:-1])

print(get_reversed([1,2,3,4,5,6,7,8,9,10]))

#New example

def get_evens(n):
  if len(n) == 0:
    return 0
  else:
    if n[0] % 2 == 0:
      return get_evens(n[1::])
    else:
      del n[0]
      return get_evens(n[1::])
  return len(n)

print(get_evens([0,1,2,3,4,5]))
# This somehow doesn't work as it meants to ?

#New example

import time

def simple_timer(t):
  if t == 0:
    print("Time has ended!")
  else:
    time.sleep(1)  # It's big brain time
    print(t-1)
    return simple_timer(t-1)

simple_timer(5)


