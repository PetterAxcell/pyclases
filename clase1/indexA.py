def serie_fibonacci(n):
    '''
        recibes un número llamado n
    '''
    initA = 0
    initB = 1
    aux = 0
    devolvemos = 0
    
    val1 = initB
    val2 = initA
    if n != 0 and n != 1:
        for i in range(2,n+1,1):
            aux = val1 + val2
            val2 = val1
            val1 = aux
            devolvemos = aux
    elif n == 1:
        devolvemos = initB
    elif n == 0:
        devolvemos = initA
    
    return devolvemos

    
        



if __name__ == "__main__":
    recuperar_numero = serie_fibonacci(6)
    print("Estamos fuera")
    print(recuperar_numero)
