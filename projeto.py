import random 
import string

def gerar_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(comprimento))
    return senha

if __name__ == "__main__":
    comprimento_senha = int(input("Digite o comprimento da senha desejada:"))
    nova_senha = gerar_senha(comprimento_senha)
    print("Sua nova senha é:", nova_senha)
