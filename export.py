from numpy import ndarray
import pandas as pd
import csv


def export_to_csv(y_predict: ndarray, file_name: str):
    """Export prediction to correct csv file"""

    df = pd.DataFrame(
        y_predict,
        columns=["p0q0"],
    )

    # df[""] = df[""].astype("str")
    df.index += 1
    df.index = df.index.astype("str")
    df.to_csv(
        f"export/{file_name}.csv",
        sep=",",
        index=True,
        doublequote=True,
        quoting=csv.QUOTE_NONNUMERIC,
    )
