def fibonacci_sequence(n):
    if n <= 0:
        return "Enter a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fibbonacci_series = [0, 1]
    for i in range(2, n):
        next_term = fibbonacci_series[-1] + fibbonacci_series[-2]
        fibbonacci_series.append(next_term)
    
    return fibbonacci_series 

n= int(input('enter a positive number:  '))
print(fibonacci_sequence(n))