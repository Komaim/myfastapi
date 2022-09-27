from typing import List, Optional
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, oauth2
from ..database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import func



router = APIRouter(
    prefix= "/posts",
    tags= ['posts']
)



# @router.get("/", response_model=List[schemas.Post])
@router.get("/", response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    # cur.execute(""" SELECT * FROM posts """)
    # posts = cur.fetchall()
    # posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cur.execute(""" INSERT INTO posts (title, content, published) VALUES (%s, %s , %s) RETURNING * """, (post.title, post.content, post.published))
    # new_post = cur.fetchall()
    # conn.commit()

    new_post = models.Post(owner_id= current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/{id}", response_model=schemas.PostOut)
def get_post(id: int, response: Response, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cur.execute(""" SELECT * FROM posts WHERE id = %s """, (str(id)))
    # post= cur.fetchone()
    # post = db.query(models.Post).filter(models.Post.id == id).first()
    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    return post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cur.execute(""" DELETE FROM posts WHERE id = %s RETURNING *""", (str(id)))
    # deleted_post = cur.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} doesn't exist")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform the requested action!")
    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cur.execute(""" UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", (post.title, post.content, post.published, str(id)))
    # updated_post = cur.fetchone()
    # conn.commit()

    query_post = db.query(models.Post).filter(models.Post.id == id)
    post = query_post.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} doesn't exist")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform the requested action!")    
    
    else: 
        query_post.update(updated_post.dict(), synchronize_session=False)
    db.commit()

    return query_post.first()    