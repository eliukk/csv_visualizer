import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#reads given csv-file to pandas DataFrame, change name of the csv-file to your own csv-file
df = pd.read_csv("ladatut_aineistot_22.09.2021_16.38.28.csv", encoding = "ISO-8859-1")

#adds year column to DataFrame using date information from csv-file
df['date'] = pd.to_datetime(df.date)
df['year'] = df['date'].dt.strftime('%Y')

#groups DataFrame by bindingTile, year and sums amount of bindings to 'niteitä' column
df = df.groupby(['bindingTitle', 'year']).size().reset_index(name='niteitä')

#Saves DataFrame to csv-file
df.to_csv('bindings.csv')

#Prints DataFrame
print (df)

#creates tkinter window
root= tk.Tk() 
root.title('Csv niteet')

#creates matplotlib Figure and bar chart using DataFrame
figure1 = plt.Figure(figsize=(6,6), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

df.groupby(['bindingTitle', 'year']).sum().unstack().plot(kind='bar', ax=ax1)
ax1.set_title('Niteiden määrät eri vuosina')
ax1.get_legend().set_title("")
figure1.autofmt_xdate()
ax1.set_xlabel('')

root.mainloop()