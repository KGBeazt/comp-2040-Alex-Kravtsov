# Exercise 2.2
# Input string with inconsistent spacing
data = "Name: Alice, Age: 30, City: Los Angeles | Name: Bob, Age: 25, City: Chicago | Name: Charlie , Age: 35, City: New York"

# Step 1 Split the data for each person based on the pipe (|)
split_data = data.split('|')

# Step 2 For each person, split their attributes (e.g., name, age, city) based on commas
dict_list = []
for person_string in split_data:
    person_dict = {}
    attributes = person_string.strip().split(',')

    # Step 3 Clean up extra spaces and organize the data into a dictionary
    for attribute in attributes:
        key, value = attribute.split(':')
        person_dict[key.strip()] = value.strip()

    # Step 4 Store all individual dictionaries in a list
    dict_list.append(person_dict)

# Step 5 Display output
for item in dict_list:
    print(item)