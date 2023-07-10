#Request user to input their name using input() command 
#Request user to input their age using input() command
#Request user to input their house number using input() command 
#Request user to input their street name using input() command
#Print out the inputs in a sentence using the f-string and including the responses

name = input("Enter your name:")
age = int(input("Enter your age:"))
house_num = int(input("Enter your house number:"))
street_name = input("Enter your street name:")
print(f"This is {name}. He/She is {age} and lives at house number {house_num} at {street_name}")
