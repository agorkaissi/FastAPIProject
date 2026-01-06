from fastapi import FastAPI, HTTPException, Depends
from typing import Any
from db import get_db, db_execute, row_to_dict
from common import get_all, get_one, create, update, delete
import logging
import requests

logging.basicConfig(
    level=logging.ERROR,
    format="%(levelname)s | %(name)s | %(message)s"
)
app = FastAPI()

MOVIE_FIELDS = ["id", "title", "director", "year", "description"]
ACTOR_FIELDS = ["id", "name", "surname"]

@app.get('/')
async def root():
    return {"message": "Hello World"}

@app.get('/hello/{name}')
async def say_hello(name: str):
    return {"message": f"Hello, {name}!"}

@app.get('/sum')
def sum(x: int = 0, y:int = 10):
    return {"result": x + y}

@app.get('/subtract')
def subtract(x: int = 0, y: int = 10):
    return x-y

@app.get('/multiply')
def multiply(x: int = 0, y: int = 10):
    return x*y

@app.get('/geocode')
def geocode(lat: float, lon: float):
    url = f"https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat={lat}&lon={lon}"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    return response.json()


@app.get("/movies")
def get_movies(db=Depends(get_db)):
    return get_all(db, "movie", MOVIE_FIELDS, "Movie")

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int, db=Depends(get_db)):
    return get_one(db, "movie", movie_id, MOVIE_FIELDS, "Movie")

@app.post("/movies")
def add_movie(params: dict[str, Any], db=Depends(get_db)):
    movie_id = create(db, "movie", params)
    return {"id": movie_id, "message": "Movie added successfully"}

@app.delete("/movies/{movie_id}")
def remove_movie(movie_id: int, db=Depends(get_db)):
    delete(db, "movie", movie_id, "Movie")
    return {"message": "Movie deleted successfully"}

@app.delete("/movies")
def delete_movies_not_allowed():
    raise HTTPException(
        405,
        "Deleting all movies is not allowed"
    )

@app.put("/movies/{movie_id}")
@app.patch("/movies/{movie_id}")
def update_movie(movie_id: int, params: dict[str, Any], db=Depends(get_db)):
    update(db, "movie", movie_id, params, "Movie")
    return {"movie_id": movie_id, "message": "Movie updated successfully"}


@app.get("/actors")
def get_actors(db=Depends(get_db)):
    return get_all(db, "actor", ACTOR_FIELDS, "Actor")

@app.get("/actors/{actor_id}")
def get_actor(actor_id: int, db=Depends(get_db)):
    return get_one(db, "actor", actor_id, ACTOR_FIELDS, "Actor")

@app.post("/actors")
def add_actor(params: dict[str, Any], db=Depends(get_db)):
    actor_id = create(db, "actor", params)
    return {"id": actor_id, "message": "Actor added successfully"}

@app.delete("/actors/{actor_id}")
def remove_actor(actor_id: int, db=Depends(get_db)):
    delete(db, "actor", actor_id, "Actor")
    return {"message": "Actor deleted successfully"}

@app.delete("/actors")
def delete_actors_not_allowed():
    raise HTTPException(
        405,
        "Deleting all actors is not allowed"
    )

@app.put("/actors/{actor_id}")
@app.patch("/actors/{actor_id}")
def update_actor(actor_id: int, params: dict[str, Any], db=Depends(get_db)):
    update(db, "actor", actor_id, params, "Actor")
    return {"actor_id": actor_id, "message": "Actor updated successfully"}

@app.get("/movies/{movie_id}/actors")
def get_actors_for_movie(movie_id: int, db=Depends(get_db)):
    rows = db_execute(
        db,
        "SELECT a.id, a.name, a.surname FROM actor a JOIN movie_actor_through mat ON a.id = mat.actor_id WHERE mat.movie_id = :id",
        {"id": movie_id},
        fetchall=True
    )

    if not rows:
        raise HTTPException(
            404,
            "Movie or actor not found"
        )

    return [row_to_dict(r, ACTOR_FIELDS) for r in rows]
