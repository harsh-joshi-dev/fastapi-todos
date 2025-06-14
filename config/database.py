from pymongo import MongoClient
client =  MongoClient("mongodb+srv://kellyharrisoninfo:1gNy7ZxN8VoQHDE9@project0.e1kmvyv.mongodb.net/?retryWrites=true&w=majority&appName=Project0")

db= client.todo_db

collection_name = db["todo_collection"]