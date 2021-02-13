#Bibliotecas utilizadas
import matplotlib.pyplot as plt
import numpy as np
import json 
import math
#Variáveis e listas vazias
C = 0
X = []
Y = []
Pista_completa = []
#Funções
    
    #Ler o arquivo unsorted
def Ler_JSON_unsorted():
    Arquivo_JSON_unsorted = open('unsorted_testcase.json', 'r') 
    Unsorted_testcase = json.load(Arquivo_JSON_unsorted)    
    a = Unsorted_testcase['center_line']
    return a
   
    #Ler o arquivo sorted 
def Ler_JSON_sorted():
    Arquivo_JSON_sorted = open('sorted_testcase.json', 'r') 
    Sorted_testcase = json.load(Arquivo_JSON_sorted)    
    a = Sorted_testcase['center_line']
    return a
    
    #Pegar as ARRAYS e organizar do maior para o menor e depois escolher a maior em Y, que seria o primeiro
def Selecionar_maior_Y(Array):
    Array.sort(key = lambda l: l[1], reverse = True)
    return Array[0]

    #Ordenar de maneira correta metade da pista (Falta ainda terminar)
def Ordenar_metade_da_pista(Array):
    #Fazer o looping que irá construir metade da figura
    for i in range(len(Array)):
        for h in range(len(Array)):
        
    Metade_da_pista = 
    return Metade_da_pista
    
    #Girar metade da pista em 180º 
def Girar_metade_da_pista():
    Metade_da_pista2 = Metade_da_pista.transpose()
    return Metade_da_pista2
   
    #Calcular o comprimento da pista 
def Calcular_comprimento(Array):
    for i in range(len(Array)):
        if i == len(Array):
            break
    else:    
        c = math.sqrt((Array[i + 1][0] - Array[i][0])**2 + (Array[i + 1][1] - Array[i][1])) 
        C += c
    Comprimento_da_pista = C * 2
    return Comprimento_da_pista

#Código
Arquivo_unsorted = Ler_JSON_unsorted()
Arquivo_sorted = Ler_JSON_sorted()
A_ = Selecionar_maior_Y(Arquivo_unsorted)
Metade_da_pista = Ordenar_metade_da_pista(Arquivo_unsorted)
Metade_da_pista2 = Girar_metade_da_pista()
    #Comparar a array criada com o arquivo JSON sorted 
np.array_equal(Arquivo_sorted, Pista_completa)
    #Imagem da pista (Falta resolver o ponto aberto)
for i in range(len(Pista_completa)):
    x = np.array(Pista_completa[i][0])
    y = np.array(Pista_completa[i][1])
    X.append(x)
    Y.append(y)
plt.plot(X, Y)
plt.title('Pista de corrida')
plt.xticks([], [])
plt.yticks([], [])
plt.show()
    #Comprimento da pista 
A = Calcular_comprimento(Metade_da_pista)
print("O comprimento da pista é de: ", A, " metros")



