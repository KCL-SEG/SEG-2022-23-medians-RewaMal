"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        #sort the list
        sorted_number = sorted(numbers)
        #find the number of elements
        length = len(numbers)
        print(sorted_number)
        #check if number of elements is even or odd
        if length %2 == 0: #it is even number of elements
            median = (sorted_number[length //2 - 1] + sorted_number[length // 2 ]) /2
            print(f'{median}')   
        else: #it is odd number of elements
            median = sorted_number[length //2] 
            print(f'{median}')      
        
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
