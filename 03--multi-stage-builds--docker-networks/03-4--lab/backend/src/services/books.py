"""Business logic for books"""

from repositories import books as book_repository


async def get_book(book_id: int) -> dict:
    """Gets a book from the repository and applies business logic."""
    book = await book_repository.get_book(book_id)

    price = book["price"]
    book["price_with_tax"] = round(price * 1.2, 2)

    return book
