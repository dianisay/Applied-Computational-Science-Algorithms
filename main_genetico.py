import numpy as np
import random
from matplotlib import pyplot as plt
from population import *
from fitness import *
from newindiv import *
from gray2real import *
from selection import *
from crossover import *
from mutation import *

def main():
    #parámetros del problema
    vari=4
    #crear población inicial
    n=32 #tamaño de la población
    g_len=5 #tamaño de cada gen
    c_len=vari*g_len #tamaño de cromosoma
    pop=population(n,c_len)#hace la tablita
    print("*** Algoritmo genético ***")
    print("Tamaño de población:\t",n)
    print("Tamaño de cromosoma:\t",c_len)
    
    bestfitg=[]
    meanfitg=[]
    stddevfitg=[]
    gen=[]
    tg=int(input("Cantidad total de generaciones: "))
    for g in range(0,tg):
        fit=[]
        for indiv in pop:
            x=gray2real(indiv,vari,g_len)
            naux=x[3]+1 #cuadros de ancho
            maux=x[2]+1 #número de serpentines
            relaux=(2*naux-1)/maux #relacion entre ancho y largo de resistencia
            errel=abs(1-relaux) #qué tan cercana está a 1 la relación
            if errel<=0.5: #para darle prioridad a las resistencias casi cuadradas
                fit.append(fitness(gray2real(indiv,vari,g_len)))
            else:
                fit.append(-1) #si no es casi cuadrada, se le  asigna un MSE grande
        fit_index=selection(fit)
        parent0=pop[fit_index]
        fit_index=selection(fit)
        parent1=pop[fit_index]
        while parent1 == parent0:
            fit_index=selection(fit)
            parent1=pop[fit_index]
        offspring0, offspring1=crossover(parent0, parent1) #cruza   
        offspring0=mutation(offspring0)
        offspring1=mutation(offspring1)
        
        #--------------------------------
        fitp0=fitness(gray2real(parent0,vari,g_len))
        fitp1=fitness(gray2real(parent1,vari,g_len))
        fito0=fitness(gray2real(offspring0,vari,g_len))
        fito1=fitness(gray2real(offspring1,vari,g_len))
        newpop=[] #nueva población
        #criterios para ver quien pasa
        if fito0 >= fitp0 or fito0 >= fitp1:
            newpop.append(offspring0)
        if fito1 >= fitp0 or fito1 >= fitp1:
            newpop.append(offspring1)        
        if fitp0 >= fito0 and fitp0 >= fito1:
            newpop.append(parent0)
        if fitp1 >= fito0 and fitp1 >= fito1:
            newpop.append(parent1)       
        
        bestfit=np.max(fit)
        bestfitg.append(-bestfit)
        meanfit=np.mean(fit)
        meanfitg.append(-meanfit)
        stddevfit=np.std(fit)
        stddevfitg.append(stddevfit)
        gen.append(g)
        #elitismo
        bestindex=fit.index(bestfit)
        newpop.append(pop[bestindex])
        #elitismo extendido (incluir a las que están fuera del promedio positivamente)
        for i in range (n):
            if fit[i]>(meanfit+stddevfit):
                newpop.append(pop[i]) 
        #fillers
        while(len(newpop)<n):
            newpop.append(newindiv(c_len))
        if g < tg-1: #para no actualizar pop en el último ciclo
            pop=newpop
    plt.figure(1)
    plt.plot(gen,bestfitg)
    plt.title('Evolución del mejor MSE por generación')
    plt.ylabel('MSE')
    plt.xlabel('Generación')
    plt.figure(2)
    plt.plot(gen,meanfitg)
    plt.title('Evolución del MSE promedio por generación')
    plt.ylabel('MSE')
    plt.xlabel('Generación')
    plt.figure(3)
    plt.plot(gen,stddevfitg)
    plt.title('Evolución de la desv. estandar del MSE por generación')
    plt.ylabel('MSE')
    plt.xlabel('Generación')
    
    gamma=0.01
    beta=4.5e-6
    Vth=0.69
    Vgs=[0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5]
    VR_data = [1.00E-07, 2.50E-02, 1.00E-01, 2.25E-01, 4.00E-01, 6.25E-01, \
            9.00E-01, 1.23E+00, 1.57E+00, 1.84E+00, 2.07E+00]
    V1=5
    
    sol=gray2real(pop[bestindex],vari,g_len)
    L = sol[1]+2
    W = 2*L+sol[0]
    m=sol[2]+1 #cuadros de ancho 
    n=sol[3]+1 #número de serpentines
    c=m*n+(n-1) #cuadros totales
    e=(n-1)*2 #cuadros esquina
    r=25*(c-e+(2*e/3)) #resistencia
    rel=(2*n-1)/m #relacion entre ancho y largo de resistencia
    Vr=[]
    for i in range(len(Vgs)):
        if Vgs[i] <= Vth:
            Id = 0.0
            Vr.append(r*Id)
        else:
            y = 0.5*beta*(W/L)*(Vgs[i]-Vth)**2
            Id=(y+y*gamma*V1)/(1+y*gamma*r)
            Vr.append(r*Id)
    print('W: '+str(0.5*W)+'μm\t'+'L: '+str(0.5*L)+'μm') #se multiplican por lambda de 0.5μm
    print('m: '+str(m)+'\t'+'n: '+str(n))
    print('R: '+str(round(r,4))+'Ω\t'+'Ws/Ls: '+str(round(rel,2)))
    print("mean sq error: ", round(-bestfit, 4))
    plt.figure(4)
    plt.plot(Vgs,VR_data)
    plt.plot(Vgs,Vr)
    plt.grid()
    plt.legend(['data','calculated'])
    plt.title('$V_R$ vs $V_{GS}$')
    plt.ylabel('resistor voltage (V)')
    plt.xlabel('gate-to-source voltage (V)')
    plt.show()
main()
