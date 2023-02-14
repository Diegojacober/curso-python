n = s = count = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999: break
    count += 1
    s += n
print(f'A soma vale {s}, e numeros foram somados {count}')
