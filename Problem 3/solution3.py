import time

def checkPrime(num):
  if num > 1:
    # check for factors
    for i in range(2,num):
        if (num % i) == 0:
            return num//i
            break
    else:
        return num
  else:
    print(num,"is not a prime numbers")
    return None

def solution(num):
  while num != None:
    factor = checkPrime(num)
    if(factor != None):
      return checkPrime(factor)
      break

def start(n):
  starttime = time.time()

  initialValue = checkPrime(n)
  largestPrime = solution(initialValue)
  print(largestPrime, "- is largest prime Factor")

  endtime = time.time()
  print(endtime - starttime)

start(25)