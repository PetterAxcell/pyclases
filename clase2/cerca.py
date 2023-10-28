def return_number_consonants(string1):
    '''
        Lo que hace
        Argumentos:
            String: Una palabra
        Return:
            Int: La posición de la primera vocal
    '''
    i = 0
    flag = True
    while(flag):
        if string1[i] in 'aeiouAEIOU':
            flag = False
        else:
            i+=1
    return i


def cerca():
    string1 = "brasa"
    return_number_consonants(string1)

if __name__ == '__main__':
    cerca()