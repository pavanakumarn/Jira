# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://pavanakumarn89.atlassian.net/rest/api/3/project"

email="pavankumarn89@gmail.com"

API_Token="ATATT3xFfGF080ZMVmLtouWw7-Dlx_MGEfEAqY6l3TMD4g0KllUwhPTVl2ArxcaknHg3P3WwqhngQt4SnSbXN3W_EfeFmDdQhuZtT6tofwMXC8k98X5hNRNohUTtP1xydwOuEmjVZoHKRjzFKCLCWPm38D4SrAwn9841EKMdHYsb554MzhDebOA=56D411B5"

auth = HTTPBasicAuth(email , API_Token)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

output=json.loads(response.text)

# print(output)
for i in range(len(output)):
    name = output[i]["name"]
    key = output[i]["key"]
    print(f"Project Name: "+name , "\nProject Key: "+key,"\n------------------")