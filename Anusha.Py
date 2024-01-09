for i in range(1, 11):
    if i == 1:
    
        current_number = i
        previous_number = 0
    else:
        current_number = i
        previous_number = i - 1
    
    
    sum_of_numbers = current_number + previous_number
    print(f"Sum of {current_number} and {previous_number} is: {sum_of_numbers}")