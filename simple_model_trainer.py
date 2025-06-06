# simple_model_trainer.py
"""
A basic ML pipeline: load dataset, split, train a model, and evaluate.
Useful for daily testing and demos.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def load_data(path):
    """Load CSV dataset."""
    try:
        data = pd.read_csv(path)
        print(f"✅ Loaded data with shape: {data.shape}")
        return data
    except Exception as e:
        print(f"❌ Failed to load data: {e}")
        return None

def train_model(df, target_column):
    """Train a Random Forest classifier."""
    X = df.drop(columns=[target_column])
    y = df[target_column]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    acc = accuracy_score(y_test, predictions)
    print(f"🎯 Model Accuracy: {acc:.2f}")

    return model

if __name__ == "__main__":
    # Replace with your file path and target column
    path = "your_dataset.csv"
    target = "target_column"

    df = load_data(path)
    if df is not None:
        train_model(df, target)
