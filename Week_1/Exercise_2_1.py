# Exercise 2.1
# Input string
data = " Name: John Doe ; Age : 25;  CITY: New York ; Occupation: Software Engineer "

# Step 1: Remove leading/trailing spaces from the entire string
clean_data = data.strip()

# Step 2: Split the string into key-value pairs based on semicolons (`;`)
split_data = clean_data.split(';')

# Step 3: Split each pair into key and value based on the colon (`:`)
data_dic = {}
for pair in split_data:
    key, value = pair.split(':')
    data_dic[key] = value

# Step 4: Strip extra spaces around the keys and values
clean_dic = {key.strip(): value.strip() for key, value in data_dic.items()}

# Step 5: Ensure all keys are lowercase for consistency
final_dic = {key.lower(): value for key, value in clean_dic.items()}

# Step 6: Display results
for key, value in final_dic.items():
    print(f"{key}: {value}")