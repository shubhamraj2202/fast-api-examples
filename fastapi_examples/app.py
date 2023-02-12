from __future__ import annotations

from enum import Enum

from fastapi import FastAPI

app = FastAPI()


BOOKS = {
    "book1": {"title:": "Title One", "author": "Author One"},
    "book2": {"title:": "Title Two", "author": "Author Two"},
    "book3": {"title:": "Title Three", "author": "Author Three"},
    "book4": {"title:": "Title Four", "author": "Author Four"},
    "book5": {"title:": "Title Five", "author": "Author Five"},
    "book6": {"title:": "Title Six", "author": "Author Six"},
}


class Direction(str, Enum):
    north = "North"
    south = "South"
    east = "East"
    west = "West"


@app.get("/")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    return BOOKS.get(book_title)


@app.get("/books/mybooks")
async def read_fav_books():
    return {"book_title": "My Favourite Book"}


@app.get("/direction/{direction_name}")
async def get_direction(direction_name: Direction):
    if direction_name == Direction.north:
        return {"direction": direction_name, "sub": "up"}
    if direction_name == Direction.south:
        return {"direction": direction_name, "sub": "down"}
    if direction_name == Direction.east:
        return {"direction": direction_name, "sub": "right"}
    if direction_name == Direction.north:
        return {"direction": direction_name, "sub": "left"}
