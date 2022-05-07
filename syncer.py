from titles import already_natively, searching_amazon, requests


async def content_from_titles(titles, content):
    for title in titles:
        content += str(title)
        content += "\n\n"
    return content


async def check_and_sync(titles, content, filename):
    content = await content_from_titles(titles, content)

    file = open(filename, 'w')
    file.write(content)
    file.close()


async def sync():
    _already_natively = []
    _searching_amazon = []
    _requests = []

    natively = check_and_sync(already_natively,
                              "These titles are already present on Natively:\n", "natively.txt")
    amazon = check_and_sync(searching_amazon,
                            "These titles are being (or were) searched on Amazon JP:\n", "amazon.txt")
    request = check_and_sync(requests,
                             "These titles are being (or were) requested on Natively:\n", "requests.txt")

    await natively
    await amazon
    await request
