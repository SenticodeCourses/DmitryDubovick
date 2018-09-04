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
                names = []
                for i in result['regions'].values():
                    names.append(i.name)
                result['regions'] = names
            return result

        if isinstance(obj, Region):
            result = dict(obj.__dict__)
            if result['cities']:
                names = []
                for i in result['cities'].values():
                    names.append(i.name)
                result['cities'] = names
            return result

        if isinstance(obj, City):
            result = dict(obj.__dict__)
            return result

        return super(MyJSONEncoder, self).default(obj)


app = Flask(__name__)
app.json_encoder = MyJSONEncoder
minsk_region_cities = {'nesvizh': City('Nesvizh', 14300),
                       'slutsk': City('Slutsk', 61400)}
viebsk_region_cities = {'orsha': City('Orsha', 117225),
                        'braslaw':City('Braslaw', 9516)}
regions_of_belarus = {'minsk_region': Region('Minsk Region', 1411500, minsk_region_cities),
                      'vitebsk_region': Region('Vitebsk Region', 1221800, viebsk_region_cities)}
my_countries = {'belarus': Country('Belarus', 'Minsk', 10000000, regions_of_belarus)}


@app.route('/countries/<country>', strict_slashes=False)
def country_info(country):
    result = my_countries[country]
    return jsonify(result)


@app.route('/countries/', strict_slashes=False)
def countries():
    all_countries = []
    for country in my_countries:
        all_countries.append(my_countries[country].name)
    return jsonify(all_countries)


@app.route('/countries/<country>/regions/', strict_slashes=False)
def regions(country):
    all_regions = []
    for region in my_countries[country].regions.values():
        all_regions.append(region.name)
    return jsonify(all_regions)


@app.route('/countries/<country>/regions/<region>', strict_slashes=False)
def region_info(country, region):
    result = my_countries[country].regions[region]
    return jsonify(result)


@app.route('/countries/<country>/regions/<region>/cities', strict_slashes=False)
def cities(country, region):
    all_cities = []
    for city in my_countries[country].regions[region].cities.values():
        all_cities.append(city.name)
    return jsonify(all_cities)


@app.route('/countries/<country>/regions/<region>/cities/<city>', strict_slashes=False)
def city_info(country, region, city):
    city_you_need = my_countries[country].regions[region].cities[city]
    return jsonify(city_you_need)

app.run('localhost', '8080')