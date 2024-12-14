import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to generate vehicle inter-arrival times using exponential distribution
def generate_vehicle_data(arrival_rate, num_vehicles):
    inter_arrival_times = np.random.exponential(1 / arrival_rate, num_vehicles)
    arrival_times = np.cumsum(inter_arrival_times)  # Cumulative sum to get actual arrival times
    return arrival_times

# Function to perform Exploratory Data Analysis (EDA)
def perform_eda(vehicle_data):
    df = pd.DataFrame(vehicle_data, columns=["Arrival Time"])

    # Basic statistics
    print("Basic statistics of vehicle arrival times:")
    print(df.describe())

    # Histogram of vehicle inter-arrival times
    sns.histplot(df["Arrival Time"], kde=True)
    plt.title("Histogram of Vehicle Arrival Times")
    plt.show()

# Main function to generate data and perform EDA
def main():
    arrival_rate = 0.1  # vehicles per minute
    num_vehicles = 100

    # Generate vehicle data
    vehicle_data = generate_vehicle_data(arrival_rate, num_vehicles)

    # Perform Exploratory Data Analysis
    perform_eda(vehicle_data)

if __name__ == "__main__":
    main()
