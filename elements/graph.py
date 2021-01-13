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

    def upgrade_points(self, restaurant_loc, right_order, lst_of_points):
        ordered_points = []
        for order in right_order:
            if order == right_order[0]:
                ordered_points.append(restaurant_loc)
            for index, point in enumerate(lst_of_points):
                if order == (index + 1):
                    ordered_points.append(point)
                    if order == right_order[-1]:
                        ordered_points.append(restaurant_loc)

        longitudes = []
        latitudes = []
        for coor in ordered_points:
            longitudes.append(coor[0])
            latitudes.append(coor[1])

        return longitudes, latitudes

    def show_graph(self, longitudes, latitudes):
        map = plt.imread(os.path.join(self.maps_directory, 'uno.png'))
        fig, ax = plt.subplots(figsize=(8, 7))
        # ax.scatter(longitudes,latitudes, zorder = 1, alpha = 0.8, c='r', s=10)
        # ax.scatter(petrol_longitudes, petrol_latitudes, zorder=1, alpha=1, c='y', s=30, marker = 'D')
        # ax.scatter(restaurant_loc[0], restaurant_loc[1], zorder = 1, alpha = 1, c='b', s=30, marker = 's')
        ax.plot(longitudes, latitudes, zorder=1, alpha=0.8, ls='--', c='r', marker='D')
        for i in range(len(longitudes) - 1):
            if i == 0:
                ax.annotate('Pozycja restauracji', xy=(longitudes[i], latitudes[i]))
            else:
                ax.annotate(f'#{i}', xy=(longitudes[i], latitudes[i]))

        ax.set_title('Trasa Pana Kierowcy')
        ax.set_xlim(self.bbox[0], self.bbox[1])
        ax.set_ylim(self.bbox[2], self.bbox[3])

        ax.imshow(map, zorder=0, extent=self.bbox, aspect='equal')
        plt.show()
        fig.savefig(os.path.join(self.trace_directory, 'trace1.png'))


    def get_cost_matrix(self):
        pass
