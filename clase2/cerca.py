def return_position_firs_vowal(string1):
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


def return_string_longer(string1, string2):
    '''
        Esta función devuelve el parametro más largo
        Args:
            string: Primer string
            string: Segundo string
        Returns:
            String: Longer string
    '''
    i = 0
    while(i<len(string1) and i<len(string2)):
        print(string1[i])
        print(string2[i])
        i+=1

    if(i==len(string1)):
        return string2
    else:
        return string1

def cerca():
    string1 = "brasa"
    string2 = "Voy al parque a jugar"
    string_longer = return_string_longer(string1, string2)
    print(string_longer)

if __name__ == '__main__':
    cerca()