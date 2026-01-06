from fastapi import HTTPException
from db import db_execute,row_to_dict

def get_all(db, table: str, fields: list[str], name: str):
    rows = db_execute(
        db,
        f"SELECT * FROM {table}",
        fetchall=True
    )

    if not rows:
        raise HTTPException(
            404,
            f"{name} not found"
        )

    return [row_to_dict(r, fields) for r in rows]


def get_one(db, table: str, entity_id: int, fields: list[str], name: str):
    row = db_execute(
        db,
        f"SELECT * FROM {table} WHERE id = :id",
        {"id": entity_id},
        fetchone=True
    )

    if row is None:
        raise HTTPException(
            404,
            f"{name} not found"
        )

    return row_to_dict(row, fields)


def create(db, table: str, params: dict):
    keys = ", ".join(params.keys())
    values = ", ".join(f":{k}" for k in params)

    cursor = db_execute(
        db,
        f"INSERT INTO {table} ({keys}) VALUES ({values})",
        params
    )

    return cursor.lastrowid


def delete(db, table: str, entity_id: int, name: str):
    cursor = db_execute(
        db,
        f"DELETE FROM {table} WHERE id = ?",
        (entity_id,)
    )

    if cursor.rowcount == 0:
        raise HTTPException(
            404,
            f"{name} not found"
        )


def update(db, table: str, entity_id: int, params: dict, name: str):
    if not params:
        raise HTTPException(
            400,
            "No fields provided for update"
        )

    fields = ", ".join(f"{k} = :{k}" for k in params)
    params["id"] = entity_id

    cursor = db_execute(
        db,
        f"UPDATE {table} SET {fields} WHERE id = :id",
        params
    )

    if cursor.rowcount == 0:
        raise HTTPException(
            404,
            f"{name} not found"
        )
