'''a program that reads data from "weight_height.csv" using pandas
and plots various relationships (weight vs height, age vs weight, etc.)
using matplotlib for visualization.'''

import pandas as pd; 'import pandas for data manipulation'
import matplotlib.pyplot as plt; 'import matplotlib for plotting'
import numpy as np; 'import numpy for numerical operations'

# reads data from the specified csv and generates various plots
def plot_data(filename="weight_height.csv"):
    try:
        df = pd.read_csv(filename) # read csv into dataframe
        if df.empty:
            print(f"the file '{filename}' is empty or contains no data. no plots to generate.")
            return
        
        # ensure columns are numeric for plotting, coerce errors to nan
        df['height'] = pd.to_numeric(df['height'], errors='coerce')
        df['weight'] = pd.to_numeric(df['weight'], errors='coerce')
        df['age'] = pd.to_numeric(df['age'], errors='coerce')
        
        # drop rows where critical plotting data might be missing after coercion
        df.dropna(subset=['height', 'weight', 'age', 'gender'], inplace=True)

        if df.empty:
            print(f"no valid numeric data found in '{filename}' for plotting after cleaning.")
            return

    except FileNotFoundError:
        print(f"error: the file '{filename}' was not found. please ensure it exists in the same directory.") # clearer error message
        return
    except Exception as e:
        print(f"an error occurred while reading the file: {e}") # general read error
        return

    # create a figure and a set of subplots (2 rows, 3 columns)
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle('analysis of weight, height, and age data', fontsize=20) # main title for the figure

    # plot 1: weight vs. height (scatterplot)
    axes[0, 0].scatter(df['height'], df['weight'], alpha=0.6, edgecolors='w', s=50)
    axes[0, 0].set_title('weight vs. height')
    axes[0, 0].set_xlabel('height (cm)')
    axes[0, 0].set_ylabel('weight (kg)')
    axes[0, 0].grid(True)

    # plot 2: age vs. weight (scatterplot)
    axes[0, 1].scatter(df['age'], df['weight'], alpha=0.6, color='green', edgecolors='w', s=50)
    axes[0, 1].set_title('age vs. weight')
    axes[0, 1].set_xlabel('age (years)')
    axes[0, 1].set_ylabel('weight (kg)')
    axes[0, 1].grid(True)
    
    # plot 3: height vs. age (scatterplot)
    axes[0, 2].scatter(df['age'], df['height'], alpha=0.6, color='red', edgecolors='w', s=50)
    axes[0, 2].set_title('height vs. age')
    axes[0, 2].set_xlabel('age (years)')
    axes[0, 2].set_ylabel('height (cm)')
    axes[0, 2].grid(True)

    # plot 4: height distribution by gender (boxplot)
    df.boxplot(column='height', by='gender', ax=axes[1, 0], patch_artist=True)
    axes[1, 0].set_title('height distribution by gender')
    axes[1, 0].set_xlabel('gender')
    axes[1, 0].set_ylabel('height (cm)')
    plt.suptitle('') # suppress default boxplot suptitle

    # plot 5: weight distribution by gender (boxplot)
    df.boxplot(column='weight', by='gender', ax=axes[1, 1], patch_artist=True)
    axes[1, 1].set_title('weight distribution by gender')
    axes[1, 1].set_xlabel('gender')
    axes[1, 1].set_ylabel('weight (kg)')

    # hide the unused 6th subplot
    axes[1, 2].axis('off')

    # adjust layout to prevent plot overlap
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    
    plt.show() # display all generated plots

# main execution block
if __name__ == "__main__":
    plot_data() 
