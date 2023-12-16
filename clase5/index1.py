DATABASE = {"Maria": {"Dni": "53421202L", "Dirección": "c/  urquinaona23", "Codigo Posta": 23445}, "Ivan":{"Dni": "16421202L", "Dirección": "c/  urquinaona25", "Codigo Posta": 23445}}

def insert_database(DATABASE, name2add, DNI2Add, Address2Add, PostalCode2Add):
    DATABASE[name2add] = {"Dni" : DNI2Add, "Dirección":Address2Add, "Código Postal" : PostalCode2Add}
    return DATABASE

DATABASE = insert_database(DATABASE, "Joan", "2345678H", "urquinaona 19", "23445")
DATABASE = insert_database(DATABASE, "Erick", "12332112D", "rosello 1", "0988") 

print(DATABASE)
