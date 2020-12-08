#Write your code below this row 👇

for i in range(1,101):
  if  i % 5 == 0 and i % 3 == 0:
    print("Fizzbuzz")
  elif i % 5 == 0:
    print("Buzz")
  elif i % 3 == 0:
    print("fizz")
  else:
    print(i)