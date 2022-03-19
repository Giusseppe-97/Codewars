import pandas as pd

df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3],
)

df2 = pd.DataFrame(
    {
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
    },
    index=[4, 5, 6, 7],
)

df3 = pd.DataFrame(
    {
        "A": ["A8", "A9", "A10", "A11"],
        "B": ["B8", "B9", "B10", "B11"],
        "C": ["C8", "C9", "C10", "C11"],
        "D": ["D8", "D9", "D10", "D11"],
    },
    index=[8, 9, 10, 11],
)

frames_ = [df1, df2, df3]

result = pd.concat(frames_)
# print(df1)
# print(df3)
# print(df2)
# print(result)

def concatenate(frames):

    results = pd.concat(
    frames,
    axis=0,
    join="outer",
    ignore_index=False,
    keys=["x", "y", "z"],
    levels=None,
    names=None,
    verify_integrity=False,
    copy=True,
    )
    return results.loc["y"]

def concatenate_several(frames):
    """If you need to use the operation over several datasets, 
    use a list comprehension

    Parameters
    ----------
    frames : list of datasets
    frames = [ process_your_file(f) for f in files ]

    Returns
    -------
    results
        pd.concat(frames)
    """
    
    results = pd.concat(
    frames,
    axis=0,
    join="outer",
    ignore_index=False,
    keys=["x", "y", "z"],
    levels=None,
    names=None,
    verify_integrity=False,
    copy=True,
    )
    return results


def concatenate_several(left, right):
    """join operations between DataFrame or named Series objects

    Parameters
    ----------
    left : datasets to the left
    right : datasets to the right

    Returns
    -------
    results : pd.merge(left,right,how=join method)
    join method (str): inner, outer, right left or cross 
    """
    
    results = pd.merge(
    left,
    right,
    how="inner",
    on=None,
    left_on=None,
    right_on=None,
    left_index=False,
    right_index=False,
    sort=True,
    suffixes=("_x", "_y"),
    copy=True,
    indicator=False,
    validate=None,
    )

    return results

print(concatenate(frames_))