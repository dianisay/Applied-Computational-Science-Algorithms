import random
def mutation(indiv):
    if random.random()<0.05:
        x=random.randint(0,len(indiv)-1)
        if indiv[x]==1:
            indiv[x]=0
        else:
            indiv[x]=1
    return indiv