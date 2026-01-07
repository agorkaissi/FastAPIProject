from fastapi import HTTPException
import sqlite3
import logging

DATABASE = "movies-extended.db"

def get_db():
    db = sqlite3.connect(DATABASE)
    try:
        yield db
    finally:
        db.close()

def row_to_dict(row, fields: list[str]):
    return dict(zip(fields, row))

def db_execute(
    db,
    query: str,
    params: dict | tuple | None = None,
    *,
    fetchone=False,
    fetchall=False
):
    try:
        cursor = db.cursor()
        cursor.execute(query, params or {})
        db.commit()

        if fetchone:
            return cursor.fetchone()
        if fetchall:
            return cursor.fetchall()

        return cursor

    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=400,
            detail="Invalid data or missing required fields"
        )
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
        raise HTTPException(
            status_code=500,
            detail="Database error"
        )
