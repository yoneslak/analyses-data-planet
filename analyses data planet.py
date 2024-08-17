import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_planetary_data():
    """Load the planetary data into a Pandas dataframe"""
    data = {
        'Planet': ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'],
        'Diameter (km)': [4879, 12104, 12756, 6792, 142984, 116460, 50724, 49528],
        'Mass (kg)': [3.3022e23, 4.8695e24, 5.9723e24, 6.4171e23, 1.8986e27, 5.6846e26, 8.6810e25, 1.0243e26],
        'Orbital Period (days)': [87.969, 224.701, 365.256, 687.024, 4332.820, 10759.220, 30687.150, 60190.030],
        'Surface Temperature (K)': [173, 737, 288, 210, 124, 95, 59, 48],
        'Atmosphere': ['Thin', 'Thick', 'Moderate', 'Thin', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen'],
        'Moons': [0, 0, 1, 2, 79, 62, 27, 14]
    }
    return pd.DataFrame(data)

def calculate_statistics(df):
    """Calculate some basic statistics for the planetary data"""
    mean_diameter = np.mean(df['Diameter (km)'])
    std_diameter = np.std(df['Diameter (km)'])
    print(f'Mean diameter: {mean_diameter:.2f} km')
    print(f'Standard deviation of diameter: {std_diameter:.2f} km')

def visualize_diameter_distribution(df):
    """Visualize the distribution of planetary diameters"""
    sns.set()
    sns.histplot(df['Diameter (km)'], bins=5)
    plt.xlabel('Diameter (km)')
    plt.ylabel('Frequency')
    plt.title('Histogram of Planetary Diameters')
    plt.show()

def visualize_diameter_mass_relationship(df):
    """Visualize the relationship between planetary diameters and masses"""
    sns.set()
    sns.scatterplot(x='Diameter (km)', y='Mass (kg)', data=df)
    plt.xlabel('Diameter (km)')
    plt.ylabel('Mass (kg)')
    plt.title('Scatterplot of Planetary Diameters vs. Masses')
    plt.show()

def visualize_moon_distribution(df):
    """Visualize the distribution of planetary moons"""
    sns.set()
    sns.barplot(x='Planet', y='Moons', data=df)
    plt.xlabel('Planet')
    plt.ylabel('Number of Moons')
    plt.title('Barplot of Number of Moons')
    plt.show()

def visualize_correlation_matrix(df):
    """Visualize the correlation matrix between planetary attributes"""
    corr_matrix = df[['Diameter (km)', 'Mass (kg)', 'Orbital Period (days)', 'Surface Temperature (K)']].corr()
    sns.set()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
    plt.title('Heatmap of Correlation Matrix')
    plt.show()

if __name__ == '__main__':
    df = load_planetary_data()
    calculate_statistics(df)
    visualize_diameter_distribution(df)
    visualize_diameter_mass_relationship(df)
    visualize_moon_distribution(df)
    visualize_correlation_matrix(df)
    #این کد داده های سیارات را تجزیه و تحلیل می کند