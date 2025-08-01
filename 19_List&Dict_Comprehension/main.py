# list = [1, 2, 3, 4, 5]
# new_list = [ item * 2 for item in list]

# name = "Metin"
# letters = [letter for letter in name]
#
# numbersInRange = [number for number in range(10)]
#
# myTuple = (1, 2, 3, 4, 5)
# listFromTuple = [number for number in myTuple]
# listFromTupleMoreThan3 = [number for number in myTuple if number > 3]

# names = ["Metin", "Kate", "Dafne", "Snezhana", "Nuriye"]
# ages = [42, 38, 7, 70, 72]
# agesDict = {name:age for name, age in zip(names, ages)}
# young_ones = {name:age for name, age in agesDict.items() if age < 40}

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# list = [word for word in sentence.split()]
# result = {key:len(key) for key in list}


import pandas
student_dict = {
    "student": ["Anna", "James", "Lily"],
    "score": [56, 76, 98]
}


student_data = pandas.DataFrame(student_dict)

# for (key, value) in student_data.items():
#     print(
#         f"The key is {key} and the value is {value}"
#     )

# Loop through the rows
for (index, row) in student_data.iterrows():
    print(row.student, row.score)
