
matriz = [[1, 2, 3],
          [ 4, 5, 6],
          [ 7, 8, 9 ]] #O(1)

matrizes=[]  #O(1)

def ele1(f,c,pasos:int,matrixguia:list,matrixes:list):  #O(1)
    actualf = f  #O(1)
    actualc = c  #O(1)



    for i in range(pasos):  #O(n)
      actualf = actualf  #O(n)
      actualc = actualc+1  #O(n)
      matrixes.append(matrixguia[actualf][actualc])  #O(n)


    for j in range(pasos):  #O(n)
      actualf = actualf+1  #O(n)
      actualc = actualc  #O(n)
      matrixes.append(matrixguia[actualf][actualc]) ##O(n)

    return actualf,actualc  #O(1)

def ele2(f,c,pasos:int,matrixguia:list,matrixes:list): #O(1)
    actualf = f #O(1)
    actualc = c #O(1)



    for i in range(pasos): #O(n)
      actualf = actualf #O(n)
      actualc = actualc-1 #O(n)
      matrixes.append(matrixguia[actualf][actualc]) #O(n)


    for j in range(pasos): #O(n)
      actualf = actualf-1 #O(n)
      actualc = actualc #O(n)
      matrixes.append(matrixguia[actualf][actualc]) #O(n)

    return actualf,actualc #O(1)



def espiral_def(matrif,matrifes:list):#O(1)
   medio = int( (len(matrif)/ 2)+0.5)#O(1)
   mediof= medio-1  #O(1)
   medioc= medio-1  #O(1)
   matrifes.append(matrif[mediof][medioc])#O(1)
   pasos = len(matrif)-1#O(1)
   newcor= mediof,medioc#O(1)

   if matrif[0] != matrif[-1]:#O(1)
      for i in range(pasos):#O(n)
         if (i+1) % 2 != 0:#O(n)
                newcor = ele1(newcor[0],newcor[1],i+1,matrif,matrifes)#O(n)
         else:#O(n)

             newcor = ele2(newcor[0],newcor[1],i+1,matrif,matrifes)#O(n)

      for j in matrif[0]:#O(n)
             if j != matrif[0][0]:#O(n)
                  matrifes.append(j)#O(n)
   else:#O(1)
      print("es 1x1 asi que es  ",matrif[0])#O(1)
   
   

if len(matriz) % 2 != 0 :#O(1)
     espiral_def(matriz,matrizes)#O(n)


print(matrizes)#O(1)

