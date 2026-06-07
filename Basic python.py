character_name = "Petyr Baelish"
character_age = 35

is_smart = False 
if is_smart == False:
    first_answer = "No"
else:
    first_answer = "Yes"

info = f"His name is {character_name} and he is {character_age} years old."

print(info + "\nWelcome new user!")

print(f"Is he smart? {first_answer}")
print(len(character_name))
print(character_name.index("Baelish"))
print(character_name[12])