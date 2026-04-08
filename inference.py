from env.environment import OpenEnv
from models.schema import Action

env = OpenEnv()
obs = env.reset()

print("Task:", obs.task)
print("Code:\n", obs.code)

while True:
    user_input = input("Your Response: ")

    action = Action(response=user_input)
    obs, reward, done, _ = env.step(action)

    print("Score:", reward.score)
    print("Feedback:", reward.feedback)

    if done:
        print("Task Completed ")
        break