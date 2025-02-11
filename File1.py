import numpy as np
import pandas as pd
from scipy.spatial.distance import euclidean

# Sample stock price data for the last 5 days (Assume daily closing prices)
data = {
    "Date": pd.date_range(start="2024-02-05", periods=5, freq="D"),
    "AAPL": [180, 182, 181, 185, 183],
    "MSFT": [380, 385, 382, 390, 388],
    "AMD": [130, 132, 131, 134, 133],
    "INTC": [45, 46, 46, 47, 46]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Normalize the prices (to make comparisons fair across different price ranges)
normalized_df = df.copy()
for col in ["AAPL", "MSFT", "AMD", "INTC"]:
    normalized_df[col] = (df[col] - df[col].mean()) / df[col].std()

# Calculate Euclidean distances between all possible pairs
stocks = ["AAPL", "MSFT", "AMD", "INTC"]
distances = {}

for i in range(len(stocks)):
    for j in range(i + 1, len(stocks)):
        stock1, stock2 = stocks[i], stocks[j]
        dist = euclidean(normalized_df[stock1], normalized_df[stock2])
        distances[(stock1, stock2)] = dist

# Find the pair with the smallest historical distance measure
closest_pair = min(distances, key=distances.get)
closest_pair, distances[closest_pair]
