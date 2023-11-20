"""Exercise 11.7-11.8: Bacterial growth."""

import numpy as np
import matplotlib.pyplot as plt


def load_data() -> np.ndarray:
    """Load data from 160 files into one array. Files are located in cp/ex11/files/experiments.
    
    :return: The data from the files in one array.
    """
    data = np.empty((160, 12), float)
    for i in range(160):
        with open(
                f'C:/Users/Ulises/Desktop/02002students/02002students-master/cp/ex08/files/experiments/experiment_{i:03d}.csv',
                'r') as f:
            data1 = np.loadtxt(f, delimiter=',')
            data[i] = data1
    return data


def threshold_exceeded(data: np.ndarray, threshold: float) -> np.ndarray:
    """Return the index at which the threshold is exceeded for each experiment.
    
    :param data: The data to search.
    :param threshold: The threshold to compare against.
    :return: The index at which the threshold is exceeded for each row.
    """
    time = np.empty(160, float)
    for i in range(160):
        time[i] = np.argmax(data[i] > threshold)
    return time


def get_mean(data: np.ndarray) -> np.ndarray:
    """Calculate the mean of the data.
    
    :param data: The data to calculate the mean of.
    :return: The mean of the data for each time-point.
    """

    return data.mean(0)


def get_std(data: np.ndarray) -> np.ndarray:
    """Calculate the standard deviation of the data.
    
    :param data: The data to calculate the standard deviation of.
    :return: The standard deviation of the data for each time-point.
    """

    return data.std(0)


if __name__ == '__main__':
    # print(load_data())
    data = load_data()
    # print(threshold_exceeded(data2, 8.5))
    # data = load_data()
    # data = np.ones((4, 4))
    # data[::2] = 2
    mean = get_mean(data)
    print(mean)
    std = get_std(data)
    plt.plot(mean)
    plt.plot(mean - std, 'm', mean + std, 'm')
    plt.legend(['Mean', 'Std'])
    plt.show()
