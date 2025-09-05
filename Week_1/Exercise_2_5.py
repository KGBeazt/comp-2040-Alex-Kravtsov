import re

# messy data string
data = "device_id: 001, temp: 72, humidity: 45 | device_id: 002, temp: N/A, humidity: 50 | device_id: 003, temp: 68, humidity: N/A"

# Step 1 Split the string by device using the pipe (|)
device_strings = data.split('|')

devices_list = []

# Step 2 For each device, extract key-value pairs like device_id, temp, and humidity
for device_data in device_strings:
    device_dict = {}
    pairs = re.findall(r'(\w+)\s*:\s*([^,]+)', device_data)

    for key, value in pairs:
        clean_key = key.strip().lower()
        clean_value = value.strip()

        # Step 3 Replace any occurrences of N/A with None
        if clean_value == 'N/A':
            device_dict[clean_key] = None
        else:
            device_dict[clean_key] = clean_value

    # Step 4 Store all device dictionaries in a list
    devices_list.append(device_dict)

# Step 5 Display output
for item in devices_list:
    print(item)
