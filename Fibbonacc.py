def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

n=int(input("Enter the value of n to find the fibonacci value:"))
value=fibonacci(n)