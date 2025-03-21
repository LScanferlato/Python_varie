import gpxpy
import gpxpy.gpx
import os
import pandas as pd

def calculate_speed(point1, point2):
    """Calculate speed between two points in m/s."""
    time_diff = (point2.time - point1.time).total_seconds()
    if time_diff == 0:
        return 0
    distance = point1.distance_3d(point2)
    return distance / time_diff

def calculate_acceleration(speed1, speed2, time_diff):
    """Calculate acceleration in m/s^2."""
    if time_diff == 0:
        return 0
    return (speed2 - speed1) / time_diff

# Initialize variables
results = []
max_speed_file = None
max_speed_value = 0

# Path to the folder containing GPX files
folder_path = 'rec'

# Iterate through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.gpx'):
        file_path = os.path.join(folder_path, filename)
        
        # Load GPX file
        with open(file_path, 'r') as gpx_file:
            gpx = gpxpy.parse(gpx_file)
        
        # Initialize variables for each file
        total_distance = 0
        speeds = []
        accelerations = []
        
        # Iterate through track points
        for track in gpx.tracks:
            for segment in track.segments:
                for i in range(1, len(segment.points)):
                    point1 = segment.points[i - 1]
                    point2 = segment.points[i]
                    
                    # Calculate distance
                    distance = point1.distance_3d(point2)
                    total_distance += distance
                    
                    # Calculate speed
                    speed = calculate_speed(point1, point2)
                    speeds.append(speed)
                    
                    # Calculate acceleration if there is a previous speed
                    if i > 1:
                        prev_speed = speeds[-2]
                        time_diff = (point2.time - point1.time).total_seconds()
                        acceleration = calculate_acceleration(prev_speed, speed, time_diff)
                        accelerations.append(acceleration)
        
        # Calculate statistics for each file
        min_speed = min(speeds) if speeds else 0
        max_speed = max(speeds) if speeds else 0
        avg_speed = sum(speeds) / len(speeds) if speeds else 0
        min_acceleration = min(accelerations) if accelerations else 0
        max_acceleration = max(accelerations) if accelerations else 0
        avg_acceleration = sum(accelerations) / len(accelerations) if accelerations else 0
        
        # Append results to the list
        results.append({
            'File Name': filename,
            'Total Distance (meters)': total_distance,
            'Min Speed (m/s)': min_speed,
            'Max Speed (m/s)': max_speed,
            'Max Speed (km/h)': max_speed * 3.6,
            'Avg Speed (m/s)': avg_speed,
            'Min Acceleration (m/s^2)': min_acceleration,
            'Max Acceleration (m/s^2)': max_acceleration,
            'Avg Acceleration (m/s^2)': avg_acceleration
        })
        
        # Check for the file with the maximum speed
        if max_speed > max_speed_value:
            max_speed_value = max_speed
            max_speed_file = filename

# Create a DataFrame from the results list
df_results = pd.DataFrame(results)

# Add a row with the file having the maximum speed
if max_speed_file:
    df_results.loc[len(df_results)] = {
        'File Name': f'Max Speed File: {max_speed_file}',
        'Total Distance (meters)': '',
        'Min Speed (m/s)': '',
        'Max Speed (m/s)': max_speed_value,
        'Max Speed (km/h)': max_speed_value * 3.6,
        'Avg Speed (m/s)': '',
        'Min Acceleration (m/s^2)': '',
        'Max Acceleration (m/s^2)': '',
        'Avg Acceleration (m/s^2)': ''
    }

# Save the results to an Excel file
df_results.to_excel('gpx_analysis_results.xlsx', index=False)

# Print the results in tabular format
print(df_results)
