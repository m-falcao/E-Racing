#O que eu tenho que fazer:
#1)Pegar o arquivo JSON unsorted 
#2)Trabalhar com a ARRAY do arquivo JSON unsorted
    #Ordena-la a partir dos valores Y : [X][Y]
        #O primeiro vetor será o ponto mais alto
            #Como o desenho é simétrico, só preciso trabalhar com metade, depois é só girar o trabalhado em 180º
#3)Fazendo o desenho
    #A partir da figura temos o seguinte looping (Sentido anti-horário):
        #Looping se repete 4 vezes
        #1) X aumenta e Y aumenta
        #2) X diminui e Y aumenta
        #3) X diminui e Y diminui
        #4) X diminui e Y aumenta
#4)Calcular o comprimento do desenho
    #Calcular a distância ponto a ponto
#Bibliotecas utilizadas
import matplotlib.pyplot as plt
import numpy as np
import json 
import math
#Variáveis e listas vazias
C = 0
X = []
Y = []
Grupo_de_baixo1 = []
Grupo_de_baixo2 = []
#Funções
    
    #Ler o arquivo unsorted (FEITO)
def Ler_JSON_unsorted():
    Arquivo_JSON_unsorted = open('unsorted_testcase.json', 'r') 
    Unsorted_testcase = json.load(Arquivo_JSON_unsorted)    
    a = Unsorted_testcase['center_line']
    return a
   
    #Ler o arquivo sorted (FEITO)
def Ler_JSON_sorted():
    Arquivo_JSON_sorted = open('sorted_testcase.json', 'r') 
    Sorted_testcase = json.load(Arquivo_JSON_sorted)    
    a = Sorted_testcase['center_line']
    return a
    
    #Pegar as ARRAYS e organizar do maior para o menor e depois escolher a maior em Y, que seria o primeiro (FEITO)
def Selecionar_maior_Y(Array):
    Array.sort(key = lambda l: l[1], reverse = True)
    return Array[0]

    #Ordenar de maneira correta metade da pista (Falta ainda terminar)
def Ordenar_metade_da_pista(Array):
    #Fazer o looping que irá construir metade da figura
    for i in range(len(Array)):
        for h in range(len(Array)):
            if Array[i][1] < Array[0][1]: #Y menor que o ponto inicial
                if Array[i][0] < Array[i + 1][0]:
                Grupo_de_baixo1.append(Array[i][0])
                else:
                Grupo_de_baixo2.append(Array[i][0])            
            if Array[i][1] > Array[1][1]: #Y maior que o ponto secundário
                Grupo_de_cima1
        
    Metade_da_pista = 
    return Metade_da_pista
    
    #Girar metade da pista em 180º (FEITO)
def Girar_metade_da_pista(Array):
    Metade_da_pista2 = Metade_da_pista.transpose()
    return Metade_da_pista2
   
    #Calcular o comprimento da pista (FEITO)
def Calcular_comprimento(Array):
    for i in range(len(Array)):
        if i == len(Array):
            break
    else:    
        c = math.sqrt((Array[i + 1][0] - Array[i][0])**2 + (Array[i + 1][1] - Array[i][1])) 
        C += c
    Comprimento_da_pista = C * 2
    return Comprimento_da_pista

    #Criar a matriz da soma das duas metades
def Soma_das_metades(Array1, Array2)
#Código
Arquivo_unsorted = Ler_JSON_unsorted()
Arquivo_sorted = Ler_JSON_sorted()
    #Comparar a array criada com o arquivo JSON sorted (FEITO)
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
    #Comprimento da pista (FEITO)
A = Calcular_comprimento(Metade_da_pista)
print("O comprimento da pista é de: ", A, " metros")



