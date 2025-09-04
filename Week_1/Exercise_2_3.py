# messy data string
data = "product_name: Laptop, price = $999, brand - Dell ; product_name: Smartphone, price: $599 , brand = Samsung ; product_name - Tablet , price=299,brand : Apple"

# expected output
[
    {'product_name': 'Laptop', 'price': '$999', 'brand': 'Dell'},
    {'product_name': 'Smartphone', 'price': '$599', 'brand': 'Samsung'},
    {'product_name': 'Tablet', 'price': '299', 'brand': 'Apple'}
]