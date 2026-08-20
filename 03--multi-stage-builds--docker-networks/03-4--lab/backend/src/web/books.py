"""HTTP endpoints for the backend application."""

import httpx
from fastapi import APIRouter, HTTPException

from services import books as books_service

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/{book_id}")
async def get_book(book_id: int) -> dict:
    """Gets a book with processed business data."""
    try:
        return await books_service.get_book(book_id)

    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise HTTPException(
                status_code=404,
                detail="Book not found",
            ) from e

        raise
