import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
import numpy as np

# Load your data into a DataFrame
df = pd.read_csv('filtered_sp500_prices.csv')


# Example preprocessing (ensure this matches your actual data structure)
# Convert Market Cap to a scale appropriate for your visual (e.g., sqrt for area representation)
df['Scaled Market Cap'] = np.sqrt(df['Market Cap'])
# Example conversion, assuming 'df' is your DataFrame
df['% Change'] = df['% Change'].str.replace('%', '').astype(float)

df['% Change Color'] = df['% Change']  # This will be mapped to a color scale

# Sort values by Industry then by Scaled Market Cap for layout purposes
df = df.sort_values(['Industry', 'Scaled Market Cap'], ascending=[True, False])

# Placeholder for where to start drawing each industry
industry_start_y = 0
current_industry = None

# Setup figure and axes
fig, ax = plt.subplots(figsize=(10, 8))

# Color map for % Change
color_map = plt.cm.get_cmap('RdYlGn')

for index, row in df.iterrows():
    if current_industry != row['Industry']:
        current_industry = row['Industry']
        industry_start_y -= 20  # Adjust spacing between industries as needed
        x_position = 0  # Reset x position for new industry
        
    # Calculate box color based on % Change
    color = color_map(row['% Change Color'])  # Adjust normalization as needed
    
    # Draw box with size based on Scaled Market Cap and color based on % Change
    rect = patches.Rectangle((x_position, industry_start_y), row['Scaled Market Cap'], row['Scaled Market Cap'], linewidth=1, edgecolor='r', facecolor=color)
    ax.add_patch(rect)
    
    # Increment x_position by the width of the box plus some padding
    x_position += row['Scaled Market Cap'] + 5  # Adjust padding as needed

# Set limits, labels, and title
ax.set_xlim(0, x_position)
ax.set_ylim(industry_start_y - 100, 0)  # Adjust as needed based on your data
ax.set_xlabel('Industry →')
ax.set_ylabel('Stocks ↓')
ax.set_title('Stocks by Industry, Sized by Market Cap, Colored by % Change')

plt.axis('off')  # Turn off the axis for a cleaner look
plt.show()
