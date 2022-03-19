import pandas._testing as tm
import pandas as pd
import numpy as np

def unpivot(frame):
    N, K = frame.shape
    data = {
        "value": frame.to_numpy().ravel("F"),
        "variable": np.asarray(frame.columns).repeat(N),
        "date": np.tile(np.asarray(frame.index), K),
    }
    return pd.DataFrame(data, columns=["date", "variable", "value"])

df = unpivot(tm.makeTimeDataFrame(3))
print(df)

filtered = df[df["variable"] == "A"]
print(filtered)

pivoted = df.pivot(index="date", columns="variable", values="value")
print(pivoted)