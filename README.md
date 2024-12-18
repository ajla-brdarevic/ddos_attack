# DDoS Detection Using K-Means Clustering

This project uses the K-means clustering algorithm to detect DDoS attacks in simulated network traffic. The goal is to separate normal traffic from anomalous traffic patterns indicative of an attack.

## Technologies Used
- **Python 3.x**
- **Scikit-learn** (for K-means)
- **NumPy** (for data manipulation)
- **Matplotlib** (for visualization)

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ddos-detection-kmeans.git
   cd ddos-detection-kmeans
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the script:
   ```bash
    python main.py
   
## How it Works
Traffic Simulation: Random network traffic data is generated with some manipulation to simulate a DDoS attack.
K-means Clustering: The K-means algorithm classifies the traffic into normal and attack traffic clusters.
Visualization: Results are displayed in a scatter plot, highlighting normal vs attack traffic.

## Conclusion
This project demonstrates basic DDoS attack detection using K-means. Future improvements could include real-time detection and using more advanced machine learning algorithms.
