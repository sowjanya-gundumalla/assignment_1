#!/usr/bin/env python3
from configparser import ConfigParser, ParsingError
from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

#config
CONFIG_FILE = "config.ini" 
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "studentsdb"
COLLECTION_NAME = "config"

#config-read
def read_config():
    """Reads and parses the configuration file into a dictionary."""

    if not os.path.exists(CONFIG_FILE):
        return None, f"Configuration file '{CONFIG_FILE}' not found."

    parser = ConfigParser()

    try:
        parser.read(CONFIG_FILE)
    except ParsingError as e:
        return None, f"Error reading configuration file: {e}"

    # Convert config to dictionary
    try:
        config_dict = {section: dict(parser[section]) for section in parser.sections()}
    except Exception as e:
        return None, f"Failed to parse configuration: {e}"

    return config_dict, None


#savetomongo

def save_to_mongo(data):
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    coll = db[COLLECTION_NAME]
    result = coll.insert_one({"config": data})
    client.close()
    return str(result.inserted_id)


#API
@app.route("/add", methods=["GET"])
def add_config():
    """Reads config.ini and stores parsed JSON into MongoDB."""
    config_data, err = read_config()

    if err:
        return jsonify({"status": "error", "message": err}), 400

    inserted_id = save_to_mongo(config_data)

    return jsonify({
        "status": "ok",
        "inserted_id": inserted_id,
        "data": config_data
    }), 201


@app.route("/get", methods=["GET"])
def get_configs():
    """Fetch all saved config JSON objects from MongoDB."""
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    coll = db[COLLECTION_NAME]
    docs = list(coll.find({}))
    client.close()

    # Convert ObjectId to string
    for doc in docs:
        doc["_id"] = str(doc["_id"])

    return jsonify({
        "status": "ok",
        "count": len(docs),
        "results": docs
    })



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
