# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_l = name1.lower()
name2_l = name2.lower()
first_no = 0
second_no = 0

for i in "true":
  first_no += name1.count(i)
  first_no += name2.count(i)
for i in "love":
  second_no += name1.count(i)
  second_no += name2.count(i)
  
final = int(str(first_no) + str(second_no))
if final <10 or final > 90:
  print(f"your score is {final}, you go together like coke and mentos.")
elif final > 40 and final < 50:
  print(f"Your score is {final}, you are alright together.")
else:
  print(f"your score is {final}.")
