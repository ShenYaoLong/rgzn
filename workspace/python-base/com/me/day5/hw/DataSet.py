import sys

import numpy
from sklearn import svm


class DataSet:
    def __init__(self, name):
        self.target = []
        self.data = []
        self.name = name

    def load_data(self):
        with open('pima-indians-diabetes.txt', 'r') as f:
            for i in f:
                l = list(map(float, i[:-1].split(',')))
                self.data.append(l[:-2])
                self.target.append(l[-1:])

    def generate_xy(self):
        self.load_data()
        x = self.data
        y = self.target
        print('\nOriginal data looks like this: \n', x)
        print('\nLabels looks like this: \n', y)
        return x, y

    def get_train_test_set(self, ratio):
        x, y = self.generate_xy()
        n_samples = len(x)
        n_train = int(n_samples * ratio)
        x_train = x[:n_train]   # x训练集
        y_train = y[:n_train]   # y训练集
        x_test = x[n_train:]    # x结果集
        y_test = y[n_train:]    # y结果集
        return x_train, y_train, x_test, y_test


def main():
    data = DataSet('digits')
    x_y = data.get_train_test_set(0.7)  # 获取数据集
    clf = svm.SVC()                     # 使用SVC作为分类器
    clf.fit(x_y[0], x_y[1])
    test_point = x_y[2][4]
    y_true = x_y[3][4]
    print(clf.predict(numpy.array(test_point).reshape(1, -1)))   # fit 训练数据，通过predict查看训练结果
    print(y_true)   # 真实结果


if __name__ == "__main__":
    sys.exit(main())
