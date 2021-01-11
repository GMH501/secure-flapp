import sys

import requests

route = sys.argv[1]
env = sys.argv[2]

key = env.split("=")[0]
value = env.split("=")[1]
print(route, key, value)

r = requests.get(route + "/" + value)
print(r.text)
