import numpy as np
import pandas as pd

data = pd.read_csv('state_wise_daily.csv')
data = pd.DataFrame(data[1::3])

data.to_csv("recovered.csv", index=False)
