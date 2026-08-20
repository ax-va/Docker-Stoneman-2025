import httpx


async def fetch_data() -> str:
    """Fetches data from server."""
    async with httpx.AsyncClient() as client:
        # "data-service" is the name of the `data-service` container in the same Docker network.
        # Docker DNS resolves this name to the container's IP address.
        response = await client.get("http://data-service:8000/data")

    response.raise_for_status()

    return response.text
