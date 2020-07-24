#!/usr/bin/env python
import os
import requests
import json, operator
import postcodes_io_api
from pprint import pprint
from flask import Flask, render_template


app = Flask(__name__)


API = postcodes_io_api.Api(debug_http=True)


# Helper Functions
def get_lat_long(postcodes):
  pc_data = API.get_bulk_postcodes(postcodes)
  ret = dict()
  #print(pc_data)
  for data in pc_data["result"]:
    d = data.get("result", {})   
    if d:
      ret[d.get("postcode", None)] = {
           "longitude": d.get("longitude", None),
           "latitude": d.get("latitude", None)
      }
  return ret


def get_nearest_postcodes(postcodes):
  ret = dict()
  to_file = dict()
  for postcode in postcodes:
    result = API.get_nearest_postcodes_for_postcode(postcode=postcode, 
                                                            limit=10,
                                                          radius=2000)
    ret[postcode] = list()
    to_file[postcode] = list()
    # print(result)
    for res in result.get("result", dict()):
      if res["distance"] > 0:
        ret[postcode].append((res["postcode"], res["distance"]))
        to_file[postcode].append({"postcode": res["postcode"], "distance": res["distance"]})
    with open("./data/nearest.json", "w") as file:
      file.write(json.dumps(to_file))
  # pprint(ret)
  return ret


# Index Route
@app.route("/")
def index():
    return "I am Monsieur Poirot. 🐶 Welcome to Tails. Woof!"


# Stores
@app.route('/stores', methods=['GET'])
def getStores():
    with app.open_resource('data/stores.json') as f:     
        data = json.load(f)
        data.sort(key=operator.itemgetter('name'))
        lat_longs = get_lat_long([d["postcode"] for d in data])
        nearest = get_nearest_postcodes([d["postcode"] for d in data])
        for d in data:
          if d["postcode"] in lat_longs: 
            d["longitude"] = lat_longs[d["postcode"]]["longitude"]
            d["latitude"] = lat_longs[d["postcode"]]["latitude"]
          if d["postcode"] in nearest:
            d["nearest"] = nearest[d["postcode"]] 
    stores = data
    return render_template('frontend/stores.html', stores=stores)



if __name__ == '__main__':
    app.run(debug=True)
