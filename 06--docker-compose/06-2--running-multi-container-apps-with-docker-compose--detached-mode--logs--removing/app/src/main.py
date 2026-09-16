import asyncio

from repository import fetch_data


async def main() -> None:
    data = await fetch_data()

    with open("/data/data.txt", "w") as file:
        file.write(data)
        print(f"Data {data!r} are fetched and saved in the volume.")


if __name__ == "__main__":
    asyncio.run(main())
