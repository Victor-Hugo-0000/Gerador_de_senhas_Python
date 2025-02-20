import random
import string

def gerar_senha(comprimento:12, maisculas:True, minusculas:True, numeros:True, simbolos:True):
    caracteres = ""
    if maisculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation
    if not caracteres:
        raise ValueError("Pelo menos um tipo de caractere deve ser selecioando.")
    
    senha = "".join(random.choice(caracteres) for _ in range(comprimento))
    return senha

while True:

    if __name__ == "__main__":
        tamanho = int(input("Digite o tamnaho da senha desejada:"))
        incluir_maisculas = input("Deseja incluir letras maisculas? (s/n)").lower() == 's'
        incluir_minusculas = input("Deseja incluir letras minusculas? (s/n)").lower() =='s'
        incluir_numeros = input("Deseja incluir numeros? (s/n)").lower() == 's'
        incluir_especiais = input("Deseja incluir caracteres especiais? (s/n)").lower() == 's'
        
        senha_gerada = gerar_senha(tamanho, incluir_maisculas, incluir_minusculas, incluir_numeros, incluir_especiais)
        print(f"senha gerada: {senha_gerada}")