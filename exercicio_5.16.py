 #execute o Programa 5.1 para os seguintes valores: 501,745,384,2, e 1.
valor = int(input("digite o valor a paga"))
cedulas = 0
atual = 50
apagar = valor 
while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1 
    else:
        print(f'{cedulas} cedulas(s) de R${atual}')
        if apagar == 0:
            break
        if atual == 50:
            atual =20
        elif atual ==20:
            atual =10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0                    
