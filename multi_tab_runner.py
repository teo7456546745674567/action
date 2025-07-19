import asyncio
from datetime import datetime
from playwright.async_api import async_playwright, TimeoutError

NUM_TABS = 3
TARGET_URL = "https://anylystic.pages.dev/"

def log(message: str):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] {message}")

async def open_tab(browser, index):
    try:
        context = await browser.new_context()
        page = await context.new_page()

        log(f"Tab {index + 1} đang điều hướng đến {TARGET_URL}")
        await page.goto(TARGET_URL, timeout=30000)  # 30s timeout
        log(f"✅ Tab {index + 1} đã mở thành công {TARGET_URL}")

        # Log khi tab reload lại (nếu có logic thêm)
        page.on("framenavigated", lambda frame: log(f"🔄 Tab {index + 1} đã điều hướng lại: {frame.url}"))

        # Giữ tab chạy mãi
        await asyncio.Future()

    except TimeoutError:
        log(f"❌ Tab {index + 1} timeout khi tải {TARGET_URL}")
    except Exception as e:
        log(f"❌ Tab {index + 1} gặp lỗi: {e}")

async def main():
    log(f"🚀 Bắt đầu mở {NUM_TABS} tab tới {TARGET_URL} ở chế độ headless")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        tasks = [open_tab(browser, i) for i in range(NUM_TABS)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
