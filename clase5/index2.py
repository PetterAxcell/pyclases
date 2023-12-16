DATABASE = {'Maria': {'Dni': '53421202L', 'Dirección': 'c/  urquinaona23', 'Código Postal': 23445}, 'Ivan': {'Dni': '16421202L', 'Dirección': 'c/  urquinaona25', 'Código Postal': 23445}, 'Joan': {'Dni': '2345678H', 'Dirección': 'urquinaona 19', 'Código Postal': '23445'}, 'Erick': {'Dni': '12332112D', 'Dirección': 'rosello 1', 'Código Postal': '09889'}} 


def refactor(db):
    new_db = {}
    for clave, valor in db.items():
        new_db[valor["Dni"]] = {"Name": clave, "Dirección":valor["Dirección"], "Codigo Posta"} 
    return new_db

DATABASE = refactor(DATABASE)
