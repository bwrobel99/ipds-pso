from flask import Flask, request
from flask_cors import CORS
from .elements.solver import Solver
from .elements.graph import Graph
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
    petrol_loactions = [[19.9380, 50.0578], [19.9500, 50.0643], [19.9499, 50.0599]]
    s = Solver(25, 25, 5.5, lst_of_points, restaurant_loc, petrol_loactions)
    delivery_time, pizza_temperature, used_fuel = s.solve()
    # print(f"Kolejność dostawy pizzy: {s.gBest}")
    # print(f"Czas dostawy [min]: {delivery_time}")
    # print(f"Temperatura pizzy [st.C]: {pizza_temperature}")
    # print(f"Długość trasy [km]: {np.around(s.gBest_cost,2)}")
    # print(f"Zużyte paliwo: {used_fuel}")
    right_order = s.gBest
    # graph = Graph()
    # longitudes , latitudes = graph.upgrade_points(restaurant_loc=restaurant_loc, right_order=right_order, lst_of_points=lst_of_points, petrol_loactions=petrol_loactions)
    # graph.show_graph(longitudes=longitudes, latitudes=latitudes, petrol_locations=petrol_loactions, restaurant_loc=restaurant_loc, lst_of_points=lst_of_points)
    return json.dumps({"result": s.gBest, "cost": s.gBest_cost})
