#Altere a função lista para que exiba tambem a posição de cada elemento
import os
agenda = []
def pede_nome():
    return input("Nome: ")

def pede_telefone():
    return input("Telefone: ")

def mostra_dados(indice, nome, telefone):
    print(f"{indice} Nome: {nome} Telefone:{telefone}")

def pede_nome_arquivo():
    return input("Nome do arquivo")

def pesquisa(nome):
    mnome = nome.lower()
    for p , e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p 
    return None

def novo():
    global agenda
    nome = pede_nome()
    telefone = pede_telefone()
    agenda.append([nome, telefone])

def apaga():
    global agenda
    nome = pede_nome()
    p = pesquisa(nome)
    if p is not None:
        del agenda[p]
    else:
        print("Nome nao econtrado")

def altera():
    p = pesquisa(pede_nome())
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print("encontrado")
        mostra_dados(nome,telefone)
        nome = pede_nome()
        telefone = pede_telefone()
        agenda[p] = [nome , telefone]
    else:
        print('Nome nao encontrado.')

def lista():
    print("\nAgenda\n\n------")
    for indice, e in enumerate(agenda):
        mostra_dados(indice,e[0], e[1] )
    print("------")

def le():
    global agenda
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, "r", encoding="utf=8") as arquivo:
        agenda = []
        for l in arquivo.readlines():
            nome, telefone = l.strip().split("#")
            agenda.append([nome,telefone])

def grava():
    nome_aquivo = pede_nome_arquivo()
    with open (nome_aquivo, "a", encoding="utf=8") as aquivo:
        for e in agenda:
            aquivo.write(f"{e[0]}#{e[1]}\n")

def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <=fim:
                return valor
        except ValueError:
            print(f"Valor invalido,favor digitar entre {inicio} e {fim}")

def menu():
    print("""
          1- Novo
          2 - Altera
          3 - Apaga
          4 - Lista
          5 - Grava
          6 - Lê
          7 - ver tamnho do arquivo 
          
          0 - Sai
          """)
    return valida_faixa_inteiro("Escolha um opção:", 0 , 7)

def tamanho():
    arquivo = pede_nome_arquivo()
    if os.path.exists(arquivo):
        tamanho = os.path.getsize(arquivo)
        
        return print(f"O tamanho do arquivo e {tamanho} bytes")
    else:
        return print("Nome invalido")

while True:
    opcao = menu()
    if opcao == 0:
        break
    if opcao == 1:
        novo()
    if opcao == 2:
        altera()
    if opcao == 3:
        apaga()
    if opcao == 4:
        lista()
    if opcao == 5:
        grava()
    if opcao == 6:
        le()
    if opcao == 7:
        tamanho()
        