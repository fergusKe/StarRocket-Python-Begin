# def add(*ns):
#   sum = 0
#   for x in ns:
#       sum += x
#   print(sum)

# def test(msg = 'hello world'):
#   print(msg)

def mul_99():
  for x in range(1, 10):
    print('=== {} ==='.format(x))
    for y in range(1, 10):
      print('{} x {} = {}'.format(x, y, x*y))

def add(n1, n2):
  sum = n1 + n2
  print(sum)
  return sum

def sub(n1, n2):
  sum = n1 - n2
  print(sum)
  return sum

def mul(n1, n2):
  sum = n1 + n2
  print(sum)
  return sum

def divi(n1, n2):
  sum = n1 / n2
  print(sum)
  return sum
