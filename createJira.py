
import requests
from requests.auth import HTTPBasicAuth
import json

def createJira():
    url = "https://pavanakumarn89.atlassian.net/rest/api/3/issue"

    email="pavankumarn89@gmail.com"
    API_Token="ATATT3xFfGF080ZMVmLtouWw7-Dlx_MGEfEAqY6l3TMD4g0KllUwhPTVl2ArxcaknHg3P3WwqhngQt4SnSbXN3W_EfeFmDdQhuZtT6tofwMXC8k98X5hNRNohUTtP1xydwOuEmjVZoHKRjzFKCLCWPm38D4SrAwn9841EKMdHYsb554MzhDebOA=56D411B5"

    auth = HTTPBasicAuth(email , API_Token)
    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "My First Jira ticket",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        "issuetype": {
        "id": "10008"
        },
        "parent": {
        "key": "PROJ-123"
        },
        "project": {
        "key": "PN"
        },
        "summary": "First Jira Ticket",
    },
    "update": {}
    } )

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))



