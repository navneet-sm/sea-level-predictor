from numpy import complex128
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv('epa-sea-level.csv')
    
def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x1, y1 = df['Year'], df['CSIRO Adjusted Sea Level']
    
    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x1, y1)
    
    # Create first line of best fit
    model1 = linregress(x1, y1)
    m1, c1 = model1.slope, model1.intercept
    x_line1 = pd.Series([i for i in range(1880, 2051)])
    y_line1 = (m1 * x_line1) + c1
    plt.plot(x_line1, y_line1, color='red')

    # Create second line of best fit
    df_mod = df.loc[df['Year'] >= 2000]
    x2, y2 = df_mod['Year'], df_mod['CSIRO Adjusted Sea Level']
    model2 = linregress(x2, y2)
    m2, c2 = model2.slope, model2.intercept
    x_line2 = pd.Series([i for i in range(2000, 2051)])
    y_line2 = (m2 * x_line2) + c2
    plt.plot(x_line2, y_line2, color='green')
    
    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
