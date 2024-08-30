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

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favorite foods", "content": "I love pizza", "id": 2}]

@app.get('/')
async def root():
  return {"message": "Welcome to my API!"}


@app.get('/posts')
async def get_posts():
  return {"data": my_posts}


@app.post('/posts')
async def create_post(post: Post):
  print(post.rating)
  print(post.dict())
  return {"data": post}
# title str, content str, category, bool published