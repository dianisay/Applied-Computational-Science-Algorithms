import random
import numpy as np
def selection(fit):
    offset=np.min(fit)
    total_fit=sum(fit)-(len(fit)*offset)
    pick=random.random() #número aleatorio entre 0 y 1
    fit_p=[] #proporción de aptitud respecto al total
    for i in range (0, len(fit)):
        fit_p.append((fit[i]-offset)/total_fit)
    fit_acc=0
    for i in range (0, len(fit)):
        fit_acc+=fit_p[i]
        if fit_acc>=pick:
            fit_index=i
            break
    return fit_index    
