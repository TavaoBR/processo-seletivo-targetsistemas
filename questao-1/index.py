def fibonacci_sequencia(limit):
 fib_sequence = [0, 1]
 while fib_sequence[-1] < limit:
    next_value = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_value)
 
 return fib_sequence

def is_in_fibonacci_sequence(number, fib_sequence):
    return number in fib_sequence

num = int(input("Informe um número: "))

fib_sequence = fibonacci_sequencia(num)

if is_in_fibonacci_sequence(num, fib_sequence):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} Não pertence à sequência de Fibonacci")    