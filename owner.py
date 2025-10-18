from procesos.mongo_data import MongoClient
import datetime

OWNER_ID = 123456789  # <-- replace with your Telegram ID

db = MongoClient()

db.users.delete_one({"user_id": OWNER_ID})  # remove old record if any

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
