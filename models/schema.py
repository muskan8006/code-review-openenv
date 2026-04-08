from pydantic import BaseModel

class Observation(BaseModel):
    task: str
    code: str

class Action(BaseModel):
    response: str

class Reward(BaseModel):
    score: float
    feedback: str