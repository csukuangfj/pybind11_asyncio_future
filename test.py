import asyncio
from example import Ticker
from time import sleep

async def main():
    tk = Ticker()
    tk.subscribe()
    #sleep(5)
    while True:
        print("[py] Awaiting to the ticker")
        ticker = await tk.next_ticker()
        print(f"[py] Ticker received: {ticker}")

asyncio.run(main())
