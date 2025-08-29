# Exercise 1.2
# List of lists:
numbers1 = [10, 15, 22, 29, 30]
numbers2 = [1, 4, 7, 9, 12]
numbers3 = [100, 150, 200]


#Function:
def Odd_Or_Even(list): # Checking a list of numbers if they're odd or evens
    numbers = list 
    for num in numbers:
        if num % 2 == 0:
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")
    print("")

# Execution 
Odd_Or_Even(numbers1)
Odd_Or_Even(numbers2)
Odd_Or_Even(numbers3)