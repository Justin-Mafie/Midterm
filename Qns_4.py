
import pandas as pd
import numpy as np

data = {
    'a': [5, 1],
    'b': [8, 2],
    'c': [3, 7]
}

df = pd.DataFrame(data)

# Calculate Manhattan distance
sample1 = df.loc[0]  # First sample
sample2 = df.loc[1]  # Second sample

manhattan_distance = np.abs(sample1 - sample2).sum()

print(f"Manhattan distance between sample 1 and sample 2: {manhattan_distance}")
