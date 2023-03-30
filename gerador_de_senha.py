#import random
#from senhas import senhas
import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%¨&*()'
numero_senhas = int(input("Quantas senhas você precisa: "))
tamanho_senha = []
senha = []
senha = ''
senhas = []

for contador_senhas in range(0,numero_senhas):
    tamanho_senha.append(int(input("Tamanho da senha: ")))

for contador_senha in range(0,numero_senhas):
    for tamanho in range(0,tamanho_senha[contador_senha]):
        senha += random.choice(chars)
    senhas.append(senha)
    senha = ''

for senha in senhas:
    print(senha)
