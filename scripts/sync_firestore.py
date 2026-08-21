import json
import os

import firebase_admin
from firebase_admin import credentials, firestore

JSON_FILE = "portfolio/data.json"

print("Starting Firestore synchronization...")
print(f"Reading JSON file: {JSON_FILE}")

with open(JSON_FILE, "r", encoding="utf-8") as file:
    data = json.load(file)

print("JSON loaded successfully.")
print(f"Top-level keys: {list(data.keys())}")

service_account_json = os.environ.get("FIREBASE_SERVICE_ACCOUNT")

if not service_account_json:
    raise RuntimeError("FIREBASE_SERVICE_ACCOUNT secret is missing.")

service_account = json.loads(service_account_json)

print(f"Firebase project: {service_account.get('project_id')}")

cred = credentials.Certificate(service_account)

firebase_admin.initialize_app(cred)

db = firestore.client()

print("Writing to Firestore:")
print("Collection: portfolio")
print("Document: main")

db.collection("portfolio").document("main").set(data)

print("SUCCESS: portfolio/main updated successfully.")
