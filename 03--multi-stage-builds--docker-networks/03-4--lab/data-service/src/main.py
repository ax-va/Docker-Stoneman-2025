""" A simple data-service that imitates a database."""

from fastapi import FastAPI, HTTPException

from books import BOOKS


app = FastAPI()

@app.get("/books/{book_id}")
async def get_book(book_id: int) -> dict:
    """Returns a book by its ID."""
    book: dict = BOOKS.get(book_id)

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found",
        )

    return book
