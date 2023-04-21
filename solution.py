import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp

chat_id = 630197911 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    p_value = anderson_ksamp([x, y]).pvalue
    return p_value < 0.04
