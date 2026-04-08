from models.schema import Observation, Action, Reward
from env.tasks import get_task, is_done


class OpenEnv:
    def __init__(self):
        self.task = None
        self.steps = 0
        self.history = []

    def reset(self):
        # New task load karo
        self.task = get_task()
        self.steps = 0
        self.history = []

        return Observation(
            task=self.task["name"],
            code=self.task["code"],
            history=self.history
        )

    def step(self, action: Action):
        # Step count increase
        self.steps += 1

        # User response history me add
        self.history.append(action.response)

        # Grader call karo
        score, feedback = self.task["grader"](action.response)

        # Check task complete hua ya nahi
        done = is_done(score, self.steps)

        return (
            Observation(
                task=self.task["name"],
                code=self.task["code"],
                history=self.history
            ),
            Reward(score=score, feedback=feedback),
            done,
            {}
        )

    def state(self):
        return self.task