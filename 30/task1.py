"""
Home Work 30 - task 1
Dmytro Verovkin
robot_dreams
"""

import requests
import random

sites = [
    "google.com",
    "facebook.com",
    "twitter.com",
    "amazon.com",
    "apple.com",
]

site = "https://" + random.choice(sites)
res = requests.get(site)

print(f"site: {site}")
print(res.status_code)
print(f"HTML length: {len(res.text)}")
