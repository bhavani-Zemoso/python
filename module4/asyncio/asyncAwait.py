import asyncio

def func():
    print("func()")

async def my_coroutine():
    await func()
