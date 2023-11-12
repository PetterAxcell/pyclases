"""
    Guarda en una lista los números primos
"""

def lista_numeros_primos(num):
    lista_ret = []
    count = 1
    while(len(lista_ret<num)):
        flag = False
        if len(lista_numeros_primos)==0:
            lista_ret.append(count)
        else:
            for i in lista_ret:
                if count % i == 0 and i!=1:
                    flag = True
        if flag == True:
            lista_ret.append(count)
        count +=1

lista_numeros_primos(4)
