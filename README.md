# 👥 Customer Segmentation using K-Means Clustering

A Machine Learning project that groups customers into different segments using the **K-Means Clustering** algorithm based on their **Age**, **Annual Income**, and **Spending Score**.

---

## 📌 Project Overview

Customer segmentation is an unsupervised machine learning technique used to divide customers into groups with similar characteristics. This project uses the K-Means algorithm to identify customer segments that can help businesses understand purchasing behavior and improve marketing strategies.

---

## 🎯 Features

- Customer Segmentation using K-Means
- Data Visualization
- Cluster Center Identification
- Customer Cluster Prediction
- Scatter Plot Visualization

---

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Scikit-learn

---

## 📂 Dataset Features

| Feature | Description |
|---------|-------------|
| Age | Customer Age |
| Annual_Income_k$ | Annual Income (in thousand dollars) |
| Spending_Score | Customer Spending Score |

---

## 📁 Project Structure

```
Customer-Segmentation-KMeans
│
├── dataset
│   └── customer_segmentation_100.csv
│
├── source
│   └── kmeans_clustering.py
│
├── images
│   └── clusters.png
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Customer-Segmentation-KMeans.git
```

Navigate to the project

```bash
cd Customer-Segmentation-KMeans
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python kmeans_clustering.py
```

---

## 🔄 Machine Learning Workflow

```
Customer Dataset
        │
        ▼
Feature Selection
        │
        ▼
K-Means Clustering
        │
        ▼
Cluster Assignment
        │
        ▼
Visualization
```

---

## 📊 Model Output

The model:

- Creates **5 customer clusters**
- Displays cluster centers
- Predicts the cluster for a new customer
- Visualizes clusters using a scatter plot

Example Test Data

```
Age : 24
Annual Income : 25
Spending Score : 85
```

Predicted Output

```
Cluster : 2
```

*(Cluster number may vary depending on model initialization.)*

---

## 📈 Visualization

The scatter plot shows:

- Customer clusters
- Cluster centers (marked with **X**)
- Spending Score vs Annual Income

---

## 🚀 Future Improvements

- Use the Elbow Method to determine the optimal number of clusters.
- Evaluate clustering quality using the Silhouette Score.
- Develop an interactive dashboard with Streamlit.
- Test other clustering algorithms such as DBSCAN and Hierarchical Clustering.

---

## 📚 Libraries Used

- Pandas
- Matplotlib
- Scikit-learn

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## 👨‍💻 Author

**Ranjita K Bagali**

Electronics & Communication Engineering Student

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.# Customer-Segmentation-KMeans
