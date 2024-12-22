def fibonacci(n):
    """Return the first n Fibonacci numbers as a list."""
    # Starting values for the first two terms of Fibonacci series
    a, b = 0, 1
    sequence = []

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b  # Move to the next pair

    return sequence

# Example usage:
num_terms = 10000  # how many Fibonacci numbers you want
fib_sequence = fibonacci(num_terms)
print(f"First {num_terms} Fibonacci numbers: {fib_sequence}")
