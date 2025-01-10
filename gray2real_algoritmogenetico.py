def gray2real(indiv,vari,g_len):
    g=[]
    b=[]
    R=[]
    for i in range(vari): #obtener gray, binario y decimal de cada variable (gen) 
        g.append(indiv[i*g_len:(i+1)*g_len]) #seccionar el cromosoma en el gen correspondiente 
        #pasar a binario  
        bi=[]
        bi.append(g[i][0])       
        for j in range(g_len-1):
            bi.append(int(bi[j])^int(g[i][j+1]))
        #pasar a decimal    
        di=0
        for k in range(g_len):
            di+=bi[k]*2**(g_len-1-k)
#         ri=(di*amp/(2**g_len-1))+inf #escalar el decimal en el rango
        b.append(bi)
        R.append(di)  
    return R
