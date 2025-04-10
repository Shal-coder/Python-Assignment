def multiplication_table(n,k):
    for i in range(1,k+1):
         print(f"{n} x {i} = {n * i}")
n=int(input("Enter a number:"))
k=int(input("Enter a number:"))
multiplication_table(n,k)