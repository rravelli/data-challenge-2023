from numpy import ndarray
import pandas as pd
import numpy as np
import csv


def export_to_csv(y_predict: ndarray, file_name: str):
    df = pd.DataFrame(
        np.array([np.arange(len(y_predict)) + 1, y_predict]).T,
        columns=["", "p0q0"],
    )

    df[""] = df[""].astype("str")

    df.to_csv(
        f"export/{file_name}.csv",
        sep=",",
        index=False,
        doublequote=True,
        quoting=csv.QUOTE_NONNUMERIC,
    )
