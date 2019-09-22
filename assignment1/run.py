import pandas as pd
import matplotlib.pyplot as plt
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

    def set_timestamps_in_dataset(self):
        self.data_frame['timestamp'] = \
            self.data_frame.apply(lambda row: self.initial_timestamp+datetime.timedelta(days = row.name*14), axis = 1)

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
        for data_row in self.dataset.data_frame.itertuples():
        #    self.s += 1. /
            print(data_row)

    def print_plot(self):
        plt.plot(self.dataset.data_frame.timestamp, self.dataset.data_frame.co2_measure)
        plt.xlabel(r'Year')
        plt.ylabel(r'$CO_2$ [ppm]')
        plt.show()
    # for (i = 0;i<data;i++) {
    #   s   +=         1. / (d[i]*d[i]);
    #   sx  +=       x[i] / (d[i]*d[i]);
    #   sy  +=       y[i] / (d[i]*d[i]);
    #   sxx +=  x[i]*x[i] / (d[i]*d[i]);
    #   sxy +=  x[i]*y[i] / (d[i]*d[i]);
    # }
    # delta  =  s*sxx - sx*sx;
    # slope =   (s*sxy - sx*sy) / delta;
    # inter = (sxx*sy - sx*sxy) / delta;
    # System.out.println("intercpt= "+inter+", "+Math.sqrt(sxx/delta));
    # System.out.println("slope =  "+slope+" , "+Math.sqrt(s/delta));
    # System.out.println("Fit Program Complete.");


# # Mean X and Y
# mean_x = np.mean(X)
# mean_y = np.mean(Y)
#
# # Total number of values
# n = len(X)
#
# # Using the formula to calculate m and c
# numer = 0
# denom = 0
# for i in range(n):
#     numer += (X[i] - mean_x) * (Y[i] - mean_y)
# denom += (X[i] - mean_x) ** 2
# m = numer / denom
# c = mean_y - (m * mean_x)
#
# # Print coefficients
# print(m, c)





dataset = DataSet('barrow')
dataset.set_timestamps_in_dataset()
dataset.set_column_header()
reg = Regression(dataset)

#reg.calculate()
reg.print_plot()