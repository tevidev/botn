import datetime
from procesos.mongo_data import MongoClient

# === CONFIG ===
OWNER_ID = 7447317982  # <-- your Telegram ID

db = MongoClient()

# === 1. CREATE OWNER USER ===
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

# === 2. ADD/UPDATE GATES ===
# These gates are based on real commands your bot uses (from your files)
default_gates = [
    {"comando": "/pp", "nombre": "Paypal", "estado": "✅"},
    {"comando": "/vbv", "nombre": "Braintree 3D", "estado": "✅"},
    {"comando": "/chk", "nombre": "Stripe Charge", "estado": "✅"},
    {"comando": "/stp", "nombre": "Stripe Auth", "estado": "✅"},
    {"comando": "/ss", "nombre": "Stripe Save", "estado": "✅"},
    {"comando": "/bin", "nombre": "Bin Lookup", "estado": "✅"},
    {"comando": "/key", "nombre": "Key Activation", "estado": "✅"},
    {"comando": "/register", "nombre": "Register", "estado": "✅"},
]

for gate in default_gates:
    db.collection_cuatro.update_one({"comando": gate["comando"]}, {"$set": gate}, upsert=True)

print(f"✅ Gates inserted/updated successfully ({len(default_gates)} total)")
