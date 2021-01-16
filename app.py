from flask import Flask, request
from flask_cors import CORS
from .elements.solver import Solver
from .elements.graph import Graph
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
    petrol_locations = [[50.06, 19.92]]
    s = Solver(25, 25, 5.5, lst_of_points, restaurant_loc, petrol_locations)
    delivery_time, pizza_temperature, used_fuel = s.solve()
    # print(f"Kolejność dostawy pizzy: {s.gBest}")
    # print(f"Czas dostawy [min]: {delivery_time}")
    # print(f"Temperatura pizzy [st.C]: {pizza_temperature}")
    # print(f"Długość trasy [km]: {np.around(s.gBest_cost,2)}")
    # print(f"Zużyte paliwo: {used_fuel}")
    return json.dumps({"delivery_time": delivery_time, "pizza_temperature": pizza_temperature, 
    "used_fuel": used_fuel, "order": s.gBest, "km": np.around(s.gBest_cost,2), "petrol_locations": petrol_locations})
