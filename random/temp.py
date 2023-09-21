import pandas as pd
print(pd.__version__)
names=['chlorhexidine', 'cyntomycin', 'afobazol']
counts=[15, 18, 7]

def create_medications(counts, names):
    series_medications = pd.Series(counts, names)
    return series_medications

print(create_medications(counts, names))