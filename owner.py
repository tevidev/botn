import datetime
from procesos.mongo_data import MongoClient

# Replace with your real Telegram ID
OWNER_ID = 7447317982

# Connect to your database
db = MongoClient()

# ----- CREATE OWNER -----
db.users.delete_one({"user_id": OWNER_ID})

db.users.insert_one({
    "user_id": OWNER_ID,
    "rango": "Owner",
    "plan": "Premium",
    "creditos": 999999,
    "antispam": 0,
    "dias": 9999,
    "bin_lasted": None,
    "fecha_registro": datetime.datetime.now(),
    "since": None
})

print(f"✅ Owner user created successfully for ID {OWNER_ID}")

# ----- ADD GATES -----
# Matches your mongo_data structure — only adds to 'gates' collection
default_gates = [
    {"comando": "/pp", "estado": "✅"},
    {"comando": "/chk", "estado": "✅"},
    {"comando": "/au", "estado": "✅"},
    {"comando": "/vbv", "estado": "✅"},
    {"comando": "/ss", "estado": "✅"},
]

for gate in default_gates:
    db.collection_cuatro.update_one({"comando": gate["comando"]}, {"$set": gate}, upsert=True)

print(f"✅ Gates added/updated successfully ({len(default_gates)} total)")
