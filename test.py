import pandas as pd

T = pd.read_excel("intrusion.xlsx", na_values='', keep_default_na=False)

selected_columns = ['Amount']

# Create the new DataFrame with the selected columns
filtered_df = T[selected_columns].copy()

max_memories = max(filtered_df["Amount"])


new_column_names = [f"{i}_Content" for i in range(1, max_memories + 1)]
new_column_names.append("Amount")
new_column_names.append("StartDate")
filtered_df = T[new_column_names].copy()

new_df = pd.DataFrame()

# Calculate the count_target for each row (sum of 1_Content == 1)

new_df['count_target'] = filtered_df.iloc[:, :4].eq(1).sum(axis=1)
new_df['count_nontarget'] = filtered_df.iloc[:, :4].eq(2).sum(axis=1)
new_df["count_total"] = filtered_df["Amount"]
new_df["Date"] = filtered_df["StartDate"]


# Set count_total to be equal to the 'Amount' column in the original DataFrame
new_df['count_total'] = filtered_df['Amount']

new_df['Date'] = pd.to_datetime(new_df['Date'])



new_df['Date'] = pd.to_datetime(new_df['Date'])

# Next, extract the date part from the 'Date' column to group the rows
new_df['Date'] = new_df['Date'].dt.date

# Group by the 'Date' column and sum the values in each group
grouped_mat = new_df.groupby('Date').agg({
    'count_total': 'sum',
    'count_target': 'sum',
    'count_nontarget': 'sum'
}).reset_index()

grouped_mat.to_excel("memories_count.xlsx", index=False)