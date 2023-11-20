import pymongo as pm
import pprint
import datetime

client = pm.MongoClient(
    "mongodb+srv://fredMelchior:NnjR0QTvg5NWU2J6@firstcluster0.lkgkx28.mongodb.net/"
)

db = client.test
bank_collection = db.bank_collection
print(db.bank_collection)

accounts = [
    {
        "name": "Fred",
        "CPF": "992.12.22",
        "address": "sd@dsdm.com",
        "account": 1,
        "agency": "0001",
        "type": "C/C",
        "currency": 324.5,
    },
    {
        "name": "Abraão",
        "CPF": "38.47.123",
        "address": "sdkfjh@jd.com",
        "account": 2,
        "agency": "0001",
        "type": "Savings",
        "currency": 1222.76,
    },
    {
        "name": "Salvia",
        "CPF": "009.1.2331",
        "address": "asd@fdfds.com",
        "account": 3,
        "agency": "0001",
        "type": "C/C",
        "currency": 8726.18,
    },
]

bank = db.bank

# bank.insert_many(accounts)
for acc in bank.find({}):
    print(f"\n")
    pprint.pprint(acc)
