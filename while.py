a = 90
c = 0
while c < a:
    c += 10
    print(c)

print("fim")

a = 3
#um programa com lup infinito que pega os numeros e soma todos mostra a qua tidade de numeros e a soma entre eles
soma = cont = 0
while True:
    vu = int(input('( digite 999 para parar) digite um numero: '))
    if vu == 999:
        break
    cont += 1
    soma += vu
print(f'a Soma dos numeros é {soma},  voce digitu {cont} de numeros!')


