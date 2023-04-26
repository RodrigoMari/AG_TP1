import random

poblacion = []
poblacion_size = 10
gen_size = 30

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



gen_poblacion()
print_poblacion()
crossover_poblacion(0, 1)
print_poblacion()