import random
import string
import sys

def gerar_senha(comprimento, incluir_maisculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_simbolos=True):
    caracteres = ""

    if incluir_maisculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation
    
    if not caracteres:
        raise ValueError("Pelo menos um tipo de caractere deve ser selecioando.")

    senha = "".join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def main():
    
    print("Gerador de Senhas".center(58, "-"))
    print("\nDigite 'sair' a qualquer momento para cancelar a operação.")
    print("Digite 'reset' a qualquer momento para reniciar a operação.\n")
    print("".center(58, "-"))

    comprimento = input("\nDigite o comprimento da senha desejada: ")

    if comprimento.lower() == 'sair':
        print("Operação cancelada. Saindo...")
        sys.exit()
    
    if comprimento.lower() == 'reset':
        print("Operação reniciando...")
        return main()

    comprimento = int(comprimento)

    incluir_maisculas = input("Deseja incluir letras maisculas? (s/n)").lower()

    if incluir_maisculas == 'sair':
        print("Operação cancelada.sindo...")
        sys.exit()

    if incluir_maisculas == 'reset':
        print("Operação reniciando...")
        return main()

    incluir_minusculas = input("Deseja incluir letras minusculas? (s/n)").lower()

    if incluir_minusculas == 'sair':
        print("Operação cancelada. Saindo...")
        sys.exit()

    if incluir_minusculas == 'reset':
        print("Operação reiniciando...")
        return main()

    incluir_numeros = input("Deseja incluir numeros? (s/n)").lower()

    if incluir_numeros == 'sair':
        print("Operação Cancelada. Saindo...")
        sys.exit()

    if incluir_numeros == 'reset':
        print("Operação reniciando...")
        return main()

    incluir_especiais = input("Deseja incluir caracteres especiais? (s/n)").lower()

    if incluir_especiais == 'sair':
        print("Operação Cancelada. Saindo...")
        sys.exit()

    if incluir_especiais == 'reset':
        print("Operação reniciando...")
        return main()

    incluir_maisculas = incluir_maisculas == 's'

    incluir_minusculas = incluir_minusculas == 's'

    incluir_numeros = incluir_numeros == 's'

    incluir_especiais = incluir_especiais == 's'

    senha_gerada = gerar_senha(comprimento, incluir_maisculas, incluir_minusculas, incluir_numeros, incluir_especiais)
    print(f"senha gerada: {senha_gerada}")

while True:
    if __name__ == "__main__":
        main()