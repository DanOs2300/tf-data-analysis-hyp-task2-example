import pandas as pd
import numpy as np


chat_id = 630197911 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    from hyppo.ksample import MMD
    
    res = MMD(compute_kernel='rbf', gamma=1.0).test(x, y)
    if res[1] < 0.03:
        bool_final = True
    else:
        bool_final = False
    return bool_final
