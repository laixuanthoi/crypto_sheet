from tkinter.messagebox import NO
import xlwings as xw
import asyncio, json, pprint
import pandas as pd
from pyppeteer import launch

import os, sys
sys.path.append(os.getcwd())

df_fed_funding_rate = None

def get_fed_funding_rate_data_frame():
    async def interceptResponse(response):
        global df_fed_funding_rate
        url_filter = "https://fred.stlouisfed.org/graph/api/series/?obs=true&sid=FEDFUNDS"
        url = response.url
        if not response.ok:
            return
        if url == url_filter:
            json = await response.json()
            observations_data = json['observations']
            df_fed_funding_rate = pd.DataFrame(observations_data[0], columns=['timestamp', 'funding_rate'])
            df_fed_funding_rate['timestamp'] = pd.to_datetime(df_fed_funding_rate['timestamp'], unit='ms')


    async def main():
        browser = await launch()
        page = await browser.newPage()
        await page.goto('https://fred.stlouisfed.org/series/FEDFUNDS')
        await page.screenshot({'path': 'example.png'})
        new_resutls = page.on('response', 
            lambda response: asyncio.ensure_future(interceptResponse(response)))
        
        while df_fed_funding_rate is None:
            print("wait for", df_fed_funding_rate)
            await page.waitFor(1000)
        await browser.close()
    asyncio.get_event_loop().run_until_complete(main())


get_fed_funding_rate()
# def main():
#     wb = xw.Book.caller()
#     sheet = wb.sheets('Fed Index')


# if __name__ == "__main__":
#     xw.Book("market_overview.xlsm").set_mock_caller()
#     main()
