import asyncio

from data_layer import fetch_data


async def main() -> None:
    data = await fetch_data()
    print(data)


if __name__ == "__main__":
    asyncio.run(main())
