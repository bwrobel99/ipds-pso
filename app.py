from flask import Flask
from .elements.solver import Solver
from .elements.graph import Graph
import json 

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/calculate')
def calculate():
    lst_of_points = [[19.9320, 50.0580],
                     [19.9431, 50.0590], [19.9270, 50.0632],
                     [19.9370, 50.0600]]
    restaurant_loc = [19.9383, 50.0634]
    petrol_loactions = [[19.9380, 50.0578], [19.9500, 50.0643], [19.9499, 50.0599]]
    s = Solver(100, 100, lst_of_points, restaurant_loc, petrol_loactions)
    s.solve()
    right_order = s.gBest
    graph = Graph()
    longitudes , latitudes = graph.upgrade_points(restaurant_loc=restaurant_loc, right_order=right_order, lst_of_points=lst_of_points, petrol_loactions=petrol_loactions)
    graph.show_graph(longitudes=longitudes, latitudes=latitudes, petrol_locations=petrol_loactions, restaurant_loc=restaurant_loc, lst_of_points=lst_of_points)
    return json.dumps({"result": s.gBest, "cost": s.gBest_cost})
