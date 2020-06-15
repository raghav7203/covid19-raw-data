import pandas as pd
pd.read_csv('deceased.csv', header=None).T.to_csv('deceasedT.csv', header=False, index=False)
