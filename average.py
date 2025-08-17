def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers (list): A list of numbers (integers or floats)
    
    Returns:
        float: The average of the numbers, or 0 if the list is empty
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Example usage
if __name__ == "__main__":
    my_numbers = [10, 20, 30]
    result = calculate_average(my_numbers)
    print(f"Average of {my_numbers}: {result}")
    
    # Additional test cases
    float_numbers = [1.5, 2.5, 3.5]
    print(f"Average of {float_numbers}: {calculate_average(float_numbers)}")
    
    empty_list = []
    print(f"Average of empty list: {calculate_average(empty_list)}")
