qty = 0
tot = 0.0
while True:
  string_x = input('Enter a number: ')
  if string_x == 'done':
    break
  try:
    float_x = float(string_x)
  except:
    print('Invalid input')
    continue
  qty = qty + 1
  tot = tot + float_x

print(tot, qty, tot/qty)
