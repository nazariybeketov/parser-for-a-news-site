import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0; Win64; x64; en-US) AppleWebKit/536.29 (KHTML, like Gecko) Chrome/53.0.2939.237 Safari/601"
}


response_1 = requests.get("https://ria.ru/politics/", headers=headers)
soup_1 = BeautifulSoup(response_1.text, "lxml")
PROGRESS_BAR_FOR = len(soup_1.find_all("div", class_="list-item"))

# URL GETTER GENERATOR


def url_generator(url: str = "https://ria.ru/politics/") -> str | None:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    data = soup.find_all("div", class_="list-item")

    for el in data:
        url_getter = el.find("a", class_="list-item__title color-font-hover-only").get(
            "href"
        )
        yield url_getter


# BASE FUNCTION


def mr_assembler():
    for el in url_generator():
        response = requests.get(el, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        try:
            article = soup.find("div", class_="article__title").text
            brief_disc = soup.find("h1", class_="article__second-title").text
            yield article, brief_disc

        except AttributeError:
            continue
