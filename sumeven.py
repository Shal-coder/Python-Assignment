def sum_even_numbers():
    total = 0
    for num in range(1, 101):
        if num % 2 == 0:
            total += num
    return total

print(f"Sum of even numbers from 1 to 100: {sum_even_numbers()}")