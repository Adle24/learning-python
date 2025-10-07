import asyncio


async def wicked():
    print("surrender")
    await asyncio.sleep(2)
    print("dorothy")


asyncio.run(wicked())
