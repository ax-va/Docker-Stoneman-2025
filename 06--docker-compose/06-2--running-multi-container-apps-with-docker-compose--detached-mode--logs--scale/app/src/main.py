import asyncio

from repository import fetch_data


async def main() -> None:
    data = await fetch_data()

    with open("/data/data.txt", "a") as file:
        file.write(f"{data}\n")
        print(f"Data {data!r} are fetched and added to the volume.")


if __name__ == "__main__":
    asyncio.run(main())
