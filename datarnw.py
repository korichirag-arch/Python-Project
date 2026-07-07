print("-----------------------------------------------------------")
print("✨✨✨ WELCOME TO THE FUNDAMENTAL BOOSTER PROGRAM ✨✨✨")
print("Let's collect and analyze some of your personal data!")
print("-----------------------------------------------------------")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters:"))
fav_number = int(input("Enter your favorite number: "))

print("-----------------------------------------------------------")
print(" Thanks For Given your Information!\n Here is the summary of your data. ")
print("-----------------------------------------------------------")

print(f"Name: {name}(type: {type(name)}, Memory Address: {id(name)})")
print(f"Age: {age}(Type: {type(age)}, Memory Address: {id(age)})")
print(f"Height: {height} meters(Type: {type(height)}, Memory Address: {id(height)})")
print(f"Favorite Number: {fav_number}(Type: {type(fav_number)}, Memory Address: {id(fav_number)})\n")

current_year = 2026
birth_year = current_year - age
print(f"You were born in the year: {birth_year} (Based on your age of {age})\n")

print("-----------------------------------------------------------")
print("Thank you for participating in the Fundamental Booster Program!")
print("We hope you enjoyed the experience and learned something new about yourself 😊.")
print("-----------------------------------------------------------  \n")
