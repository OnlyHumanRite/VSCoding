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
    # Test cases
    test_numbers = [10, 20, 30, 40, 50]
    result = calculate_average(test_numbers)
    print(f"The average of {test_numbers} is: {result}")
    
    # Test with empty list
    empty_list = []
    result = calculate_average(empty_list)
    print(f"The average of an empty list is: {result}")
    
    # Test with decimal numbers
    decimal_numbers = [1.5, 2.5, 3.5, 4.5]
    result = calculate_average(decimal_numbers)
    print(f"The average of {decimal_numbers} is: {result}")
