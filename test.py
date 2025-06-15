# Jamal's Programming Readiness Test

score = 0

print("Welcome to your programming readiness test!")
print("Answer carefully. Type exactly what's asked.\n")

# Question 1
answer1 = input("1) What is the output of print(2 ** 3)? ")
if answer1.strip() == "8":
    score += 1

# Question 2
answer2 = input("2) What type of value is '42' (with quotes)? ")
if "str" in answer2.lower():
    score += 1

# Question 3
answer3 = input("3) Complete: if x == 10: print('Ten'). What does this do? ")
if "prints" in answer3.lower() and "Ten" in answer3:
    score += 1

# Question 4
answer4 = input("4) What keyword defines a function in Python? ")
if answer4.strip().lower() == "def":
    score += 1

# Question 5
answer5 = input("5) What does '==' mean in Python? ")
if "equal" in answer5.lower():
    score += 1

print(f"\nYour score: {score}/5")
if score == 5:
    print(" You're ready to level up!")
elif score >= 3:
    print(" You're on the right track.")
else:
    print(" A bit more practice and you'll get there!")
