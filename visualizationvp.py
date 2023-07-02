import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression

#C:\Users\user\Documents\GitHub\MemoryDiary\Intrusions+Diary+-+Daily+summery_26+June+2023_15.17.xlsx

file_name =r'139_Daily_Diary_Summary.xlsx'
treatment_dates = r'dates139.xlsx'

def plot_graph(file_name: Path, treatment_dates: Path, count_of_interest: str):
    print(treatment_dates)
    df = pd.read_excel(file_name)
    #df = df.drop(df.index[0])
    treatment_dates = pd.read_excel(treatment_dates)

    # Assuming you have imported necessary libraries and loaded the data frame (df)
    colors = ['green' if date in treatment_dates.values else 'blue' for date in df['Date']]

    plt.bar(df['Date'].unique(), df[count_of_interest], color=colors)
    
    i=1
    for date, treatment in zip(df['Date'], df[count_of_interest]):
        if date in treatment_dates.values:
            plt.text(date, treatment, i, ha='center', va='bottom')
            i+=1
        
    # Convert the date column to numeric values for regression
    date_values = np.arange(len(df['Date'].unique()))

    # Reshape the date values to fit the input requirements of LinearRegression
    X1 = date_values.reshape(-1, 1)
    y1 = df[count_of_interest]

    # Perform linear regression
    regressor = LinearRegression()
    regressor.fit(X1, y1)

    # Predict the trend line values
    trend_y1 = regressor.predict(X1)

    # Plot the trend line
    plt.plot(df['Date'], trend_y1, color='red', label='Trend Line')

    plt.ylim(0,None)
    plt.xticks(rotation=90)
    # Add labels and legends
    plt.xlabel('Date')
    plt.ylabel(count_of_interest)
    plt.legend()
    # Display the plot
    plt.show()
    
def average_per_week(file_name: Path, treatment_dates: Path, count_of_interest: str):

    df = pd.read_excel(file_name)
    df = df.drop(df.index[0])
    print(df['Date'])
    treatment_dates = pd.read_excel(treatment_dates)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index(df['Date'], inplace=True)

    # # Resample the data by week and calculate the mean
    weekly_average = df[count_of_interest].resample('W').mean()

    # Reset the index to make 'Date' a column again
    weekly_average = weekly_average.reset_index()
    #dates = weekly_average['Date'].tolist()
    weeks= weekly_average['Date']
    averages = weekly_average[count_of_interest].tolist()
    
    # Create the bar plot
    plt.bar(weekly_average['Date'], weekly_average[count_of_interest], width=6.5)
    plt.xticks(weeks, rotation=90)
    plt.xlabel('Week')
    plt.ylabel('Average Count_Target')
    plt.title('Weekly Average Count_Target')
    plt.show()



average_per_week(file_name, treatment_dates, 'Count_Target')
average_per_week(file_name, treatment_dates, 'Count_Nontarget')
average_per_week(file_name, treatment_dates, 'Count_Total')