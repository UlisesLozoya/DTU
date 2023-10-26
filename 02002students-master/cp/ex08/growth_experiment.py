"""Exercise 8.9: Bacteria Growth experiment."""
import csv

import matplotlib.pyplot as plt


def growth_threshold_reached(path: str, threshold: float) -> float:
    """Return the time point at which the growth threshold is reached.
    
    :param path: The path to the folder of the data files.
    :param threshold: The threshold value.
    
    :return: The average time point.
    """
    # TODO: Code has been removed from here. 


if __name__ == "__main__":
    for i in range(160):
        with open(f'files/experiments/experiment_{i:03d}.csv', 'r') as f:
            reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
            row = next(csvreader)
            plt.plot(row)
    plt.show()
