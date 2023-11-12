"""
    Guarda en una lista los números primos
"""
def check(lista, count):
    for i in lista:
        if count % i == 0 and i!=1:
            return False
    return True

def lista_numeros_primos(num):
    lista_ret = []
    count = 1
    while(len(lista_ret)<num):
        if len(lista_ret)==0:
            lista_ret.append(count)
        else:
            if check(lista_ret, count):
                lista_ret.append(count)
        count +=1
    return lista_ret

print(lista_numeros_primos(10))
