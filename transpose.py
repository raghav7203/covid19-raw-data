import pandas as pd
pd.read_csv('confirmed.csv', header=None).T.to_csv('confirmedT.csv', header=False, index=False)
