import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://pavanakumarn89.atlassian.net/rest/api/3/issue/bulk"

email="pavankumarn89@gmail.com"
API_Token="ATATT3xFfGF080ZMVmLtouWw7-Dlx_MGEfEAqY6l3TMD4g0KllUwhPTVl2ArxcaknHg3P3WwqhngQt4SnSbXN3W_EfeFmDdQhuZtT6tofwMXC8k98X5hNRNohUTtP1xydwOuEmjVZoHKRjzFKCLCWPm38D4SrAwn9841EKMdHYsb554MzhDebOA=56D411B5"


auth = HTTPBasicAuth(email , API_Token)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "issueUpdates": [
    {
      "fields": {
        "assignee": {
          "id": "5b109f2e9729b51b54dc274d"
        },
        "components": [
          {
            "id": "10000"
          }
        ],
        "customfield_10000": "09/Jun/19",
        "customfield_20000": "06/Jul/19 3:25 PM",
        "customfield_30000": [
          "10000",
          "10002"
        ],
        "customfield_40000": {
          "content": [
            {
              "content": [
                {
                  "text": "Occurs on all orders",
                  "type": "text"
                }
              ],
              "type": "paragraph"
            }
          ],
          "type": "doc",
          "version": 1
        },
        "customfield_50000": {
          "content": [
            {
              "content": [
                {
                  "text": "Could impact day-to-day work.",
                  "type": "text"
                }
              ],
              "type": "paragraph"
            }
          ],
          "type": "doc",
          "version": 1
        },
        "customfield_60000": "jira-software-users",
        "customfield_70000": [
          "jira-administrators",
          "jira-software-users"
        ],
        "customfield_80000": {
          "value": "red"
        },
        "description": {
          "content": [
            {
              "content": [
                {
                  "text": "Order entry fails when selecting supplier.",
                  "type": "text"
                }
              ],
              "type": "paragraph"
            }
          ],
          "type": "doc",
          "version": 1
        },
        "duedate": "2011-03-11",
        "environment": {
          "content": [
            {
              "content": [
                {
                  "text": "UAT",
                  "type": "text"
                }
              ],
              "type": "paragraph"
            }
          ],
          "type": "doc",
          "version": 1
        },
        "fixVersions": [
          {
            "id": "10001"
          }
        ],
        "issuetype": {
          "id": "10008"
        },
        "labels": [
          "bugfix",
          "blitz_test"
        ],
        "priority": {
          "id": "20000"
        },
        "project": {
          "key": "PN"
        },
        "reporter": {
          "id": "5b10a2844c20165700ede21g"
        },
        "security": {
          "id": "10000"
        },
        "summary": "Main order flow broken",
        "timetracking": {
          "originalEstimate": "10",
          "remainingEstimate": "5"
        },
        "versions": [
          {
            "id": "10000"
          }
        ]
      },
      "update": {
        "worklog": [
          {
            "add": {
              "started": "2019-07-05T11:05:00.000+0000",
              "timeSpent": "60m"
            }
          }
        ]
      }
    },
    {
      "fields": {
        "assignee": {
          "id": "5b109f2e9729b51b54dc274d"
        },
        "components": [
          {
            "id": "10000"
          }
        ],
        "customfield_10000": "09/Jun/19",
        "customfield_20000": "06/Jul/19 3:25 PM",
        "customfield_30000": [
          "10000",
          "10002"
        ],
        "customfield_40000": {
          "content": [
            {
              "content": [
                {
                  "text": "Occurs on all orders",
                  "type": "text"
                }
              ],
              "type": "paragraph"
            }
          ],
          "type": "doc",
          "version": 1
        },
        "customfield_50000": {
          "content": [
            {
              "content": [
                {
                  "text": "Could impact day-to-day work.",
                  "type": "text"
                }
              ],
              "type": "paragraph"
            }
          ],
          "type": "doc",
          "version": 1
        },
        "customfield_60000": "jira-software-users",
        "customfield_70000": [
          "jira-administrators",
          "jira-software-users"
        ],
        "customfield_80000": {
          "value": "red"
        },
        "description": {
          "content": [
            {
              "content": [
                {
                  "text": "Order remains pending after approved.",
                  "type": "text"
                }
              ],
              "type": "paragraph"
            }
          ],
          "type": "doc",
          "version": 1
        },
        "duedate": "2019-04-16",
        "environment": {
          "content": [
            {
              "content": [
                {
                  "text": "UAT",
                  "type": "text"
                }
              ],
              "type": "paragraph"
            }
          ],
          "type": "doc",
          "version": 1
        },
        "fixVersions": [
          {
            "id": "10001"
          }
        ],
        "issuetype": {
          "id": "10008"
        },
        "labels": [
          "new_release"
        ],
        "priority": {
          "id": "20000"
        },
        "project": {
          "key": "PN"
        },
        "reporter": {
          "id": "5b10a2844c20165700ede21g"
        },
        "security": {
          "id": "10000"
        },
        "summary": "Order stuck in pending",
        "timetracking": {
          "originalEstimate": "15",
          "remainingEstimate": "5"
        },
        "versions": [
          {
            "id": "10000"
          }
        ]
      },
      "update": {}
    }
  ]
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))