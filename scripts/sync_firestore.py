import json
import os
import firebase_admin
from firebase_admin import credentials, firestore


JSON_FILE = "portfolio/data.json"

service_account = json.loads(
    os.environ["FIREBASE_SERVICE_ACCOUNT"]
)

cred = credentials.Certificate(service_account)

firebase_admin.initialize_app(cred)

db = firestore.client()

with open(JSON_FILE, "r", encoding="utf-8") as file:
    data = json.load(file)

db.collection("portfolio").document("main").set(data)

print("Successfully synchronized portfolio/data.json → Firestore")