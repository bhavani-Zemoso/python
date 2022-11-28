import asyncio
import os
import aiohttp
import async_timeout

import time

async def download_coroutine(session, url):
    
    with async_timeout.timeout(1000):
        async with session.get(url) as response:
            filename = os.path.basename(url)
            with open(filename, 'wb') as file_handle:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    file_handle.write(chunk)
                await response.release()
                return response.status == 200


async def main(loop):

    urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]
    
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            print(await download_coroutine(session, url))

if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main(event_loop))
