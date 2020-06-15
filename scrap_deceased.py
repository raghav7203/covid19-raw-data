import numpy as np
import pandas as pd

data = pd.read_csv('state_wise_daily.csv')
data = pd.DataFrame(data[2::3])

data.to_csv("deceased.csv", index=False)
