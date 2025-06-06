# daily_eda_toolkit.py
"""
A handy script for performing basic Exploratory Data Analysis (EDA) on any dataset.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_dataset(path):
    """Load dataset from CSV file."""
    try:
        data = pd.read_csv(path)
        print(f"✅ Dataset loaded successfully. Shape: {data.shape}")
        return data
    except Exception as e:
        print(f"❌ Error loading dataset: {e}")

def basic_info(df):
    """Display basic information of the dataset."""
    print("\n📊 Basic Info:\n")
    print(df.info())
    print("\n🧮 Descriptive Statistics:\n")
    print(df.describe())
    print("\n🔍 Missing Values:\n")
    print(df.isnull().sum())

def visualize_distribution(df, column):
    """Visualize distribution of a single column."""
    plt.figure(figsize=(8, 4))
    sns.histplot(df[column], kde=True)
    plt.title(f"Distribution of {column}")
    plt.show()

def correlation_heatmap(df):
    """Plot correlation heatmap."""
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title("🔗 Correlation Heatmap")
    plt.show()

if __name__ == "__main__":
    # Change this path to your CSV file
    file_path = "your_dataset.csv"
    
    df = load_dataset(file_path)
    
    if df is not None:
        basic_info(df)
        correlation_heatmap(df)
        # To visualize specific column: uncomment below
        # visualize_distribution(df, 'your_column_name')
