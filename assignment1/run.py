import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import datetime

class DataSet:

    def __init__(self, dataset_name):
        self.dataset_name = dataset_name
        self.initial_timestamp = datetime.datetime.strptime("1981-01-01", "%Y-%m-%d")
        self.column_header = ['co2_measure', 'timestamp']
        self.script_path = os.path.dirname(os.path.abspath(__file__))
        self.data_path = os.path.join(self.script_path, 'data')
        self.datasets = {}
        self.y_vec =[]
        self.datasets['barrow'] = {
            "file_location": os.path.join(self.data_path, 'Barrow.dat'),
            "type": "csv"
        }

        self.datasets['mauna'] = {
            "file_location": os.path.join(self.data_path, 'Mauna.dat'),
            "type": "csv"
        }

        self.check_dataset_name(dataset_name)
        self.data_frame = self.import_dataset()

    def check_dataset_name(self, dataset_name):
        if not self.datasets[dataset_name]:
            raise Exception("Dataset not found!")

    #def set_timestamps_in_dataset(self):
    #    self.data_frame['timestamp'] = \
    #        self.data_frame.apply(lambda row: self.initial_timestamp+datetime.timedelta(days = row.name*14), axis = 1)

    def set_timestamps_in_dataset(self):
        self.data_frame['timestamp'] = \
            self.data_frame.apply(lambda row: row.name, axis = 1)

    def set_column_header(self):
        self.data_frame.columns = self.column_header

    def import_dataset(self):
        dataset_type = self.datasets[self.dataset_name]['type']
        if dataset_type == 'csv':
            return pd.read_csv(self.datasets[self.dataset_name]['file_location'])
        else:
            raise Exception("Filetype not supported.")

    def head_dataset(self, num = 5):
        return self.data_frame.head(num)

    def dataset_size(self):
        return len(self.data_frame.index)


class Regression:

    def __init__(self, dataset):
        self.dataset = dataset
        self.sxx = 0
        self.syy = 0
        self.beta0 = 0
        self.beta1 = 0

    def calculate(self):
        sum_x = 0
        sum_xx = 0
        sum_y = 0
        sum_xy = 0

        for data_row in self.dataset.data_frame.itertuples():
            sum_x = sum_x + data_row.timestamp
            sum_xx = sum_xx + data_row.timestamp**2
            sum_y = sum_y + data_row.co2_measure
            sum_xy = sum_xy + data_row.co2_measure * data_row.timestamp

        delta = sum_x * sum_x - 229 * sum_xx
        m = (sum_y * sum_x - 229 * sum_xy) / delta
        b = (sum_x * sum_xy - sum_y * sum_xx) / delta

        y_vec = []
        for data_row in self.dataset.data_frame.itertuples():
            y_vec.append( m*data_row.timestamp + b)

        self.y_vec = y_vec

    def print_plot(self):
        print("change = {}".format((self.y_vec[24] - self.y_vec[0])/1))
        plt.axes(title='Waves on a string with fixed ends', xlim=(0, 300), ylim=(335, 365))
        plt.plot(self.dataset.data_frame.timestamp, self.dataset.data_frame.co2_measure, '.')
        plt.plot(self.dataset.data_frame.timestamp, self.y_vec)
        plt.xlabel(r'Year')
        plt.ylabel(r'$CO_2$ [ppm]')
        plt.show()

#dataset = DataSet('barrow')
dataset = DataSet('mauna')
dataset.set_timestamps_in_dataset()
dataset.set_column_header()
reg = Regression(dataset)
reg.calculate()
reg.print_plot()
