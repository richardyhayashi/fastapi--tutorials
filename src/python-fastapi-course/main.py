from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI();

# Request GET Methods url: "/"

@app.get('/')
async def root():
  return {"message": "Welcome to my API!"}


@app.get('/posts')
async def get_posts():
  return {"data": "This is your posts"}


@app.post('/createposts')
async def create_post(payload: dict = Body(...)):
  print(payload)
  return {"new_post": f"title: {payload['title']}, content: {payload['content']}"}