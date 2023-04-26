import random

poblacion = []
poblacion_size = 10
gen_size = 30
prob_mutacion = float(0.05)

def print_poblacion():
    for gen in range(poblacion_size):
        print(poblacion[gen])

def gen_poblacion():
    for i in range(poblacion_size):
        gen = []
        for _ in range(gen_size):
            gen.append(random.choice([0, 1]))

        poblacion.append(gen)

def crossover_poblacion(madre_indice, padre_indice):
    madre = poblacion[madre_indice]
    padre = poblacion[padre_indice]

    corte = random.randint(1, gen_size - 1)

    poblacion[madre_indice] = padre[:corte] + madre[corte:]
    poblacion[padre_indice] = madre[:corte] + padre[corte:]

    print(corte)

def fitness_poblacion():

    fitness = []

    for i in range(poblacion_size):
        actual = poblacion[i]
        k = 0
        fit = 0
        for j in range(gen_size-1, -1, -1):
            if actual[j] == 1:
                fit = fit + pow(2, k)
            k += 1
        
        fitness.append(fit)
        

def mutacion_hijo(hijo_indice): #La mutacion que pide es la invertida que dice que si se cumple la probabilidad agarremos un segmento de bits
                                #random y mutemos todos los bits entre ese segmento 
    
    hijo_mutado = poblacion[hijo_indice]

    principio = 0
    fin = 0
    if random.random() < prob_mutacion:
        principio = random.randint(1, gen_size - 1)
        
        while fin <= principio:
            fin = random.randint(1, gen_size - 1)
        print(principio)
        print(fin)
        for j in range(principio, fin + 1):
            print(j)
            hijo_mutado[j] = 1 - hijo_mutado[j]
    




gen_poblacion()
print_poblacion()
#crossover_poblacion(0, 1) #Solo hace crossover con 2 padres
#fitness_poblacion() #Genera un array de la longitud de la poblacion con los valores de fitness (sin ordenar de mayor a menor todavia)
#mutacion_hijo(0) #Mutacion de un hijo
