def fibonacci_sequence(n):
    """
    Generate a Fibonacci sequence of length n.
    
    Args:
        n (int): The number of Fibonacci numbers to generate
        
    Returns:
        list: A list containing the first n Fibonacci numbers
    """
    if n < 0:
        raise ValueError("Sequence length must be non-negative")
    
    result = []
    a = 0
    b = 1
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

def calculate_fibonacci_stats(sequence_length):
    """
    Calculate statistics for a Fibonacci sequence.
    
    Args:
        sequence_length (int): The length of the Fibonacci sequence to analyze
        
    Returns:
        dict: A dictionary containing sequence statistics
    """
    sequence = fibonacci_sequence(sequence_length)
    stats = {
        'sequence': sequence,        # Fixed: Added comma
        'average': sum(sequence) / len(sequence),    # Fixed: Added comma
        'maximum': max(sequence),    # Fixed: Added comma
        'minimum': min(sequence),    # Fixed: Added comma
        'length': len(sequence)      # Fixed: Changed length() to len()
    }
    return stats    # Fixed: Changed stat to stats

# Example usage
if __name__ == "__main__":
    try:
        result = calculate_fibonacci_stats(10)
        print("Fibonacci Statistics:")
        print(f"Sequence: {result['sequence']}")
        print(f"Average: {result['average']}")
        print(f"Maximum: {result['maximum']}")
        print(f"Minimum: {result['minimum']}")
        print(f"Length: {result['length']}")
    except Exception as e:
        print(f"An error occurred: {e}")
