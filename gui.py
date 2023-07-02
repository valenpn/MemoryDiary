from tkinter import Tk, Label, Entry, Button
from datetime import datetime
import fake_api

def get_dates():
    dates = []
    for entry in date_entries:
        date_string = entry.get()
        try:
            date = datetime.strptime(date_string, "%d/%m/%Y")
            translated_date = date.strftime("%Y/%m/%d")
            dates.append(translated_date)
        except ValueError:
            print("Invalid date format. Please use the DD/MM/YYYY format.")
            return []

    # Verify the order of dates
    for i in range(len(dates) - 1):
        if dates[i] >= dates[i + 1]:
            print("Dates are not in the correct order.")
            return []
    fake_api.get_graph_by_dates(dates)
    return dates

# Create the main window
window = Tk()
window.title("Date Input")
window.geometry("400x300")  # Set the size of the window

date_labels = []
date_entries = []
for i in range(1, 6):
    label = Label(window, text=f"Treatment session {i} date (DD/MM/YYYY):")
    label.pack()
    date_labels.append(label)

    entry = Entry(window)
    entry.pack()
    date_entries.append(entry)

button = Button(window, text="Get Dates", command=lambda: print("Dates:", get_dates()))
button.pack()

# Start the GUI event loop
window.mainloop()
