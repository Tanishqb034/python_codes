import pandas as pd
import numpy as np
a = np.array([
    [101,4000],
    [102,5000],
    [103,6000]
])
df = pd.DataFrame(a,columns=["Student_ID","Fees"],index=["ST-01","ST-02","ST-03"])
print(df)