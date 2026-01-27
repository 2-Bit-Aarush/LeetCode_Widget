import requests, json

username = "Aarush_2_Bits"

url = "https://leetcode.com/graphql"
query = {
    "query": """
    query getUserProfile($username: String!) {
      matchedUser(username: $username) {
        submitStatsGlobal {
          acSubmissionNum {
            difficulty
            count
          }
        }
      }
    }
    """,
    "variables": {"username": username}
}

r = requests.post(url, json=query).json()
stats = r["data"]["matchedUser"]["submitStatsGlobal"]["acSubmissionNum"]

data = {
    "easy": stats[1]["count"],
    "medium": stats[2]["count"],
    "hard": stats[3]["count"],
    "total": stats[0]["count"]
}

with open("stats.json", "w") as f:
    json.dump(data, f, indent=2)
