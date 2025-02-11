# Sample stock price data for last 5 days (Simulated)
data = {
    "Date": pd.date_range(start="2024-02-05", periods=5, freq="D"),
    "AAPL": [180, 182, 181, 185, 183],
    "MSFT": [380, 385, 382, 390, 388],
    "AMZN": [150, 152, 151, 153, 152],
    "INTC": [45, 46, 46, 47, 46],
    "AMD": [130, 132, 131, 134, 133],
    "QCOM": [160, 162, 161, 164, 163],
    "AVGO": [900, 910, 905, 920, 915]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Normalize the prices for fair comparison
normalized_df = df.copy()
for col in ["AAPL", "MSFT", "AMZN", "INTC", "AMD", "QCOM", "AVGO"]:
    normalized_df[col] = (df[col] - df[col].mean()) / df[col].std()

# Define stocks in each industry
tech_stocks = ["AAPL", "MSFT", "AMZN"]
semiconductor_stocks = ["INTC", "AMD", "QCOM", "AVGO"]

# Calculate Euclidean distances for all (Tech, Semiconductor) pairs
pair_distances = {}

for tech in tech_stocks:
    for semi in semiconductor_stocks:
        dist = euclidean(normalized_df[tech], normalized_df[semi])
        pair_distances[(tech, semi)] = dist

# Find the pair with the smallest historical distance measure
best_pair = min(pair_distances, key=pair_distances.get)
best_pair, pair_distances[best_pair]
