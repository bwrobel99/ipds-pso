from flask import Flask, request
from flask_cors import CORS
from elements.solver import Solver
from elements.graph import Graph
import numpy as np
import json 

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/calculate', methods=['POST'])
def calculate():
    data = json.loads(request.data)
    lst_of_points = data['places'][1:]
    restaurant_loc = data['places'][0]
    fuel_level = data['petrol']
    petrol_locations = [[50.06, 19.92]]
    s = Solver(25, 25, fuel_level, lst_of_points, restaurant_loc)
    delivery_time, pizza_temperature, used_fuel = s.solve()
    return json.dumps({"delivery_time": delivery_time, "pizza_temperature": pizza_temperature, 
    "used_fuel": used_fuel, "order": s.gBest, "km": np.around(s.gBest_cost,2), "petrol_locations": s.petrol_locations})
