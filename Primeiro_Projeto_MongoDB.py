import datetime
import pprint

import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://erick:35312017@cluster0.zbeqe5i.mongodb.net/?retryWrites=true&w=majority")

db = client.test
collection = db.test_collection
print(db.test_collection)

post = {
    "Nome":"Erick",
    "Cpf":"143..411.466-02",
    "Endereço":"Rua,45",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.utcnow()
}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

new_post = [{
    "Conta":"01",
    "Tipo":"Corrente",
    "num":"4500",
    "tags": ["familia", "companheira", "amiga"],
    "date": datetime.datetime.utcnow()}]
resultado = posts.insert_many(new_post)
pprint.pprint(resultado.inserted_ids)

print("\nRecuperação Final")

pprint.pprint(db.posts.find_one({"Nome":"Erick"}))
print("\n")
pprint.pprint(db.posts.find_one({"Conta":"01"}))
