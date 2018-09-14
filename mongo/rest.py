from flask import Flask
from flask.json import JSONEncoder
from flask import jsonify
from bson import ObjectId
import mongo1 as mgc

class MyJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return super(MyJSONEncoder, self).default(o)


app = Flask(__name__)
app.json_encoder = MyJSONEncoder


@app.route('/preferences/<pref>', strict_slashes=False)
def pref(pref):
    return jsonify(mgc.coll.find()[0][pref])


@app.route('/preferences/', strict_slashes=False)
def all_prefs():
    return jsonify(mgc.coll.find_one())


app.run('localhost', '8080')