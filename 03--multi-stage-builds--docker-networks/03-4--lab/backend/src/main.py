"""Main FastAPI application."""

from fastapi import FastAPI

from web.books import router

app = FastAPI()
app.include_router(router)


@app.get("/")
async def root() -> dict:
    "Returns the backend service status."
    return {"status": "Backend is running"}
