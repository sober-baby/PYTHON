import math
# problem 3

def gcd(n, m):
  a = 0
  gcd = 0
  while a < min(n, m):
    a += 1
    if n % a == 0 and m % a == 0:
      gcd = a

  return gcd

def gcd_2(n, m):
  a = min(n, m)
  gcd = 0
  while a >= 1:
    if n % a == 0 and m % a == 0:
      return a
    a = a-1
  return 1

# problem 4

def simpify_fraction(n, m):
  if n % m == 0:
    print(int(n/m))
  else:
    gcd = gcd_2(n, m)
    print(f"{int(n/gcd)}/{int(m/gcd)}")

# problem 5

def morex(n):
  ans = 0
  x = 0
  while True:
    ans = ans + (-1)**x / (2*x + 1)
    if int(math.pi*(10**n)) == int(ans*4*(10**n)):
      return x
    x+=1

# problem 6

def next_day(y, m , d):
  if m in [1, 3, 5, 7, 8, 10, 12]:
    if m == 12 and d == 31:
      print(f"{y+1}/1/1")
      return
    if d == 31:
      print(f"{y}/{m+1}/1")
      return
    print(f"{y}/{m}/{d+1}")
    return
  if m in [4, 6, 9, 11]:
    if d == 30:
      print(f"{y}/{m+1}/1")
      return
    print(f"{y}/{m}/{d+1}")
    return
  if m == 2 and y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
    if d == 29:
      print(f"{y}/{m+1}/1")
      return
    print(f"{y}/{m}/{d+1}")
    return
  if d == 28:
    print(f"{y}/{m+1}/1")
    return
  print(f"{y}/{m}/{d+1}")
  return

def print_days(y, m, d, y2, m2, d2)
  while(y != y2 and m != m2 and d != d2):
    print(f"{y}/{m}/{d}")
    if m in [1, 3, 5, 7, 8, 10, 12]:
      if m == 12 and d == 31:
        y += 1
        m = 1
        d = 1
        continue
      if d == 31:
        m += 1
        d = 1
        continue
      d += 1
      continue
    if m in [4, 6, 9, 11]:
      if d == 30:
        m += 1
        d = 1
        continue
      d += 1
      continue
    if m == 2 and y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
      if d == 29:
        m += 1
        d = 1
        continue
      d += 1
      continue
    if d == 28:
      m += 1
      d = 1
      continue
    d += 1
    continue

def count_days(y, m, d, y2, m2, d2)
  count = 0
  while(y != y2 and m != m2 and d != d2):
    count += 1
    if m in [1, 3, 5, 7, 8, 10, 12]:
      if m == 12 and d == 31:
        y += 1
        m = 1
        d = 1
        continue
      if d == 31:
        m += 1
        d = 1
        continue
      d += 1
      continue
    if m in [4, 6, 9, 11]:
      if d == 30:
        m += 1
        d = 1
        continue
      d += 1
      continue
    if m == 2 and y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
      if d == 29:
        m += 1
        d = 1
        continue
      d += 1
      continue
    if d == 28:
      m += 1
      d = 1
      continue
    d += 1
    continue
  return count

# problem 7

def euclid(n , m):
  while max(n,m) % min(n,m):
      n, m = min(n,m), max(n,m)-int(max(n,m)/min(n,m))*min(n,m)
    return min(n,m)


if __name__ == '__main__':

# problem 1

  ans = 0
  pi = 0

  for x in range(1001):
    ans = ans + (-1)**x / (2*x + 1)

  pi = ans*4
  print(ans)
  print(pi)

# problem 2

  ans = 0
  count = 0
  pi = 0

  while count < 1687:
    ans = ans + (-1)**count / (2*count + 1)
    count += 1

  pi = ans*4
  print(ans)
  print(pi)

# problem 3

  print(gcd(26,12))
  print(gcd_2(26,12))
  simpify_fraction(25,12)
  print(morex(3))













