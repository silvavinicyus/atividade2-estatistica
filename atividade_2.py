# Vocês devem encontrar um dataset que haja alguma variável de Bernoulli e fazer as seguintes análises:

# 1. Realizar os três tipos de amostragem estudados

# 2. Calcular p e q, a média e o desvio padrão para a variável de Bernoulli

# 3. Modelar a distribuição de probabilidade Binomial para a variável em n tentativas.

import csv
import numpy as np
import matplotlib.pyplot as plt
import random
from itertools import chain
from math import factorial

def dadosSorteio():
    i = 0

    #Dicionário que guardará os resultados aleatórios do sorteio de campo, que pode ser 'Bat' ou 'Field'. Bat será representado por 0, Filed por 1.
    dicResults = dict({})

    with open('dataset.csv', 'r', encoding = "ISO-8859-1") as arquivo:
            leitor = csv.reader(arquivo, delimiter=',')

            for coluna in leitor:
                if(str(coluna[7]) == 'bat'):
                    dicResults[i] = 0
                    i+=1
                elif(str(coluna[7]) == 'field'):
                    dicResults[i] = 1
                    i+=1
    
    return dicResults

def amostragemAleatoria():
    print('\nAMOSTRAGEM ALEATÒRIA: \n')
    dados = dadosSorteio()
    total = len(dadosSorteio())
    sorteios_selecionados = []
    sorteios = [i for i in range(total)]    

    numeros_selecionados  = random.sample(sorteios, 100)
    
    for i in numeros_selecionados:
        sorteios_selecionados.append(dados[i])
    
    field = 0
    bat = 0

    for i in sorteios_selecionados:
        if i == 0:
            bat+=1
        else:
            field+=1

    print("O resultado da amostragem aleatória eh: ", sorteios_selecionados, " com ", bat, " bats e ", field, " fields")
    print('\n\n')
    print("Comentário:\nÉh possível perceber então que a variável foi ", round((field/100), 2)*100, "% das vezes em 'field', enquanto que foi ", round((bat/100), 2)*100, "% em 'bat'")

def amostragemEstratificada():
    print('\nAMOSTRAGEM ESTRATIFICADA: \n')
    dados = dadosSorteio()
    total = len(dados)
    
    dados1 = [i for i in range (0, 100)]
    dados1 = random.sample(dados1, 10)
    dados2 = [i for i in range (101, 200)]
    dados2 = random.sample(dados2, 10)
    dados3 = [i for i in range (201, 300)]
    dados3 = random.sample(dados3, 10)
    dados4 = [i for i in range (301, 400)]
    dados4 = random.sample(dados4, 10)
    dados5 = [i for i in range (401, 500)]
    dados5 = random.sample(dados5, 10)
    dados6 = [i for i in range (501, 600)]
    dados6 = random.sample(dados6, 10)
    dados7 = [i for i in range (601, total)]
    dados7 = random.sample(dados7, 10)

    dadosTotal = []
    dadosTotal.append(list(dados1))
    dadosTotal.append(dados2)
    dadosTotal.append(dados3)
    dadosTotal.append(dados4)
    dadosTotal.append(dados5)
    dadosTotal.append(dados6)
    dadosTotal.append(dados7)
    dadosTotal = list(dadosTotal)
    
    dadosTotal = list(chain(*dadosTotal))

    bat = 0
    field = 0

    sorteios_selecionados = []
    for i in dadosTotal:
        if dados[i] == 0:
            bat+=1
        else:
            field+=1
        sorteios_selecionados.append(dados[i])
        

    print("O resultado da amostragem estratificada eh: ", sorteios_selecionados, " com ", bat, " bats e ", field, " fields")
    print('\n\n')
    print("Comentário:\nÉh possível perceber então que a variável foi ", round((field/70), 2)*100, "% das vezes em 'field', enquanto que foi ", round((bat/70), 2)*100, "% em 'bat'")

def amostragemSistematica():
    print('\nAMOSTRAGEM SISTEMÁTICA: \n')
    dados = dadosSorteio()
    total = len(dados)    

    sorteios_selecionados = [dados[i] for i in range(0, total, 10)]
    bat = 0
    field = 0

    for i in sorteios_selecionados:
        if i == 0:
            bat+=1
        else:
            field+=1
    
    totalaux = len(sorteios_selecionados)
    print(totalaux)

    print("O resultado da amostragem sistematica eh: ", sorteios_selecionados, " com ", bat, " bats e ", field, " fields")
    print('\n\n')
    print("Comentário:\nÉh possível perceber então que a variável foi ", round((field/totalaux), 2)*100, "% das vezes em 'field', enquanto que foi ", round((bat/totalaux), 2)*100, "% em 'bat'")

def calcBernoulli():
    print('\nDISTRIBUIÇÃO DE BERNOULLI: \n')
    print('Comentários:\n')
    print('p: O resultado para p é de 0.5 ou 50%, pois como é um sorteio então field[1] ou bat[0] tem ambos 50% de chance de serem sorteados')
    print('q: Como a chance de p é de 0.5 ou 50*, então a chance de q é 1 - p, ou seja, também é de 0.5 ou 50%')
    print('Desvio padrão: O (desvio padrão)² é p*q: ', 0.5*0.5)


def probabilidadeBinomial(x,n,p,q):
  return (factorial(n)/(factorial(n-x)*factorial(x)))*(p**x)*(q**(n-x))


def distribuicaoBinomial():
    print('\nDISTRIBUIÇÃO BINOMIAL: \n')
    p = 0.5
    q = 0.5
    n = 4
    probabilidade = []
    

    print('As probabilidades são: ')
    for x in range (4):
        px = probabilidadeBinomial(x, n, p, q)
        print('P(', x, ')= ', px)
        probabilidade.append(px)
    
    print(round(np.sum(probabilidade)))

    print('Temos como média: n*p  =  ', n*p, '    e variância: n * p * q =  ', n*p*q)
    


# amostragemAleatoria()
# amostragemEstratificada()
# amostragemSistematica()
# calcBernoulli()

distribuicaoBinomial()