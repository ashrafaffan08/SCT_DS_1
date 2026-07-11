import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("population_data.csv")

# ---------------- Histogram ----------------
plt.figure(figsize=(8,5))
plt.hist(df["Age"], bins=8, edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of People")
plt.grid(True)
plt.show()

# ---------------- Bar Chart ----------------
gender_count = df["Gender"].value_counts()

plt.figure(figsize=(6,5))
gender_count.plot(kind="bar")
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.grid(axis="y")
plt.show()