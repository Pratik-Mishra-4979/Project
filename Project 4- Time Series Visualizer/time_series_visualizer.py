# === [Import Libraries] ===
import matplotlib.pyplot as plt
import pandas as pd
import calendar 
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# === [Load and Prepare Data] ===
# Load the dataset with 'date' parsed as datetime and set as index
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Remove top and bottom 2.5% of data to eliminate outliers
df = df[(df['value'] > df['value'].quantile(0.025)) &
        (df['value'] < df['value'].quantile(0.975))]

# === [Function: Line Plot] ===
def draw_line_plot():
    # Create a line plot showing daily page views
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.plot(df.index, df['value'], linewidth=1, linestyle=':', color='red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    
    # Save and return figure
    fig.savefig('line_plot.png')
    return fig

# === [Function: Bar Plot] ===
def draw_bar_plot():
    # Prepare monthly average page views grouped by year and month
    df_bar = df.copy()
    df_bar['Years'] = df.index.year
    df_bar['Month'] = df.index.strftime('%B')
    
    # Define month order for sorting
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                   'July', 'August', 'September', 'October', 'November', 'December']
    df_bar['Month'] = pd.Categorical(df_bar['Month'], categories=month_order, ordered=True)
    df_bar.sort_values(by=['Years', 'Month'], inplace=True)

    # Group and calculate mean
    monthly_avg_df = df_bar.groupby(['Years', 'Month'], observed=False)['value'].mean().reset_index()
    monthly_avg_df.rename(columns={'value': 'Average Page Views'}, inplace=True)

    # Pivot for plotting
    monthly_avg_pivot = monthly_avg_df.pivot(index='Years', columns='Month', values='Average Page Views')

    # Create bar plot
    ax = monthly_avg_pivot.plot(kind='bar', figsize=(10, 8), colormap='Set1')
    ax.set_ylabel('Average Page Views')
    plt.tight_layout()
    
    # Save and return figure
    fig = ax.get_figure()
    fig.savefig('bar_plot.png')
    return fig

# === [Function: Box Plot] ===
def draw_box_plot():
    # Prepare data with separate 'year' and 'month' columns
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')
    
    # Define correct order for months
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df_box['month'] = pd.Categorical(df_box['month'], categories=month_order, ordered=True)

    # Create box plots
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    sns.boxplot(data=df_box, x='year', y='value', ax=axes[0], hue='year', palette='Set1', legend=False)
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    sns.boxplot(data=df_box, x='month', y='value', ax=axes[1], hue='month', palette='Set1', legend=False)
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    plt.tight_layout()

    # Save and return figure
    fig.savefig('box_plot.png')
    return fig
