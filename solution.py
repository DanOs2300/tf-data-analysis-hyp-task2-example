import pandas as pd
import numpy as np


chat_id = 630197911 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    
    res = cramervonmises_2samp(x, y)
    
    return res.pvalue < 0.03
