import time
from typing import Optional
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends
from pydantic import BaseModel
from random import randrange
import psycopg
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

class Post(BaseModel):
  title: str
  content: str
  published: bool = True
  # rating: Optional[int] = None

while True:
  try:
    conn = psycopg.connect("host=localhost dbname=fastapi user=postgres password=postgres")
    cursor = conn.cursor()
    print("Database connection was successfull!")
    break
  except Exception as error:
    print("Connecting to database failed")
    print("Error: ", error)
    time.sleep(2)

my_posts = [
  {"title": "title of post 1", "content": "content of posts 1", "id": 1},
  {"title": "favorite foods", "content": "I like pizza", "id": 2}
]

def find_post(id):
  for p in my_posts:
    if p['id'] == id:
      return p

def find_index_post(id):
  for i, p in enumerate(my_posts):
    if p['id'] == id:
      return i
 
@app.get("/")
def root():  return {"message": "Hello World"}

@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
  posts = db.query(models.Post).all()
  return {"data": posts}


@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
  posts = db.query(models.Post).all()
  return {"data": posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post, db: Session = Depends(get_db)):
  new_post = models.Post(**post.dict())
  db.add(new_post)
  db.commit()
  db.refresh(new_post)
  return {"data": new_post}

@app.get("/posts/{id}")
def get_post(id: int, db: Session = Depends(get_db)):
  post = db.query(models.Post).filter(models.Post.id == id).first()
  if not post:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f"post with id: {id} was not found"
    )
  return {"post_detail": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
  post = db.query(models.Post).filter(models.Post.id == id)

  if post.first() == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    detail=f"post with id: {id} does not exist")

  post.delete(synchronize_session=False)
  db.commit()
  
  return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, updated_post: Post, db: Session = Depends(get_db)):
  post_query = db.query(models.Post).filter(models.Post.id == id)
  post = post_query.first()

  if post == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    detail=f"post with id: {id} does not exist")

  post_query.update(updated_post.dict(), synchronize_session=False)
  db.commit()

  return {"data": post_query.first()}
