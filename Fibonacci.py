def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

try:
    num_terms = int(input("Enter the number of terms for the Fibonacci series: "))
    if num_terms <= 0:
        print("Please enter a positive integer.")
    else:
        print("Fibonacci Series:")
        for i in range(num_terms):
            print(fibonacci_recursive(i), end=" ")
        print()
except ValueError:
    print("Invalid input. Please enter an integer.")
