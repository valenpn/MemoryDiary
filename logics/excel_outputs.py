import pandas as pd

def weekly_sums(df: pd.DataFrame , dates: list):
    # Convert the first and last dates in the list to Timestamp objects
    first_date = pd.Timestamp(dates[0])
    last_date = pd.Timestamp(dates[-1])
    # Calculate the start and end dates of the desired range
    start_date = first_date - pd.Timedelta(days=7)
    end_date = last_date + pd.Timedelta(days=7)
    # Filter the DataFrame based on the date range
    filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

    # Create a new DataFrame to store the results
    result_df = pd.DataFrame(columns=['Gap Between Sessions', 'Average Target', 'Average Nontarget', 'Average Total'])

    # Iterate over the dates in the list
    for i in range(len(dates)-1):
      # Calculate the start and end dates for each gap
        start_date = pd.Timestamp(dates[i])
        end_date = pd.Timestamp(dates[i+1])

        # Filter the DataFrame based on the start and end dates for each gap
        filtered_df = df[(df['Date'] >= start_date) & (df['Date'] < end_date)]

        # Calculate the number of days between the start and end dates for each gap
        num_days = (end_date - start_date).days

        # Calculate the average values for each week, normalized by the number of days
        average_target = filtered_df['Count_Target'].sum() / num_days
        average_nontarget = filtered_df['Count_Nontarget'].sum() / num_days
        average_total = filtered_df['Count_Total'].sum() / num_days

        # Append the results to the new DataFrame
        result_df = pd.concat([result_df, pd.DataFrame({'Gap Between Sessions': [num_days], 'Average Target': [average_target], 'Average Nontarget': [average_nontarget], 'Average Total': [average_total]})])

        # Reset the index of the result DataFrame
        result_df = result_df.reset_index(drop=True)

    # Write the new DataFrame to an Excel file
    result_df.to_excel('Weekly_Diary_Summary.xlsx', index=False)
    
