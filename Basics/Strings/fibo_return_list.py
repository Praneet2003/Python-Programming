n = int(input("Enter how many Fibonacci numbers you want: "))
fibo_list = []
a, b = 0, 1
for _ in range(n):
    fibo_list.append(a)
    a, b = b, a + b  # update for next Fibonacci number
print(fibo_list)
