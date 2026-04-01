jobs = [
    {"title": "IT Support Engineer", "location": "Dublin", "salary": 32000,},
    {"title": "Sysadmin", "location": "remote", "salary": 45000},
    {"title": "Helpdesk", "location": "Sligo", "salary": 30000}
    ]

for job in jobs:
    if job["location"] == "remote":
        print(f"Remote jobe found: {job['title']}")