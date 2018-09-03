from flask import Flask
from flask.json import JSONEncoder
from flask import jsonify
from country import Country
from city import City
from region import Region


class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Country):
            result = dict(obj.__dict__)
            if result['regions']:
                for i in range(len(result['regions'])):
                    name = result['regions'][i].name
                    result['regions'][i] = name

            return result

        if isinstance(obj, Region):
            result = dict(obj.__dict__)
            if result['cities']:
                for i in range(len(result['cities'])):
                    name = result['cities'][i].name
                    result['cities'][i] = name
            return result

        if isinstance(obj, City):
            result = dict(obj.__dict__)
            return result

        return super(MyJSONEncoder, self).default(obj)


app = Flask(__name__)
app.json_encoder = MyJSONEncoder
minsk_region_cities = [City('Nesvizh', 14300), City('Slutsk', 61400)]
regions_of_belarus = [Region('Minsk Region', 1411500, minsk_region_cities), Region('Vitebsk Region', 1221800)]
my_countries = {'belarus': Country('Belarus', 'Minsk', 10000000, regions_of_belarus)}


@app.route('/countries/<country>', strict_slashes=False)
def country_info(country):
    if my_countries[country]:
        result = jsonify(my_countries[country])
    else:
        result = 'Wrong country!'
    return result

@app.route('/countries/', strict_slashes=False)
def countries():
    all_countries = []
    for country in my_countries:
        all_countries.append(my_countries[country].name)
    return jsonify(all_countries)

@app.route('/countries/<country>/regions/', strict_slashes=False)
def regions(country):
    all_regions = []
    if my_countries[country].regions:
        for region in my_countries[country].regions:
            all_regions.append(region.name)
    return jsonify(all_regions)

@app.route('/countries/<country>/regions/<region>', strict_slashes=False)
def region_info(country, region):
    info = None
    for reg in my_countries[country].regions:
        if reg.name.lower().replace(' ', '') == region:
            info = reg
    if info:
        result = jsonify(info)
    else:
        result = 'Wrong region!'
    return result





app.run('localhost', '8080')