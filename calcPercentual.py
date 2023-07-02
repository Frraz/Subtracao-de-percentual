print("-="*10,"Bem Vindo", "-="*10)
try:
    num1 = int(input("Digite um número para começarmos: "))
except:
    print('Ops, você digitou algo errado, por favor digite um numero inteiro: ')
    num1 = int(input("Número inteiro: "))
continua = 's'
while(continua == "s"):
    print("Agora digite o percentual que deseja subtrair desse número, ex: 50 = 50%")
    try:
        sub = float(input("Percentual: "))
        resultado = (sub/100) * num1
        print(f'\033[32mResultado: {num1 - resultado:.2f}\033[m')
        num1 = num1 - resultado
    except:
        print("Parece que você digitou algo errado :(\nPor favor digite um número inteiro para se referir ao percentual que deseja subtrair.")
        print("Tente novamente.")
    continua = str(input('Deseja continuar?[s/n]\n'))
    continue
print('Até breve')