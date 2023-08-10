


import numpy as np
import requests

# Using numpy to create an array
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# Using requests to fetch data from a URL
response = requests.get("https://api.github.com")
print("GitHub API status code:", response.status_code)
