def list_operations():
    numbers = [2, 4, 6, 8, 19]
    print(f"Original list: {numbers}")
    numbers.append(10)
    print(f"After adding 10: {numbers}")
    numbers.remove(6)
    print(f"After removing 6: {numbers}")
    print(f"Maximum value: {max(numbers)}")
    print(f"Minimum value: {min(numbers)}")

list_operations()