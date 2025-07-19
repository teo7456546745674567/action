import asyncio
from playwright.async_api import async_playwright

NUM_TABS = 3
TARGET_URL = "https://anylystic.pages.dev/"

async def open_tab(browser, index):
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto(TARGET_URL)
    print(f"Tab {index + 1} đã mở {TARGET_URL}")
    await asyncio.Future()  # giữ tab chạy vô hạn

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        tasks = [open_tab(browser, i) for i in range(NUM_TABS)]
        await asyncio.gather(*tasks)

asyncio.run(main())
