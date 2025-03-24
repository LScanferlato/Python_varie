import json
import math

# Define the planets in our solar system
planets = {
    'Mercury': {'diameter': 4879, 'mass': 3.3022e23, 'orbital_radius': 57.909},
    'Venus': {'diameter': 12104, 'mass': 4.8695e24, 'orbital_radius': 108.208},
    'Earth': {'diameter': 12756, 'mass': 5.9723e24, 'orbital_radius': 149.6},
    'Mars': {'diameter': 6792, 'mass': 6.4171e23, 'orbital_radius': 227.939},
    'Jupiter': {'diameter': 142984, 'mass': 1.8986e27, 'orbital_radius': 778.299},
    'Saturn': {'diameter': 116460, 'mass': 5.6846e26, 'orbital_radius': 1429.398},
    'Uranus': {'diameter': 50724, 'mass': 8.6810e25, 'orbital_radius': 2870.9},
    'Neptune': {'diameter': 49528, 'mass': 1.0243e26, 'orbital_radius': 4497.06}
}

# Create a JSON object with the planet data
planet_data = {}
for planet in planets:
    planet_data[planet] = {
        'diameter_km': round(planets[planet]['diameter'] / 1000),
        'mass_kg': round(planets[planet]['mass'] / 1e9),
        'orbital_radius_km': round(planets[planet]['orbital_radius'] * 10**3)
    }

# Print the JSON object
print(json.dumps(planet_data, indent=4))
