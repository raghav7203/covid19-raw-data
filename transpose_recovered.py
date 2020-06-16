import pandas as pd
pd.read_csv('recovered.csv', header=None).T.to_csv('recoveredT.csv', header=False, index=False)
