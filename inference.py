from env.environment import OpenEnv
from models.schema import Action

def run_once():
    env = OpenEnv()
    obs = env.reset()

    print("=== Code Review Environment ===")
    print("Task:", obs.task)
    print("Code:\n", obs.code)

    responses = [
        "missing colon",
        "use better loop",
        "use parameterized query to prevent SQL injection"
    ]

    total_score = 0

    for r in responses:
        action = Action(response=r)
        obs, reward, done, _ = env.step(action)

        print("\nResponse:", r)
        print("Score:", reward.score)
        print("Feedback:", reward.feedback)

        total_score += reward.score

        if done:
            break

    print("\nFinal Score:", total_score)

if __name__ == "__main__":
    run_once()
