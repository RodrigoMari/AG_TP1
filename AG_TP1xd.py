import random

poblacion = []
fitness = []
poblacion_size = 10
gen_size = 30
cant_ciclos = 100
prob_crossover = float(0.75)
prob_mutacion = float(0.05)
coef = 1073741823

def print_poblacion_datos(decimales, valores_funcion):
    print("poblacion                                                                                  X           F obj.  fitness \n")
    for gen in range(poblacion_size):
        print("{:<30} {:<11} {:<7} {:<5}".format(str(poblacion[gen]), str(decimales[gen]), str(valores_funcion[gen]), str(fitness[gen])))
    
    print("                                                                                           -------------------------")
    print("                                                                                           Suma:      ","{:<7} {:<5}".format(round(sum(valores_funcion), 3), round(sum(fitness), 3)))
    print("                                                                                           Promedio:  ", "{:<7} {:<5}".format(round(sum(valores_funcion) / len(valores_funcion), 3), round(sum(fitness) / len(fitness), 3)))
    print("                                                                                           Maximo:    ","{:<7} {:<5}".format(max(valores_funcion), max(fitness)), "\n")
    print("--------------------------------------------------------------------------------------------------------------------")

def gen_poblacion():
    for i in range(poblacion_size):
        gen = []
        for _ in range(gen_size):
            gen.append(random.choice([0, 1]))

        poblacion.append(gen)

def crossover_poblacion(padre, madre, i):

    corte = random.randint(1, gen_size - 1)

    poblacion[i] = padre[:corte] + madre[corte:]
    poblacion[i+1] = madre[:corte] + padre[corte:]

def mutacion_hijo(hijo, i):

    principio = 0
    fin = 0
    
    principio = random.randint(1, gen_size - 1)
    while fin <= principio:
        fin = random.randint(1, gen_size - 1)

    for j in range(principio, fin + 1):
        hijo[j] = 1 - hijo[j]
    
    poblacion[i] = hijo


def fitness_poblacion():

    global fitness
    fitness = []
    decimales = []
    valores_funcion = []
    suma_valores = 0

    for i in range(poblacion_size):
        actual = poblacion[i]
        k = 0
        dec = 0
        for j in range(gen_size-1, -1, -1):
            if actual[j] == 1:
                dec = dec + pow(2, k)
            k += 1
        
        decimales.append(dec)
        valores_funcion.append(round(pow(dec/coef, 2), 3))
        suma_valores = suma_valores + valores_funcion[i]
    
    for i in range(poblacion_size):
        fitness.append(round((valores_funcion[i] / suma_valores), 3))


    print_poblacion_datos(decimales, valores_funcion)


def ruleta_seleccion():
    seleccion = []
    
    seleccion = random.choices(poblacion, fitness, k = 10)

    for i in range(0, poblacion_size, 2):
        if random.random() < prob_crossover:
            crossover_poblacion(seleccion[i], seleccion[i+1], i)
            if random.random() < prob_mutacion:
                mutacion_hijo(poblacion[i], i)
            if random.random() < prob_mutacion:
                mutacion_hijo(poblacion[i+1], i+1)
    

    

    




gen_poblacion()
fitness_poblacion()

for i in range(cant_ciclos):
    ruleta_seleccion()
    fitness_poblacion()
    print(i)
