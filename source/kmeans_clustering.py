import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# ==============================
# Load Dataset
# ==============================
df = pd.read_csv("customer_segmentation_100.csv")

# ==============================
# Select Features
# ==============================
X = df[['Age', 'Annual_Income_k$', 'Spending_Score']]

# ==============================
# Train K-Means Model
# ==============================
model = KMeans(
    n_clusters=5,
    random_state=42,
    n_init=10
)

model.fit(X)

# ==============================
# Display Cluster Centers
# ==============================
print("Cluster Centers:")
print("--------------------------------------------")
print("Age | Annual Income (k$) | Spending Score")
print(model.cluster_centers_)

# ==============================
# Predict Cluster for a New Customer
# ==============================
new_customer = [[24, 25, 85]]

predicted_cluster = model.predict(new_customer)

print("\nNew Customer Details:")
print(f"Age            : {new_customer[0][0]}")
print(f"Annual Income  : {new_customer[0][1]} k$")
print(f"Spending Score : {new_customer[0][2]}")

print(f"\nPredicted Cluster : {predicted_cluster[0]}")

# ==============================
# Add Cluster Labels
# ==============================
df["Cluster"] = model.labels_

# ==============================
# Visualize Customer Clusters
# ==============================
plt.figure(figsize=(8, 6))

plt.scatter(
    df["Annual_Income_k$"],
    df["Spending_Score"],
    c=df["Cluster"],
    s=70
)

plt.scatter(
    model.cluster_centers_[:, 1],
    model.cluster_centers_[:, 2],
    marker="X",
    color="black",
    s=250,
    label="Cluster Centers"
)

plt.title("Customer Segmentation using K-Means")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score")
plt.legend()

# Save graph
plt.savefig("customer_clusters.png", dpi=300, bbox_inches="tight")

plt.show()