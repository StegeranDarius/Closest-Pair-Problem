
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import time

from numpy.core.defchararray import isdigit

import pairgenerator
from closestpair import closest_pair_of_points


class Plotter(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.closest_points = None
        self.points = []

        self.figure, self.ax = plt.subplots()

        self.canvas = FigureCanvas(self.figure)

        self.add_custom_point_button = QtWidgets.QPushButton('Add Custom Point')
        self.add_custom_point_button.clicked.connect(self.add_point)

        self.add_point_button = QtWidgets.QPushButton('Add Points')
        self.add_point_button.clicked.connect(self.add_points)

        self.find_closest_pair_button = QtWidgets.QPushButton('Find Smallest Pair')
        self.find_closest_pair_button.clicked.connect(self.find_closest_pair)

        self.clear_plot_button = QtWidgets.QPushButton('Clear Plot')
        self.clear_plot_button.clicked.connect(self.clear_plot)

        self.closest_points_label = QtWidgets.QLabel("")
        self.closest_points_label.setAlignment(QtCore.Qt.AlignTop)

        self.min_value_label = QtWidgets.QLabel("(int) Minimum Value:")
        self.min_value_edit = QtWidgets.QLineEdit()

        self.max_value_label = QtWidgets.QLabel("(int) Maximum Value:")
        self.max_value_edit = QtWidgets.QLineEdit()

        self.num_points_label = QtWidgets.QLabel("(int) Number of Points:")
        self.num_points_edit = QtWidgets.QLineEdit()

        input_form_layout = QtWidgets.QFormLayout()
        input_form_layout.addRow(self.min_value_label, self.min_value_edit)
        input_form_layout.addRow(self.max_value_label, self.max_value_edit)
        input_form_layout.addRow(self.num_points_label, self.num_points_edit)
        input_form_layout.addWidget(self.add_point_button)

        layout = QtWidgets.QHBoxLayout()
        canvas_layout = QtWidgets.QVBoxLayout()
        canvas_layout.addWidget(self.canvas)
        layout.addLayout(canvas_layout)

        right_layout_widget = QtWidgets.QWidget()
        right_layout_widget.setFixedSize(int(self.width() / 2), self.height())
        right_layout = QtWidgets.QVBoxLayout(right_layout_widget)

        right_layout.addLayout(input_form_layout)
        right_layout.addWidget(self.clear_plot_button)
        right_layout.addWidget(self.add_custom_point_button)
        right_layout.addWidget(self.find_closest_pair_button)
        right_layout.addWidget(self.closest_points_label)

        layout.addWidget(right_layout_widget)
        self.setLayout(layout)

    def add_points(self):
        min_value = int(self.min_value_edit.text())
        max_value = int(self.max_value_edit.text())
        number_of_points = int(self.num_points_edit.text())
        self.points = list(pairgenerator.generate(min_value, max_value, number_of_points))
        self.ax.set_xlim(min_value, max_value)
        self.ax.set_ylim(min_value, max_value)
        self.populate_points()

    def find_closest_pair(self):
        start_time = time.time()
        self.closest_points = list(closest_pair_of_points(self.points, self.points.__len__()))
        end_time = time.time()
        self.change_points_color()
        distance = self.closest_points[0]
        points = self.closest_points[1]
        formatted_points = ', '.join(['({:.2f}, {:.2f})'.format(x[0], x[1]) for x in points])
        output = "Found!!!\n" \
                 "Distance {:.5f}\n" \
                 "Points = {}\n" \
                 "In time: {}".format(distance, formatted_points, end_time - start_time)

        self.closest_points_label.setText(output)

    def add_point(self):
        point, ok = QtWidgets.QInputDialog.getText(self, 'Add Point', 'Enter x,y coordinates of point:')
        if ok:
            x, y = point.split(',')
            x, y = float(x), float(y)
            self.points += [(x, y)]
            self.populate_points()

    def populate_points(self):
        self.ax.clear()
        for pair in self.points:
            self.ax.scatter(pair[0], pair[1], color='blue')
        self.canvas.draw()
        QtWidgets.QApplication.processEvents()

    def change_points_color(self):
        self.ax.clear()
        for point in self.points:
            if point in self.closest_points[1]:
                self.ax.scatter(point[0], point[1], color='red')
            else:
                self.ax.scatter(point[0], point[1], color='blue')
        self.canvas.draw()

    def clear_plot(self):
        self.ax.clear()
        self.points = []
        self.canvas.draw()
