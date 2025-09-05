import re

# messy data string
data = "employee_name: Sarah, department: HR, roles: recruiter, trainer | employee_name: Mike , department: Engineering , roles: developer, team lead | employee_name: Alice , department: HR , roles: recruiter"

# Step 1: Split the string into individual employees based on the "|" delimiter
employee_strings = data.split('|')

# Step 2: Iterate through each employee's string data and extract key-value pairs
employees_list = []
for employee_data in employee_strings:
    employee_dict = {}
    pairs = re.findall(r'(\w+)\s*:\s*([^|]+?)(?=\s*\w+\s*:|$)', employee_data)

    # Step 3 Split the `roles` value into a list of roles.
    for key, value in pairs:
        clean_key = key.strip().lower()
        clean_value = value.strip()
        
        # Step 4 Organize the data into a dictionary where `roles` is a list for each employee
        if clean_key == 'roles':
            employee_dict[clean_key] = [role.strip() for role in clean_value.split(',')]
        else:
            employee_dict[clean_key] = clean_value
    
    # Step 5 Store the dictionaries for each employee in a list
    employees_list.append(employee_dict)

# Step 6 Display output
for item in employees_list:
    print(item)