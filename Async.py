import asyncio

async def hello():
    print("Hello Digvijay!")

    await asyncio.sleep(2)

    print("Welcome to Python Async Programming")


asyncio.run(hello())
