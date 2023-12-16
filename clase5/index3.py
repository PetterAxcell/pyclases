





database = {"Maria" : { "Dni" : "dsfas"}, "Joan": {"Dni": "asdfasf"}, "Ivan": {"Dni": "asdfas"}} 

new_db      = {"34679867Q" : {}}

for key, value in database.items():
    new_db[value["Dni"]] = {}

print(new_db)
