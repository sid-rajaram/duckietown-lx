from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    res[160:, :320] = np.ones((320,1))*np.linspace(0.05,1,320)[np.newaxis,:]
    # res[160:, 320:] = np.ones((320,1))*np.linspace(-1,-0.05,320)[np.newaxis,:]
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    # res[160:, :320] = np.ones((320,1))*np.linspace(-0.05,-1,320)[np.newaxis,:]
    res[160:, 320:] = np.ones((320,1))*np.linspace(1,0.05,320)[np.newaxis,:]
    return res
