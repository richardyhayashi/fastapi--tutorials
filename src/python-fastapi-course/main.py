from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI();


class Post(BaseModel):
  title: str
  content: str
  published: bool = True
  rating: Optional[int] = None


@app.get('/')
async def root():
  return {"message": "Welcome to my API!"}


@app.get('/posts')
async def get_posts():
  return {"data": "This is your posts"}


@app.post('/createposts')
async def create_post(post: Post):
  print(post.rating)
  print(post.dict())
  return {"data": post}
# title str, content str, category, bool published