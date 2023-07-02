from typing import List

import filter_data
import validators
import visualizations

def get_graph_by_dates(dates:List):
    # dates = ["04/06/2023", "11/06/2023","18/06/2023","24/06/2023","01/07/2023"]
    df = filter_data.run_filter_flow()
    validators.validate_range(dates, df)
    visualizations.plot_graph(df, dates, 'Count_Target')
    visualizations.plot_graph(df, dates, 'Count_Nontarget')
    visualizations.plot_graph(df, dates, 'Count_Total')
