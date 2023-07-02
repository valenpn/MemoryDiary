import pandas as pd
from logics.filter_data import run_filter_flow


def test_identical_keys():
    test_df = pd.read_excel('memories_count.xlsx')
    df = run_filter_flow(pd.read_excel('Intrusions.xlsx'))

    assert list(df) == list(test_df)


def test_df_values():
    test_df = pd.read_excel('memories_count.xlsx')
    df = run_filter_flow(pd.read_excel('Intrusions.xlsx'))
    test_df['Date'] = pd.to_datetime(test_df['Date']).dt.date

    for key in list(test_df):
        assert list(df[key]) == list(test_df[key])
