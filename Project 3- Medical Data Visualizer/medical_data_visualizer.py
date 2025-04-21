import pandas as pd  # Importing pandas for data manipulation
import seaborn as sns  # Importing seaborn for visualization
import matplotlib.pyplot as plt  # Importing matplotlib for visualization
import numpy as np  # Importing numpy for numerical operations

# === Load Data ===
df = pd.read_csv("medical_examination.csv")  # Reading the CSV file into a DataFrame
# Convert to binary based on boolean condition and cast to int

# === Calculate BMI and Identify Overweight ===
df['BMI'] = df['weight'] / (df['height'] / 100) ** 2  # Calculating BMI based on weight and height
df['overweight'] = (df['BMI'] > 25).astype(int)  # Marking individuals as overweight if BMI > 25

# === Categorize Cholesterol and Glucose ===
df['cholesterol'] = (df['cholesterol'] >= 2).astype(int)  # Categorizing cholesterol: 1 if >= 2, else 0 (boolean Logic)
df['gluc'] = (df['gluc'] >= 2).astype(int) # Categorizing glucose: 1 if >= 2, else 0 (boolean Logic)

# === Draw Categorical Plot ===
def draw_cat_plot():
   
    # === Reshape Data ===
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])  # Reshaping the DataFrame to long format
   
    # === Group Data ===
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')  # Grouping by categories and counting occurrences
   
    # === Create Plot ===
    facetgrid = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar', height=7, aspect=1)  # Creating a categorical plot
    fig = facetgrid.fig  # Extracting the figure object from the seaborn plot
   
    # === Save Plot ===
    fig.savefig('catplot.png')  # Saving the plot as a PNG file
    return fig  # Returning the figure

# === Draw Heatmap ===
def draw_heat_map():
    
    # === Filter Data ===
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]  # Filtering data where blood pressure and weight/height are within valid ranges
    df_heat = df_heat.drop(columns=['BMI'])  # Dropping the BMI column for correlation analysis
    
    # === Calculate Correlation ===
    corr = df_heat.corr()  # Calculating the correlation matrix of the filtered data
    
    # === Create Mask ===
    mask = np.triu(np.ones_like(corr, dtype=bool))  # Creating a mask to display only the lower triangle of the correlation matrix
    
    # === Create Plot ===
    fig, ax = plt.subplots(figsize=(10, 10), dpi=100)  # Creating a subplot with a specific size and resolution
    ax.set_title("Correlation Heatmap")  # Setting the title of the heatmap
    ax.set_xlabel('Variable')  # Labeling the x-axis
    ax.set_ylabel('Variable')  # Labeling the y-axis
    
    # === Plot Heatmap ===
    sns.heatmap(corr, mask=mask, annot=True, cmap='coolwarm', fmt='.1f', ax=ax, center=0, square=True, cbar_kws=dict(shrink=0.5))  # Plotting the heatmap with the correlation data
    
    # === Save Plot ===
    fig.savefig('heatmap.png')  # Saving the heatmap as a PNG file
    return fig  # Returning the figure


