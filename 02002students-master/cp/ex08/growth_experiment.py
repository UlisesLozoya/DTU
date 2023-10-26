"""Exercise 8.9: Bacteria Growth experiment."""
import csv

import matplotlib.pyplot as plt


def growth_threshold_reached(path: str, threshold: float) -> float:
    """Return the time point at which the growth threshold is reached.
    
    :param path: The path to the folder of the data files.
    :param threshold: The threshold value.
    
    :return: The average time point.
    """
    # C:\Users\Ulises\Desktop\02002students\02002students-master\cp\ex08\files\experiments
    avg_time = 0
    for i in range(160):
        with open(
                f'C:/Users/Ulises/Desktop/02002students/02002students-master/cp/ex08/files/experiments/experiment_{i:03d}.csv',
                'r') as f:
            data = f.read()
            data = data.replace("\n", "")
            data = data.split(',')
            t = 0
            while t in range(len(data) - 1):
                t += 1
                if float(data[t]) > threshold:
                    second = t
                    t = 1000
            if i == 0:
                avg_time = second
            else:
                avg_time = (avg_time + second)
    return avg_time/160


if __name__ == "__main__":
    # for i in range(160):
    #    with open(f'files/experiments/experiment_{i:03d}.csv', 'r') as f:
    #        reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    #        row = next(reader)
    #        plt.plot(row)
    # plt.show()
    print((growth_threshold_reached("files/experiments", 8.5)))
