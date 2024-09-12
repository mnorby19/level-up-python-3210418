import math

def get_prime_factors(num):
  returnPrimes = []
  devisor = 2
  workingNum = num

  while devisor <= workingNum:
    if workingNum % devisor == 0:
      returnPrimes.append(devisor)
      workingNum = workingNum // devisor
    else:
      devisor += 1
  return(returnPrimes)

print(get_prime_factors(1300))