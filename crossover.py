import random
def crossover(parent0, parent1):
    if random.random() < 0.75: #verificar si se cruzan o no, valor arbitrario
        cut=random.randint(0,len(parent0)-2) #-2 para forzar a que no quede igual
        offspring0=[]
        offspring1=[]
        for i in range(len(parent0)):
            if i <= cut:
                offspring0.append(parent0[i])
                offspring1.append(parent1[i])
            else:
                offspring0.append(parent1[i])
                offspring1.append(parent0[i])        
    else:
        offspring0=parent0
        offspring1=parent1
    return offspring0, offspring1
