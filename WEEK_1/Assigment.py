# password strenght checker
# Exercise: “Password Strength Checker” 🔐

# You are creating a basic program to check if a user’s password is strong enough.

# Requirements:
# 	1.	Ask the user to enter a password (store it in a variable).
# 	2.	Use if statements to check:
# 	•	If the password is less than 6 characters long, print:
# "Weak: Too short."
# 	•	If the password is 6 to 9 characters long, print:
# "Medium: Could be stronger."
# 	•	If the password is 10 or more characters long, print:
# "Strong password!"
# 	3.	Extra Challenge:
# 	•	If the password contains the word "password" (case-insensitive), print a warning: "Avoid using common words!"
# 	•	If the password contains a number and is at least 8 characters long, print: "Good job! Your password has variety."
# variables

password = input ("Enter password")

print(len(password))

if len(password) < 6:
  print ("Weak : too short")

elif len(password) > 6 and len(password) < 9:
  print ("Medium: Could be stronger")

else :
  print ("Strong password")


if "password" in password.lower() :
  print("warning: avoid using common words")
  print(password.lower())

import re 

match = re.search(r"\d", password)
print(match)

if len(password) >= 8 and match:
  print("Good Job")
  






# if password < 6 
# print("Weak: too short")



