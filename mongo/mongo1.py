from flask import Flask
from flask.json import JSONEncoder
from flask import jsonify
import pymongo as pm
from bson import ObjectId

class MyJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return super(MyJSONEncoder, self).default(o)


client = pm.MongoClient("localhost", 27017)
db = client['preferences']
# admin_info = {'name': 'Dima',
#               'age': 19,
#               'phone_number': 80297153728}
coll = db['admin_pref']
# coll.insert_one(admin_info)

# collist = db.list_collection_names()
# if 'admin_pref' in collist:
#     print(1)
# else: print(0)


app = Flask(__name__)
app.json_encoder = MyJSONEncoder


@app.route('/preferences/<pref>', strict_slashes=False)
def pref(pref):
    return jsonify(coll.find()[0][pref])


@app.route('/preferences/', strict_slashes=False)
def all_prefs():
    return jsonify(coll.find_one())


app.run('localhost', '8080')