# from typing import List, Union
#
# import pandas as pd
# import numpy as np
#
# def count_values(df: pd.DataFrame, value: Union[int, float]) -> int:
#     return df.eq(value).sum(axis=1)
#
# def get_filtered_pd(df: pd.DataFrame, cols_names: List) -> pd.DataFrame:
#     return df[cols_names].copy()
#
#
# memories_df = pd.read_excel(DF, na_values='', keep_default_na=False)
#
# max_ideas = max(memories_df["Amount"])
# new_df = pd.DataFrame()
#
# for i in range(1, max_ideas + 1):
#     type_column_name = f"{i}_Type"
#
#     # If the type is 3, set all values in the set to NaN
#     mask = (memories_df[type_column_name] == 3)
#
#     for suffix in ["_When", "_Type", "_Content", "_Distress", "_Vividness"]:
#         column_name = f"{i}{suffix}"
#
#         if column_name in memories_df.columns:
#             memories_df.loc[mask, column_name] = np.nan
#
# new_df['count_target'] = count_values(memories_df.filter(like='_Content'), 1)
# new_df['count_nontarget'] = count_values(memories_df.filter(like='_Content'), 2)
# new_df["count_total"] = memories_df["Amount"]
# new_df["Date"] = pd.to_datetime(memories_df["StartDate"]).dt.date
#
# # Group by the 'Date' column and sum the values in each group
# grouped_mat = new_df.groupby('Date').agg({
#     'count_total': 'sum',
#     'count_target': 'sum',
#     'count_nontarget': 'sum'
# }).reset_index()
#
# grouped_mat.to_excel("memories_count.xlsx", index=False)
#
#
#
