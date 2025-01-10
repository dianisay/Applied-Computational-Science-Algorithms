def fitness(R):
    gamma=0.01
    beta=4.5e-6
    Vth=0.69
    Vgs=[0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5]
    VR_data = [1.00E-07, 2.50E-02, 1.00E-01, 2.25E-01, 4.00E-01, 6.25E-01, \
            9.00E-01, 1.23E+00, 1.57E+00, 1.84E+00, 2.07E+00]
    V1=5
    
    L = R[1]+2      #gate length, se suma 2 para que sea mínimo 1μm
    W = 2*L+R[0]      #gate width, se le suma el doble de L para que mínimo sea el doble de L
    m=R[2]+1 #cuadros de ancho 
    n=R[3]+1 #número de serpentines
    c=m*n+(n-1) #cuadros totales
    e=(n-1)*2 #cuadros esquina
    r=25*(c-e+(2*e/3)) #resistencia
    Vr=[]
    mse=0
    for i in range(len(Vgs)):
        if Vgs[i] <= Vth:
            Id = 0.0
            Vr.append(r*Id)
        else:
            y = 0.5*beta*(W/L)*(Vgs[i]-Vth)**2
            Id=(y+y*gamma*V1)/(1+y*gamma*r)
            Vr.append(r*Id)
        mse=mse+(Vr[i]-VR_data[i])**2
    MSE = -(1/len(VR_data))*mse 
    return MSE