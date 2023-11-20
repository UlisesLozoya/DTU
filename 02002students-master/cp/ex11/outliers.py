"""Exercise 11.9: Outliers."""
import numpy as np

from cp.ex11.bacterial_growth import get_mean, get_std, load_data


def outliers(data: np.ndarray) -> np.ndarray:
    """Return the outliers of a dataset.
    
    :param data: The data to search.
    :return: The outliers of the data.
    """
    nrows = np.shape(data)[0]
    ncols = np.shape(data)[1]
    mean = get_mean(data)
    std = get_std(data)
    outliers = np.empty(0)
    for i in range(nrows):
        value = float(data[i, (ncols-1)])
        outlying = mean[ncols-1] + (2 * std[ncols-1])
        if value > outlying:
            outliers = np.append(outliers, i)
    return outliers


if __name__ == '__main__':
    np.random.seed(43)
    data = (np.random.rand(160, 20) * 2) ** 2
    print(outliers(data))
