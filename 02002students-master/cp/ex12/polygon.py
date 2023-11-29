"""Exercises 12.2-12.4.: Polygon."""

import matplotlib.pyplot as plt
import numpy as np
import math


class Polygon:
    """A class to represent a polygon."""

    def __init__(self, points: list):
        x_array = np.empty(0)
        for i in range(len(points)):
            x = points[i][0]
            x_array = np.append(x_array, x)
        self.x = x_array
        y_array = np.empty(0)
        for i in range(len(points)):
            y = points[i][1]
            y_array = np.append(y_array, y)
        self.y = y_array

    def plot_polygon(self):
        x = self.x
        x_plot = np.append(x, x[0])
        y = self.y
        y_plot = np.append(y, y[0])
        plt.plot(x_plot, y_plot, 'k.-')
        plt.show()

    def get_area(self):
        A_2 = np.roll(self.x, -1)
        B_2 = np.roll(self.y, -1)
        area_1 = 0
        for i in range(len(self.x)):
            area_1 = self.x[i] * B_2[i] + area_1
        area_2 = 0
        for i in range(len(self.x)):
            area_2 = self.y[i] * A_2[i] + area_2
        total = (area_1 - area_2) / 2
        return abs(total)

    def get_perimeter(self):
        d = 0
        for i in range(len(self.x) - 1):
            d1 = abs((self.x[i] - self.x[i + 1]) ** 2)
            d2 = abs((self.y[i] - self.y[i + 1]) ** 2)
            d3 = math.sqrt(d1 + d2)
            d = d3 + d
        d001 = abs((self.x[len(self.x) - 1] - self.x[0]) ** 2 + (self.y[len(self.y) - 1] - self.y[0]) ** 2)
        d01 = math.sqrt(d001)
        return d + d01

    def smooth_polygon(self, alpha):
        x0new = 0
        y0new = 0
        xarray = np.empty(0)
        yarray = np.empty(0)

        for i in range(len(self.x)):
            if i == 0:
                x0new = (1 - alpha) * self.x[i] + (0.5 * alpha * (self.x[len(self.x) - 1] + self.x[i + 1]))
                y0new = (1 - alpha) * self.y[i] + (0.5 * alpha * (self.y[len(self.y) - 1] + self.y[i + 1]))
            elif i == len(self.x) - 1:
                self.x[i] = (1 - alpha) * self.x[i] + (0.5 * alpha * (self.x[i - 1] + self.x[0]))
                self.y[i] = (1 - alpha) * self.y[i] + (0.5 * alpha * (self.y[i - 1] + self.y[0]))
            else:
                a = (1 - alpha) * self.x[i] + (0.5 * alpha * (self.x[i - 1] + self.x[i + 1]))
                b = (1 - alpha) * self.y[i] + (0.5 * alpha * (self.y[i - 1] + self.y[i + 1]))
                yarray = np.append(yarray, b)
                xarray = np.append(xarray, a)

        self.x[0] = x0new
        self.y[0] = y0new
        for i in range(len(self.x) - 1):
            if not i == 0:
                self.x[i] = xarray[i-1]
                self.y[i] = yarray[i-1]
        return self


if __name__ == "__main__":
    P = Polygon([(1, 2), (2, 3), (3, 4), (4, 5), (3, 2), (2, 2.5)])
    P.smooth_polygon(alpha=0.2)
    print(P.x)
    print(P.y)
    # P.plot_polygon()
    # print(P.get_area())
    # P = Polygon([(24, 12), (40, 16), (36, 8), (44, 4), (28, 0), (18, 4), (12, 0), (0, 4), (8, 12), (4, 16)])
    # P.plot_polygon()
    # P.smooth_polygon(0.5)
    # P.plot_polygon()
