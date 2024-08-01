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