import asyncio

from pynput.keyboard import Listener
from selenium import webdriver

import keyboard
from syncer import sync
from titles import check_natively, check_amazon, request_on_natively, Title, requests


async def main():
    response = input("Do you want to get suggestions from Amazon? [y/N] ").lower()
    suggestions_from_amazon = True if response == "y" or response == "yes" else False

    browser = webdriver.Firefox()

    await check_natively(browser)
    await sync()
    await check_amazon(browser)
    await sync()
    await request_on_natively(browser)

    browser.close()


async def test():
    browser = webdriver.Firefox()

    title = Title("オーク英雄物語", "ln")
    title.set_link(
        "https://www.amazon.co.jp/-/en/%E7%90%86%E4%B8%8D%E5%B0%BD%E3%81%AA%E5%AD%AB%E3%81%AE%E6%89%8B/dp/4040736656")
    requests.append(title)

    await request_on_natively(browser)


if __name__ == '__main__':
    with Listener(on_release=keyboard.on_release) as listener:
        asyncio.run(main())
