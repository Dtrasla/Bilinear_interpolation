from PIL import Image
import numpy as np
from numpy import asarray


def bilinear(old_array, new_scale):
    old_height, old_width = old_array.shape
    new_height = old_height * new_scale
    new_width = old_width * new_scale
    new_array = np.zeros((new_height, new_width)).astype(int)
    for i in range(old_height - 1):
        for j in range(old_width - 1):
            new_array = interpolateHorizontal(new_array, i, j, new_scale, old_array)
            new_array = interpolateVertical(new_array, i, j, new_scale, old_array)

    for i in range(old_height - 1):
        for j in range(old_width - 1):
            new_array = interpolateSubgrid(new_array, i, j, new_scale)

    return new_array


def interpolateHorizontal(new_array, i, j, new_scale, old_array):
    x0Distance = 0
    x1Distance = new_scale
    for k in range(new_scale):
        weightedAverage = ((1 - (x0Distance / new_scale)) * old_array[i][j]) + (
                    (1 - (x1Distance / new_scale)) * old_array[i][j + 1])
        new_array[i * new_scale][(j * new_scale) + k] = int(weightedAverage)
        x0Distance += 1
        x1Distance -= 1
    return new_array


def interpolateVertical(new_array, i, j, new_scale, old_array):
    x0Distance = 0
    x1Distance = new_scale
    for k in range(new_scale):
        weightedAverage = ((1 - (x0Distance / new_scale)) * old_array[i][j]) + (
                    (1 - (x1Distance / new_scale)) * old_array[i + 1][j])
        new_array[(i * new_scale) + k][(j * new_scale)] = int(weightedAverage)
        x0Distance += 1
        x1Distance -= 1
    return new_array


# Called after calculating horizontal and vertical lines to interpolate inner grid by bilinear
def interpolateSubgrid(new_array, i, j, new_scale):
    x0Distance = 0
    x1Distance = new_scale
    for k in range(new_scale):
        for l in range(new_scale):
            weightedAverage = ((1 - (x0Distance / new_scale)) * new_array[i * new_scale][j * new_scale]) + (
                        (1 - (x1Distance / new_scale)) * new_array[(i + 1) * new_scale][j * new_scale])
            new_array[(i * new_scale) + k][(j * new_scale) + l] = int(weightedAverage)
        x0Distance += 1
        x1Distance -= 1
    return new_array


image = Image.open("test.png")
image = image.convert("L")

array = asarray(image)

new_array = bilinear(array, 3)

print(new_array.shape)

new_image = Image.fromarray(new_array)
new_image = new_image.convert("L")
# new_image.save("assets/result.png")
new_image.show()
