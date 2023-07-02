from typing import List
import pandas as pd

import filter_data
import validators
import visualizations

memories_df: pd.DataFrame = None


def get_graph_by_dates(dates: List):
    df = filter_data.run_filter_flow(memories_df)
    validators.validate_range(dates, df)
    visualizations.plot_graph(df, dates, 'Count_Target')
    visualizations.plot_graph(df, dates, 'Count_Nontarget')
    visualizations.plot_graph(df, dates, 'Count_Total')
    visualizations.average_per_week(df, 'Count_Target')
    visualizations.average_per_week(df, 'Count_Nontarget')
    visualizations.average_per_week(df, 'Count_Total')
