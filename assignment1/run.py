import pandas as pd
import matplotlib.pyplot as plt
import os

class DataSet:

    def __init__(self, dataset_name):
        self.dataset_name = dataset_name
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

    def import_dataset(self):
        dataset_type = self.datasets[self.dataset_name]['type']
        if dataset_type == 'csv':
            return pd.read_csv(self.datasets[self.dataset_name]['file_location'])
        else:
            raise Exception("Filetype not supported.")

    def dataset_size(self):
        return len(self.data_frame.index)


class Regression:

    def __init__(self, dataset):
        self.dataset = dataset
        self.s = 0
        self.sx = 0
        self.sy = 0
        self.sxx = 0
        self.syy = 0

    def calculate(self):
        for data_row in self.dataset.data_frame.itertuples():
            self.s += 1. /
            print(data_row)
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






dataset = DataSet('barrow')
reg = Regression(dataset)
reg.calculate()