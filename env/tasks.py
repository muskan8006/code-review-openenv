import random

def bug_grader(response):
    if ":" in response:
        return 1.0, "Correct bug found"
    return 0.5, "Partial"

def optimization_grader(response):
    if "for item in" in response:
        return 1.0, "Optimized"
    return 0.5, "Try better"

def security_grader(response):
    if "sql injection" in response.lower():
        return 1.0, "Security issue detected"
    return 0.5, "Partial"

tasks = [
    {
        "name": "Bug Detection",
        "code": "for i in range(5)\n    print(i)",
        "grader": bug_grader
    },
    {
        "name": "Code Optimization",
        "code": "for i in range(len(arr)):\n    print(arr[i])",
        "grader": optimization_grader
    },
    {
        "name": "Security Issue",
        "code": "query = \"SELECT * FROM users WHERE name = '\" + user_input + \"'\"",
        "grader": security_grader
    }
]

def get_task():
    return random.choice(tasks)

def is_done(score, steps):
    return score > 0.8 or steps > 3