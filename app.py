from fastapi import FastAPI
from pydantic import BaseModel
from env import SportsTalentEnv

app = FastAPI()

env = SportsTalentEnv()


# ✅ Request model
class ActionRequest(BaseModel):
    action: str


# ✅ Home route
@app.get("/")
def home():
    return {"status": "ok"}


# ✅ Health check
@app.get("/health")
def health():
    return {"status": "healthy"}


# ✅ Reset (POST is correct)
@app.post("/reset")
def reset():
    return {"state": env.reset()}


# ✅ Get current state
@app.get("/state")
def state():
    return {"state": env.state()}


# ✅ Step (FIXED - JSON input)
@app.post("/step")
def step(req: ActionRequest):
    state, reward, done, _ = env.step(req.action)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }
