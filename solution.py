import pandas as pd
import numpy as np


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    from scipy.stats import ks_2samp
    if len(x) == 0 or len(y) == 0:
        return False
    
    stat, p_value = ks_2samp(x, y)
    
    alpha = 0.05
    
    if p_value < alpha:
        return False
    
    return True
