#Cores da tabela ANSI nesse módulo

import emoji
panda = emoji.emojize(":panda:")
print("\n \033[1;95mSite de cores ANSI = https://raccoon.ninja/pt/post/dev/tabela-de-cores-ansi-python\033[;0m", panda, "\n")

def validar_nome_comprador():
    nomecomprador = input("Digite o nome do comprador: ").strip().lower()
    while not nomecomprador.replace(" ", "").isalpha():
        print("\033[1;31mERRO!! Digite novamente o nome do comprador (apenas letras)\033[;0m")
        nomecomprador = (input("Digite o nome do comprador: ")).strip().lower()


def validar_idade_comprador():
    idadecomprador = (input("Digite a idade do comprador: "))
    while not idadecomprador.isdigit():
        print("\033[1;31mERRO!! Digite a idade do comprador (apenas números)\033[;0m")
        idadecomprador = (input("Digite a idade do comprador: "))
    idadecomprador = int(idadecomprador)
    print(f"Idade do usuário: {idadecomprador}")
    while idadecomprador < 18 or idadecomprador <=0:
            print("\033[1;31mUsuário inválido (menor de idade). Impossível simular\033[;0m")
            print("Reinicialize o programa...")
            exit()

def validar_valor_imovel():
    while True:
        valor = input("Valor do imóvel: R$ ").strip()
        try:
            valor = valor.replace(".", "").replace(",", ".")
            valor = float(valor)
            if valor > 0:
                return valor
            else:
                print("\033[1;31mO valor deve ser maior que zero.\033[;0m")
        except ValueError:
            print("\033[1;31mEntrada inválida. Digite um número.\033[;0m")

def validar_salario():
    while True:
        salario = input("Salário mensal: R$ ").strip()
        try:
            salario = salario.replace(".", "").replace(",", ".")
            salario = float(salario)
            if salario > 0:
                return salario
            else:
                print("\033[1;31mO salário deve ser maior que zero.\033[;0m")
        except ValueError:
            print("\033[1;31mEntrada inválida. Digite um número.\033[;0m")

def validar_prazo_anos():
    while True:
        prazo = input("Prazo em anos: ").strip()
        try:
            prazo_int = int(prazo)
            if prazo_int > 0:
                return prazo_int
            else:
                print("\033[1;31mO prazo deve ser maior que zero.\033[;0m")
        except ValueError:
            print("\033[1;31mEntrada inválida. Digite um número inteiro.\033[;0m")