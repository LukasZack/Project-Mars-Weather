import math

# ------------------------------------------------------------------------------------------------------------------------------------------------

# Given data
mean_anomaly = 101.46  # (January 1st, 2023)
eccentricity = 0.0934
inclination = 1.847925718684767  # (January 1st, 2023)
longitude_of_ascending_node = 4.948907666319641E+01  # (January 1st, 2023)
argument_of_periapsis = 2.866284864604108E+02  # (January 1st, 2023)

# Convert mean anomaly to radians
mean_anomaly_rad = math.radians(mean_anomaly)

# Initial guess for eccentric anomaly
E = mean_anomaly_rad

# Set a tolerance for convergence
tolerance = 1e-8

# Maximum number of iterations
max_attempts = 100

# Iterative method (Newton-Raphson)
for _ in range(max_attempts):
    E_new = E - (E - eccentricity * math.sin(E) - mean_anomaly_rad) / (1 - eccentricity * math.cos(E))
    if abs(E_new - E) < tolerance:
        E = E_new
        break
    E = E_new

# Convert eccentric anomaly from radians to degrees
E_deg = math.degrees(E)

print("Eccentric Anomaly:", E_deg)

# ------------------------------------------------------------------------------------------------------------------------------------------------

# Calculate the arctangent term
tan_half_E = math.tan(E / 2)

# Calculate the factor
factor = math.sqrt((1 + eccentricity) / (1 - eccentricity))

# Calculate the true anomaly
v = 2 * math.atan(factor * tan_half_E)

# Convert the true anomaly from radians to degrees
v_deg = math.degrees(v)

print("True Anomaly:", v_deg)

# ------------------------------------------------------------------------------------------------------------------------------------------------

# Semi-major axis for Mars in kilometers
semi_major_axis_mars_km = 2.279254603773820e8

true_anomaly_rad = math.radians(v_deg)

# Calculate the distance from Mars to the Sun (r) using the orbital equation
r = semi_major_axis_mars_km * (1 - eccentricity**2) / (1 + eccentricity * math.cos(true_anomaly_rad))
print("Distance between Mars and the Sun:", r, "KiloMeters")

# ------------------------------------------------------------------------------------------------------------------------------------------------

# Convert angles to radians
inclination_rad = math.radians(inclination)
longitude_of_ascending_node_rad = math.radians(longitude_of_ascending_node)
argument_of_periapsis_rad = math.radians(argument_of_periapsis)

# Calculate rectangular coordinates
X = r * (math.cos(longitude_of_ascending_node_rad) * math.cos(argument_of_periapsis_rad + true_anomaly_rad) -
         math.sin(longitude_of_ascending_node_rad) * math.sin(argument_of_periapsis_rad + true_anomaly_rad) * math.cos(inclination_rad))
Y = r * (math.sin(longitude_of_ascending_node_rad) * math.cos(argument_of_periapsis_rad + true_anomaly_rad) +
         math.cos(longitude_of_ascending_node_rad) * math.sin(argument_of_periapsis_rad + true_anomaly_rad) * math.cos(inclination_rad))
Z = r * math.sin(argument_of_periapsis_rad + true_anomaly_rad) * math.sin(inclination_rad)

print("X:", X)
print("Y:", Y)
print("Z:", Z)

# ------------------------------------------------------------------------------------------------------------------------------------------------

# Calculate right ascension (RA) and declination (Dec)
RA = math.atan2(Y, X)
Dec = math.asin(Z / math.sqrt(X**2 + Y**2 + Z**2))

# Convert right ascension from radians to degrees
RA_deg = math.degrees(RA)

# Print the calculated right ascension and declination
print("Right Ascension (RA):", RA_deg)
print("Declination (Dec):", math.degrees(Dec))

# ------------------------------------------------------------------------------------------------------------------------------------------------

# Calculate the magnitude of the position vector (distance from Mars to the Sun)
D = math.sqrt(X**2 + Y**2 + Z**2)
d_miles = D * 0.621371

# Print the calculated distance
print("Distance between Mars and the Sun:", d_miles, "Miles")

# ------------------------------------------------------------------------------------------------------------------------------------------------

