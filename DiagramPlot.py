
class DiagramPlot:
    def __init__(self, canv=None):
        self.canvas = canv
        # hide axes and borders
        self.canvas.axis('off')

    def draw_roots(self, data_rs,  color='red', ):
        self.canvas.quiver(data_rs[0], data_rs[1], data_rs[2], data_rs[3],
                           color=color, scale_units='inches', scale=1)

    def draw_points(self, points):
        for point in points:
            self.canvas.scatter(point[0], point[1], color='black', marker='.')
