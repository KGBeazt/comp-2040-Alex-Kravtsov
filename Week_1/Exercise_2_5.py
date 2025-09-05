# messy data string
data = "device_id: 001, temp: 72, humidity: 45 | device_id: 002, temp: N/A, humidity: 50 | device_id: 003, temp: 68, humidity: N/A"

# expected output
[
    {'device_id': '001', 'temp': 72, 'humidity': 45},
    {'device_id': '002', 'temp': None, 'humidity': 50},
    {'device_id': '003', 'temp': 68, 'humidity': None}
]