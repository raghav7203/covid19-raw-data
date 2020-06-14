import numpy as np
import pandas as pd

data = pd.read_csv('state_wise_daily.csv')
data = pd.DataFrame(data[::3])

data.to_csv("confirmed.csv", index=False)
