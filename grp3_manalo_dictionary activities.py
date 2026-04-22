# ACTIVITY 1: FILL IN THE BLANK

student = {
  "name":"Ana",
  "age":20,
  "course":"IT"
}

print(student["name"]) # should print Ana

# ACTIVITY 2: ADD AND UPDATE

student = {"name": "Ana", "age": 20}

# Add "grade": 95
student["grade"] = 95

# Change age to 21
student["age"] = 21

print(student)

# ACTIVITY 3: LOOP THROUGH DICTIONARY

car = {"brand": "Toyota", "model":
  "Corolla", "year": 2020}
  
for key, value in car.items():
  print(key, ":", value)

# ACTIVITY 4: (CHANGE): MINI PHONEBOOK

# Create dictionary
phonebook = {
  "Marjorie": "09197972176",
  "Marilou": "09100082100",
  "Jonnel": "09496650814"
}

# Ask user for a name
name = input("Enter name: ")

# Print the number
print(phonebook.get(name, "Name not found"))
