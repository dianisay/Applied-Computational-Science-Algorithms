import random
def newindiv(c_len):
    indiv=[]
    for i in range (0,c_len):
        if random.random()>0.5:
            indiv.append(1)
        else:
            indiv.append(0)
    return indiv
