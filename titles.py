from asyncio import sleep
from urllib import parse

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.select import Select

import keyboard


class Title:
    def __init__(self, name: str, type_format: str):
        self.name = name
        self.type_format = type_format
        self.link = None

    def set_link(self, link: str):
        self.link = link

    def __str__(self):
        return f"Name: {self.name}; Type format: {self.type_format}\nLink: {self.link}"


natively_query = "https://learnnatively.com/resources/search/?q="
amazon_query = "https://www.amazon.co.jp/s?k="
natively_request = "https://learnnatively.com/add-resource/"

already_natively = []
searching_amazon = []
requests = []


async def check_natively(browser: WebDriver):
    with open("titles.txt", "r") as file:
        for line in file.read().splitlines():
            if line == "":
                continue
            split = line.split(";")
            title = Title(split[0], split[1])

            # skip everything if the user duplicated the title
            # we don't want to flood Natively with double requests
            if title in searching_amazon:
                continue

            user_response = keyboard.ask_user()
            browser.get(f"{natively_query}{parse.quote(title.name)}")

            try:
                if browser.find_element_by_class_name("no-results"):
                    searching_amazon.append(title)
                    keyboard.reset_key_listener()
                    continue
            except NoSuchElementException:
                if await user_response:
                    searching_amazon.append(title)
                else:
                    already_natively.append(title)
                keyboard.reset_key_listener()


async def check_amazon(browser: WebDriver):
    for title in searching_amazon:
        browser.get(f"{amazon_query}{parse.quote(title.name)}")
        print(title.name)
        user_response = await keyboard.ask_user()

        if not user_response:
            continue

        title.set_link(browser.current_url.split("/ref=")[0])
        requests.append(title)


async def request_on_natively(browser: WebDriver):
    file = open("cred.txt", "r")
    line = file.read()
    file.close()
    cred = line.split(";")
    for title in requests:
        browser.get(f"{natively_request}")
        if "Login to your account" in browser.page_source:
            try:
                browser.find_element_by_class_name("t-acceptAllButton").click()
            except NoSuchElementException:
                pass
            browser.find_element_by_id("formEmail").send_keys(cred[0])
            browser.find_element_by_id("formPassword").send_keys(cred[1])
            for btn in browser.find_elements_by_class_name("btn-primary"):
                if btn.text == "Login":
                    btn.click()

        await sleep(1)
        try:
            browser.find_element_by_class_name("t-acceptAllButton").click()
        except NoSuchElementException:
            pass
        finally:
            await sleep(1)
        await sleep(1)
        browser.find_element_by_id("series-check").click()

        elements = browser.find_elements_by_class_name("form-control")
        elements[0].send_keys(title.link)
        Select(elements[1]).select_by_value(
            "manga" if title.type_format == "m" else "light_novel"
        )
        Select(elements[3]).select_by_value("25" if title.type_format == "m" else "30")

        for btn in browser.find_elements_by_class_name("btn-info"):
            if btn.text == "Request book to be added":
                btn.click()
