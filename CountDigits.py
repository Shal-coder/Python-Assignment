def count_digit(number):
    num_str = str(abs(number))
    num_str = num_str.replace(".", "")
    return len(num_str)

num =int(input("enter a number:"))
result=count_digit(num)
print(result)