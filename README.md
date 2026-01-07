# FastAPI Project Name
FastAPIProject

# Description
This repository contains an assignment for the “Introduction to Web Application Technology” course.

# Technologies Used
- Python 3.x
- FastAPI
- SQLite 

# Project Structure
```
FastAPIProject/
│
├── .gitignore
├── common.py
├── db.py
├── main.py
├── movies.db
├── movies-extended.db
├── README.md
├── requirements.txt
└── test_main.http
```
## Files ignored by Git
The project uses `.gitignore` to exclude virtual environments, environment
variables, cache files, etc.

## Installation
1. Clone the repository:
```
git clone https://github.com/agorkaissi/FastAPIProject.git
cd FastAPIProject
```
2. Create a virtual environment (recommended):
```
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```
3. Install dependencies:
```
pip install -r requirements.txt
```
## Running the Application
```
uvicorn main:app --reload
```
then open your browser (Tested on Brave) and open:

The application will be available at:
http://127.0.0.1:8000

Interactive Swagger documentation:
http://127.0.0.1:8000/docs

Redoc documentation:
http://127.0.0.1:8000/redoc

## API Endpoints
### General
| Method | Path                             | Description                                 |
|--------|----------------------------------|---------------------------------------------|
| GET    | /                                | Test endpoint                               |
| GET    | /hello/{name}                    | Greet a user by name                        |
| GET    | /sum                             | Return sum of two numbers (query params)    |
| GET    | /subtract                        | Return difference of two numbers            |
| GET    | /multiply                        | Return product of two numbers               |
| GET    | /geocode                         | Return geocode for a given address          |

### Movies

| Method | Path                             | Description                                 |
|--------|----------------------------------|---------------------------------------------|
| GET    | /movies                          | Get list of all movies                      |
| GET    | /movies/{movie_id}               | Get a single movie by ID                    |
| POST   | /movies                          | Create a new movie                          |
| DELETE | /movies/{movie_id}               | Delete a movie by ID                        |
| DELETE | /movies                          | Delete all movies                           |
| PUT    | /movies/{movie_id}               | Update a movie by ID                        |
| PATCH  | /movies/{movie_id}               | Partially update a movie                    |

### Actors

| Method | Path                             | Description                                 |
|--------|----------------------------------|---------------------------------------------|
| GET    | /actors                          | Get list of all actors                      |
| GET    | /actors/{actor_id}               | Get a single actor by ID                    |
| POST   | /actors                          | Create a new actor                          |
| DELETE | /actors/{actor_id}               | Delete an actor by ID                       |
| DELETE | /actors                          | Delete all actors                           |
| PUT    | /actors/{actor_id}               | Update an actor by ID                       |
| PATCH  | /actors/{actor_id}               | Partially update an actor                   |

### Others

| Method | Path                             | Description                                 |
|--------|----------------------------------|---------------------------------------------|
| GET    | /movies/{movie_id}/actors        | Get all actors for a specific movie         |