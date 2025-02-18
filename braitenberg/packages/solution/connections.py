from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    # res[160:, :320] = np.ones((320,1))*np.linspace(0,1,320)[np.newaxis,:]
    res[160:, 320:] = np.ones((320,1))*np.linspace(-1,0,320)[np.newaxis,:]
    # res[400:, :80] = 1.0
    # res[400:, 560:] = -1.0
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    res[160:, :320] = np.ones((320,1))*np.linspace(0,-1,320)[np.newaxis,:]
    # res[160:, 320:] = np.ones((320,1))*np.linspace(1,0,320)[np.newaxis,:]
    # res[400:, :80] = -1.0
    # res[400:, 560:] = 1.0
    return res