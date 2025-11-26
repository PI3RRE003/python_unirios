#ARQUIVOS - OS - WAR
#LISTA E DICT
#VALIDAÇÃO

import datetime
import os

ENTRADAS = "entradas.txt"
SAIDAS = "saidas.txt"

def write_entradas():
    if not os.path.exists(ENTRADAS):
        with open(ENTRADAS,'w'):
            ...

def append_entradas(nome,data,tipo):
    with open(ENTRADAS,'a') as arquivo:
        entrada = f'{nome};{data};{tipo}\n'
        arquivo.write(entrada)

def read_entradas():
    with open(ENTRADAS,'r') as arquivo:
        entradas = arquivo.readlines()

        if len(entradas) == 0:
            print("Lista de entradas vazias")
        else:
            for entrada in entradas:
                dados = entrada.strip().split(";")
                ponto = {
                    "NOME" : dados[0],
                    "DATA" : dados[1],
                    "TIPO" : dados[2],
                }
                registro = (f'\nNome:{ponto[0]}'
                            f'\nData:{ponto[1]}'
                            f'\nTipo:{ponto[2]}')
                return registro

def ponto_entrada():
    try:
         nome = input("Digite o seu nome: ")
         data = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
         tipo = "ENTRADA"
         append_entradas(nome,data,tipo)
         print("\nPonto de Entrada Registrado com Sucesso !!!"
               f"\nNome:{nome}"
               f"\nData:{data}"
               f"\nTipo:{tipo}")

    except Exception as e:
        print(f"Error:{e}")


def write_saidas():
    if not os.path.exists(SAIDAS):
        with open(SAIDAS,'w'):
            ...

def append_saidas(nome,data,tipo):
    with open(SAIDAS,'a') as arquivo:
        saida = f'{nome};{data};{tipo}\n'
        arquivo.write(saida)

def read_saidas():
    with open(SAIDAS,'r') as arquivo:
        saidas = arquivo.readlines()

        if len(saidas) == 0:
            print("Lista de entradas vazias")
        else:
            for saida in saidas:
                dados = saida.strip().split(";")
                ponto = {
                    "NOME" : dados[0],
                    "DATA" : dados[1],
                    "TIPO" : dados[2],
                }
                registro = (f'\nNome:{ponto[0]}'
                            f'\nData:{ponto[1]}'
                            f'\nTipo:{ponto[2]}')
                return registro

def ponto_saida():
    try:
         nome = input("Digite o seu nome: ")
         data = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
         tipo = "SAIDA"

         append_saidas(nome,data,tipo)

         print("\nPonto de Saida Registrado com Sucesso !!!"
               f"\nNome:{nome}"
               f"\nData:{data}"
               f"\nTipo:{tipo}")

    except Exception as e:
        print(f"Error:{e}")


