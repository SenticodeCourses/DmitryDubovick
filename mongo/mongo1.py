import pymongo as pm


client = pm.MongoClient("localhost", 27017)
db = client['preferences']
# admin_info = {'name': 'Dima',
#               'age': 19,
#               'phone_number': 80297153728}
coll = db['admin_pref']
# coll.insert_one(admin_info)


def update_name(new_name):
    if type(new_name) == str:
        coll.update_one({}, {"$set": {'name': new_name}})
    else:
        print('Wrong name!')


def update_age(age):
    if age.isdigit() and 0 < int(age) < 125:
        coll.update_one({}, {"$set": {'age': int(age)}})
    else:
        print('Wrong age!')


def update_phone(phone):
    if phone.isdigit():
        coll.update_one({}, {"$set": {'phone_number': int(phone)}})
    else:
        print('Wrong number!')




