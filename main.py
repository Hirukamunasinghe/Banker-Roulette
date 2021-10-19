# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num_items = len(names)
import random
random_choice = random.randint(0, num_items - 1)
person_who_will_pay_the_bill = names[random_choice]
print(f"Person who will pay the bill is {person_who_will_pay_the_bill}")



