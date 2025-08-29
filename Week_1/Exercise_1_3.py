# Exercise 1.3
# Function:
def Disc_Cal(p, d):
    price = p 
    discount = d 
    final_price = price - (price * discount)
    print(f"The discounted price of your item is: ${final_price}\n")

# Execution
Disc_Cal(100, 0.10)
Disc_Cal(250, 0.15)
Disc_Cal(50, 0.05)