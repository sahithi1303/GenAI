import pandas as pd
import numpy as np

# Update path to use correct relative path from notebooks directory
df = pd.read_csv('../data/raw/cars.csv')
print(df.head(5))



