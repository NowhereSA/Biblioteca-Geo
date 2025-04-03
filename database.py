from pymongo import MongoClient

cliente = MongoClient('mongodb://localhost:27017')
db = cliente['Biblioteca']
collection = db['dados']