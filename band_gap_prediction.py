"""
Band Gap Prediction for Perovskites using Random Forest

Dataset: Castelli Perovskites (from matminer)
Author: Kajal Madaan
"""

# =======================
# 📦 1. Imports
# =======================
import pandas as pd
from matminer.datasets import load_dataset
from pymatgen.core import Composition

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


# =======================
# 📋 2. Data Loading & Cleaning
# =======================
def load_and_clean_data():
    """
    Load the Castelli perovskites dataset and clean it by removing NaNs.
    Extract A, B, X elements from the chemical formula.
    Returns: Cleaned DataFrame with new columns: A, B, X
    """
    df = load_dataset("castelli_perovskites")

    # Drop rows with missing band gap
    df = df.dropna(subset=['gap gllbsc'])

    # Extract A, B, X sites from formula
    def extract_sites(formula):
        comp = Composition(formula)
        elements = list(comp.elements)
        A = elements[0].symbol if len(elements) > 0 else None
        B = elements[1].symbol if len(elements) > 1 else None
        X_elements = elements[2:] if len(elements) > 2 else []
        X = ''.join([el.symbol for el in X_elements]) if X_elements else None
        return pd.Series([A, B, X])

    df[['A', 'B', 'X']] = df['formula'].apply(extract_sites)

    return df


# =======================
# 🧪 3. Feature Engineering
# =======================
def prepare_features(df):
    """
    Selects and encodes features. Drops non-relevant columns.
    Returns:
        - X_encoded: One-hot encoded features
        - y: Target band gap
    """
    X = df.drop(columns=['gap gllbsc', 'structure', 'formula', 'gap is direct'])
    y = df['gap gllbsc']

    # One-hot encode categorical columns (A, B, X)
    X_encoded = pd.get_dummies(X, columns=['A', 'B', 'X'])

    return X_encoded, y


# =======================
# 🤖 4. Train and Evaluate Model
# =======================
def train_and_evaluate(X, y):
    """
    Splits data, trains a RandomForest model, and prints MAE.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)

    print(f"✅ Mean Absolute Error: {mae:.3f} eV")
    return model


# =======================
# 🚀 5. Main Script
# =======================
def main():
    print("📥 Loading dataset...")
    df = load_and_clean_data()

    print("🔧 Preparing features...")
    X_encoded, y = prepare_features(df)

    print("🤖 Training and evaluating model...")
    model = train_and_evaluate(X_encoded, y)


if __name__ == "__main__":
    main()
