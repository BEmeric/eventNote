from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

print('Controle de connexion à MongoDB en cours ....')

# Controle de la connexion à mongoDB
uri = "mongodb+srv://superuser:292407@cluster0.lcohyqa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"Erreur de connexion à MongoDB : {e}")

client.close()

from datetime import datetime

def string_to_date(date_string):
    # Étape 1 : Vérifier si la chaîne peut être convertie en un nombre entier
    try:
        date_number = int(date_string)
    except ValueError:
        return "Erreur : la chaîne fournie ne peut pas être convertie en un nombre entier."

    # Étape 2 : Vérifier si le nombre entier peut être interprété comme une date valide
    date_str = str(date_number)
    if len(date_str) != 8:
        return "Erreur : le nombre entier ne correspond pas à un format de date valide AAAAMMJJ."

    try:
        date_obj = datetime.strptime(date_str, "%Y%m%d")
    except ValueError:
        return "Erreur : la date fournie n'est pas valide."

    # Étape 3 : Convertir ce nombre en un format de date AAAAMMJJ
    return date_obj.strftime("%Y%m%d")

# Exemples d'utilisation
print(string_to_date("20230807"))  # Sortie attendue: 20230807
print(string_to_date("20231301"))  # Sortie attendue: Erreur : la date fournie n'est pas valide.
print(string_to_date("abc"))       # Sortie attendue: Erreur : la chaîne fournie ne peut pas être convertie en un nombre entier.
print(string_to_date("202308"))    # Sortie attendue: Erreur : le nombre entier ne correspond pas à un format de date valide AAAAMMJJ.
