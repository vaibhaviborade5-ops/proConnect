from fastapi import FastAPI
from env import SportsTalentEnv

app = FastAPI()
env = SportsTalentEnv()

@app.get("/")
def home():
    return {"status": "ok"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/reset")
def reset():
    return {"state": env.reset()}

@app.get("/state")
def state():
    return {"state": env.state()}

@app.post("/step")
def step(action: str):
    state, reward, done, _ = env.step(action)
    return {"state": state, "reward": reward, "done": done}