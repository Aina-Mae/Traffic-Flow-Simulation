import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to generate vehicle inter-arrival times using exponential distribution
def generate_vehicle_data(arrival_rate, num_vehicles):
    inter_arrival_times = np.random.exponential(1 / arrival_rate, num_vehicles)
    arrival_times = np.cumsum(inter_arrival_times)  # Cumulative sum to get actual arrival times
    return arrival_times

# Function to simulate traffic flow based on the vehicle data and green light duration
def simulate_traffic_flow(vehicle_data, green_light_duration):
    vehicles_passed = 0
    for arrival_time in vehicle_data:
        if arrival_time <= green_light_duration:
            vehicles_passed += 1
    return vehicles_passed

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

# Main simulation function
def main():
    # Parameters
    arrival_rate = 0.1  # vehicles per minute
    num_vehicles = 100
    green_light_duration = 10  # 10 minutes of green light

    # Data generation
    vehicle_data = generate_vehicle_data(arrival_rate, num_vehicles)

    # Perform EDA
    perform_eda(vehicle_data)

    # Run the simulation
    vehicles_passed = simulate_traffic_flow(vehicle_data, green_light_duration)
    print(f"Number of vehicles that passed during green light: {vehicles_passed}")

    # Visualization of vehicle arrivals and green light duration
    plt.figure(figsize=(10, 6))
    plt.plot(vehicle_data, np.ones_like(vehicle_data), 'bo', label="Vehicle Arrivals")
    plt.axvline(x=green_light_duration, color='r', linestyle='--', label="Green Light Duration")
    plt.xlabel("Time (minutes)")
    plt.ylabel("Vehicles")
    plt.title("Vehicle Arrivals and Green Light Duration")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
