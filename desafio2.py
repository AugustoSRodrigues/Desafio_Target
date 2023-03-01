def isFibonnaci(n):
    ant1=0
    ant2=1

    if n==0:
         return True
    while True:
        fibo = ant1+ant2
        if fibo == n:
            return True
        elif fibo > n:
            return  False
        ant1 = ant2
        ant2 = fibo

def main():
        n = int(input("Digite um número:"))
        if isFibonnaci(n):
            print(f'O número {n} pertence a sequência de Fibonacci')
        else:
             print(f'O número {n} não pertence a sequência de Fibonacci')

if __name__ == '__main__':
     main()