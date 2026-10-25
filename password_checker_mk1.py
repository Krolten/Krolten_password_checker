import string 
import sys
import getpass

password = getpass.getpass("Enter your password:")

#common password check -----------------------------------------------

with open("common.txt", "r") as f:
    common_passwords = f.read().splitlines()

if password in common_passwords:
    print("Your password is too common. Please choose a different password.")
    sys.exit()

score = 0
feedback = []

#length check ----------------------------------------------

length = len(password)
if length >= 8:
    score += 1
if length >= 10:
    score += 2
if length >= 12:
    score += 2
if length >= 14:
    score += 2



#character type check -----------------------------------------------
#digit check
if any(char.isdigit() for char in password):
    score += 2
else:
    feedback.append("digits")
#uppercase check
if any(char.isupper() for char in password):
    score += 2 
else:
    feedback.append("uppercase letters")
#lowercase check
if any(char.islower() for char in password):
    score += 2
else:
    feedback.append("lowercase letters")
#special character check
if any(char in string.punctuation for char in password):
    score += 2
else:
    feedback.append("special characters")

#feedback and scoring -----------------------------------------------
if length < 8:
    print("Your password is too short. It should be at least 8 characters long.")
else :
    if len(set(password)) <= length / 2:
        print("Your password has too many repeated characters. Try using more unique characters.")
    else:
        if score < 8:
            print("Password is too weak")
        if score >= 8 and score < 12:
            print("Your password is moderate.")
        if score >= 12:
            print("Your password is strong!")
        if length >= 8:
            if feedback:
                print("Try adding " + ", ".join(feedback) + " to make it stronger.")
