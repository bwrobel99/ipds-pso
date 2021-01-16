import os
from matplotlib import pyplot as plt

class Graph:
    def __init__(self):
        self.dct = {}
        self.bbox = []
        self.maps_directory = "./maps"
        self.trace_directory = "./traces"
        f = open(os.path.join(self.maps_directory, 'uno_coor.txt'), "r")
        splitted = f.read().split(' ')
        for elem in range(0, len(splitted)-1, 2):
            self.dct[splitted[elem]] = float(splitted[elem + 1])

        for value in self.dct.values():
            self.bbox.append(value)

    def upgrade_points(self, restaurant_loc, right_order, lst_of_points, petrol_loactions):
        ordered_points = []
        for order in right_order:
            if order >= 10:
                ordered_points.append(petrol_loactions[order - 10])
            else:
                ordered_points.append(lst_of_points[order - 1])
        ordered_points.append(restaurant_loc)
        ordered_points.insert(0, restaurant_loc)

        longitudes = []
        latitudes = []
        for coor in ordered_points:
            longitudes.append(coor[0])
            latitudes.append(coor[1])

        return longitudes, latitudes

    def show_graph(self, longitudes, latitudes, petrol_locations, restaurant_loc, lst_of_points):
        map = plt.imread(os.path.join(self.maps_directory, 'uno.png'))
        fig, ax = plt.subplots(figsize=(8, 7))
        petrol_long = []
        petrol_lat = []
        points_long = []
        points_lat = []
        for i in lst_of_points:
            points_long.append(i[0])
            points_lat.append(i[1])

        for i in petrol_locations:
            petrol_long.append(i[0])
            petrol_lat.append(i[1])


        ax.plot(longitudes, latitudes, zorder=1, alpha=0.8, ls='--', c='r')
        for i in range(len(longitudes) - 1):
            if i == 0:
                ax.annotate('Pozycja restauracji', xy=(longitudes[i], latitudes[i]))
            else:
                ax.annotate(f'#{i}', xy=(longitudes[i], latitudes[i]))

        ax.set_title('Trasa Pana Kierowcy')
        ax.set_xlim(self.bbox[0], self.bbox[1])
        ax.set_ylim(self.bbox[2], self.bbox[3])

        ax.scatter(petrol_long, petrol_lat, zorder=1, alpha=1, c='y', s=30, marker='D')
        ax.scatter(points_long, points_lat, zorder=1, alpha=0.8, c='r', s=30, marker = 'o')
        ax.scatter(restaurant_loc[0], restaurant_loc[1], zorder = 1, alpha = 1, c='b', s=30, marker = 's')
        for i in range(len(petrol_long)):
            ax.annotate(f'SB{i}', xy=(petrol_long[i], petrol_lat[i]))

        ax.imshow(map, zorder=0, extent=self.bbox, aspect='equal')
        plt.show()
        fig.savefig(os.path.join(self.trace_directory, 'trace1.png'))
