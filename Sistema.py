from Validacoes import validar_valor_imovel
from Validacoes import validar_salario
from Validacoes import validar_prazo_anos
from Validacoes import validar_nome_comprador
from Validacoes import validar_idade_comprador
from colorama import init, Fore
init()

def menu_inicial():
    print("===BEM-VINDO ao SISTEMA Imobiliário Python=== 🏦\n")
    print("Por favor, insira os dados abaixo para simular seu empréstimo:")
    print("1. Valor do imóvel")
    print("2. Salário mensal")
    print("3. Prazo do empréstimo em anos\n")
while True:
    menu_inicial()

    nomecomprador = validar_nome_comprador()
    idadecomprador = validar_idade_comprador()
    valor_imovel = validar_valor_imovel()
    salario_mensal = validar_salario()
    prazo_anos = validar_prazo_anos()

    prestacao = valor_imovel / (prazo_anos * 12)
    prestacao_maxima = 0.30 * salario_mensal

    if prestacao <= prestacao_maxima:
        print(f"\n \033[1;32mEmpréstimo APROVADO!✅\033[0m")
    else:
        print(f"\n \033[91mEmpréstimo NEGADO! ❌ excede 30% do seu salário \033[0m")
        print(f"O valor máximo da prestação para seu salário seria R$ {prestacao_maxima:,.2f}")
        continue

    
    print(f"{Fore.GREEN}Prestação mensal: R$ {prestacao:,.2f}")
    print(f"{Fore.LIGHTMAGENTA_EX}Prazo do empréstimo: {prazo_anos} anos")
    print(f"{Fore.YELLOW}Obrigado por utilizar nosso sistema 🏦\n")

    continuar = input(f"{Fore.WHITE}Deseja simular outro empréstimo? (S/N): ").strip().upper()
    if continuar == "S":
        continue
    else:
        print("\nEncerrando o sistema...🏦❤️")
        exit()