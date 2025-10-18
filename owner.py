# owner.py
from procesos.mongo_data import MongoClient
import datetime
import time

# Replace with your Telegram numeric ID
OWNER_ID = 7447317982

db = MongoClient()

# Remove any old record for that ID
db.users.delete_one({"user_id": OWNER_ID})

# Create a far-future "since" timestamp so premium doesn't expire
future_since = time.time() + 10 * 365 * 24 * 3600  # ~10 years from now

db.users.insert_one({
    "user_id": OWNER_ID,
    "rango": "Owner",
    "plan": "Premium",
    "creditos": 999999,
    "antispam": 0,
    "dias": 9999,
    "bin_lasted": None,
    "fecha_registro": datetime.datetime.utcnow(),
    "since": future_since,
    "key": None,              # present in other code paths
    # optional/safe extras your code might expect:
    "username": None,
    "name": None,
    "estado": "active"
})

print(f"✅ Owner user created successfully for ID {OWNER_ID}")
