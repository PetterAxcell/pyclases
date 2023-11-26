from colorama import init, Fore, Back, Style
init(autoreset=True)


Alumnos = [["Arnau", 10, 9, 3, 10], ["Ivan", 4, 2, 7], ["Alex", 5, 4, 6, 10], ["Maria", 3, 10, 4], ["Alba", 2, 3, 10]]

def desvia(lista, media):
    sum_var = 0
    print(lista)
    for i in lista:
        sum_var += abs(i-media)
    return (sum_var/len(lista))

def media(Alumnos):
    media_total = 0
    count = 0
    flag = True
    for alumno in Alumnos:
        media_individual=0
        for index in range(1, len(alumno)):
            media_individual += alumno[index]
            media_total += alumno[index]
            count += 1
        media_individual = media_individual/(len(alumno)-1)
        desviacion_tipica = desvia(alumno[1:], media_individual)
        if flag == True:
            print(Fore.BLUE+ f"La desviación tipica es: {desviacion_tipica}")
            flag = False
        else: 
            varianza = desviacion_tipica * desviacion_tipica
            print(Fore.BLUE+ f"La varianza es: {desviacion_tipica}")
            flag = True 
        print(Fore.WHITE + f"La media individual es: {media_individual}")
    media_total = media_total/count
    print(Fore.WHITE+Back.RED+"La media total es:")
    print(media_total)
media(Alumnos)
