from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from bson import ObjectId
import os

app = Flask(__name__)

# Configuration de la base de données MongoDB
mongo_uri = "mongodb+srv://superuser:292407@cluster0.lcohyqa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(mongo_uri)
db = client.db_events
collection = db.collection_event

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_event', methods=['POST'])
def add_event():
    data = request.json
    start = data.get('Start')
    stop = data.get('Stop')
    tag = data.get('Tag')

    if not start or not tag:
        return jsonify({"error": "Les champs 'Start' et 'Tag' sont obligatoires"}), 400

    event = {"Start": start, "Stop": stop, "Tag": tag}
    result = collection.insert_one(event)
    return jsonify({"message": "Événement ajouté", "id": str(result.inserted_id)}), 201

@app.route('/list_events', methods=['GET'])
def list_events():
    events = list(collection.find())
    for event in events:
        event['_id'] = str(event['_id'])
    return jsonify(events), 200

@app.route('/remove_event/<event_id>', methods=['DELETE'])
def remove_event(event_id):
    result = collection.delete_one({"_id": ObjectId(event_id)})
    if result.deleted_count == 1:
        return jsonify({"message": "Événement supprimé"}), 200
    else:
        return jsonify({"error": "Événement non trouvé"}), 404

if __name__ == '__main__':
    app.run(debug=True)
