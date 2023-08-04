import pandas as pd
import matplotlib.pyplot as plt

# Read the tab-delimited CSV file
df = pd.read_csv('C:\\Users\\vivek\\Downloads\\results.csv', delimiter='|')


# Set timestamp as the dataframe index
df.set_index('timestamp', inplace=True)

# Create a figure and axis
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot wpm against timestamp
color = 'tab:blue'
ax1.set_xlabel('Timestamp')
ax1.set_ylabel('WPM', color=color)
ax1.plot(df.index, df['wpm'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

# Instantiate a second y-axis that shares the same x-axis
ax2 = ax1.twinx()

# Plot acc against timestamp on the second y-axis
color = 'tab:red'
ax2.set_ylabel('Accuracy', color=color)  # we already handled the x-label with ax1
ax2.plot(df.index, df['acc'], color=color)
ax2.tick_params(axis='y', labelcolor=color)

# Add a title to the plot
plt.title('WPM and Accuracy Over Time')

# Show the plot
plt.show()