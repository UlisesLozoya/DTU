"""Exercise 11.10: Bacterial area."""
import numpy as np
import matplotlib.pyplot as plt


def bacterial_area(npy_path: str) -> float:
    """Calculate the percentage of the image where pixel intensities are greater than 100.

    Parameters:
    :param npy_path: Path to the image data file in NumPy format.
    :return: The percentage of area in an image where there are bacteria.
    """
    img = np.load('C:/Users/Ulises/Desktop/02002students/02002students-master/cp/ex11/files/bacteria.npy')
    rows = np.shape(img)[0]
    cols = np.shape(img)[1]
    pixels = np.ones((rows, cols))
    for i in range(rows):
        for j in range(cols):
            if img[i, j] > 100:
                pixels[i, j] = 1
            else:
                pixels[i, j] = 0
    pixel_mean = np.mean(pixels)
    return pixel_mean


if __name__ == '__main__':
    image_path = 'files/bacteria.npy'
    print(bacterial_area(image_path))
    img = np.load(image_path)
    plt.imshow(img, cmap='gray')  # Display image
    plt.show()
