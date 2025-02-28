import pandas as pd

# 🔹 Replace with the RAW GitHub URL of the CSV file
github_url = "https://raw.githubusercontent.com/TheiScale/YouTube-Video-Notes/ac9ab55fb90681f3d8414ab8e6fd89e7fca6b272/E%20commerce%20sales%20analysis/Sample%20-%20Superstore.csv"

# Read CSV from the URL with specified encoding
df = pd.read_csv(github_url, encoding='ISO-8859-1')

# Save the CSV locally
df.to_csv("downloaded_data.csv", index=False)

print("✅ CSV file downloaded and saved as 'downloaded_data.csv'")
