# Febonacci series

def fibonacci(n):
    fib_sequence = [0, 1]  # Initialize Fibonacci sequence with first two terms
    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]  # Calculate next term by adding last two terms
        fib_sequence.append(next_term)  # Append next term to the sequence
    return fib_sequence

# Example usage:
num_terms = int(input("Enter the number of Fibonacci terms: "))
fib_sequence = fibonacci(num_terms)
print("Fibonacci sequence up to {} terms:".format(num_terms))
print(fib_sequence)
