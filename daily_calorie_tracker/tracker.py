print("\t\t\t\t Welcome to Calorie Tracker")
print()
print("This program calculates your daily calorie intake and warns when recommended amount is surpassed")
print()

n=int(input("How many meals did you have? "))

meals=[]
calories=[]

for i in range(n):
    ml=input('Enter meal name ')
    cal=int(input('Enter calories '))
    print()
    meals.append(ml)
    calories.append(cal)
total=sum(calories)
avg=total/(len(calories))

lim=int(input('Enter daily calorie limit '))
print()

print("Meal\t\tCalories")
print()

for i in range(len(meals)):
    print(meals[i],"\t\t",calories[i])

print("-----------------------")
print("Total calories:", total)
print("Average calories per meal", avg)
print()

if total>lim:
    print("Recommended calorie limit exceeded")
else:
    print("Calorie intake within recommended limit")