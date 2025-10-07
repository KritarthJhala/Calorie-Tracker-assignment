# Name: Kritarth Jhala
# Date: 6 October 2025
# Calorie Tracker

# Task 1
print("\t\t\t\t Welcome to Calorie Tracker")
print()
print("This program calculates your daily calorie intake and warns when recommended amount is surpassed")
print()

n=int(input("How many meals did you have? "))

meals=[]
calories=[]

# Task 2
# Taking data from user regarding calorie intake
for i in range(n):
    ml=input('Enter meal name ')
    cal=int(input('Enter calories '))
    print()
    meals.append(ml)
    calories.append(cal)

# Task 3
# Calculating total calories and average calories per meal
total=sum(calories)
avg=total/(len(calories))

lim=int(input('Enter daily calorie limit '))
print()

# Task 4
# Comparing user provided data to the clorie intake limit and providing suitable response
if total>lim:
    print("Warning! Calorie intake exceeded recommended calorie limit")
else:
    print("Good job! Calorie intake within recommended limit")

# Task 5
# Displaying a report with the given data
print("\tSUMMARY")
print("Meal\t\tCalories")
print()

for i in range(len(meals)):
    print(meals[i],"\t\t",calories[i])

print("-----------------------")
print("Total calories:", total)
print("Average calories per meal", avg)
