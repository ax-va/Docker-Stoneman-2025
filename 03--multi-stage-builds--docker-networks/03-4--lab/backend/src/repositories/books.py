"""Data access for the backend application"""

import httpx


async def get_book(book_id: int) -> dict:
    """Gets a book from the data-service container."""
    async with httpx.AsyncClient() as client:
        # "data-service" is the name of the `data-service` container in the same Docker network.
        # Docker DNS resolves this name to the container's IP address.
        response = await client.get(f"http://data-service:8000/books/{book_id}")

    response.raise_for_status()

    return response.json()
