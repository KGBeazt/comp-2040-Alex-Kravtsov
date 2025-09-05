# messy data string
import re

data = "product_name: Laptop, price = $999, brand - Dell ; product_name: Smartphone, price: $599 , brand = Samsung ; product_name - Tablet , price=299,brand : Apple"

# Step 1: Split the string into individual products based on the semicolon (`;`)
product_strings = data.split(';')

# Step 2 For each product, use multiple separators (like `:`, `=`, and `-`) to extract key-value pairs.
dict_list = []
for product_string in product_strings:
    product_dict = {}
    pairs = re.findall(r'(\w+)\s*[:=-]\s*([^,;]+)', product_string)

   # Step 3 Clean up spaces and ensure keys are lowercase. 
    for key, value in pairs:
        product_dict[key.strip().lower()] = value.strip()
    
    # Step 4: Store each product's data in a dictionary, and put all dictionaries in a list.
    dict_list.append(product_dict)

# Step 5 Display output
for item in dict_list:
    print(item)
