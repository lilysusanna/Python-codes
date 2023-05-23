# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
choose = random.randint(0, len(names)-1)
buy= names[choose]
print(f"{buy} is going to buy the meal today!")