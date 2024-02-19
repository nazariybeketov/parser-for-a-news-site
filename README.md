# Скрабер новостного сайта
## Версия только для MacOS


## Инструкция по запуску:

- Клонировать репозиторий к себе на рабочий стол
- В файле <font color="green">writer.py</font> поменять имя пользователя в переменной <font color="red">book</font>
- Запуск производится в файле <font color="green">writer.py</font>

<br>

## Программа состоит из:
- Функции - генератора подссылок
```python

def url_generator(url: str = "https://ria.ru/politics/") -> str | None:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    data = soup.find_all("div", class_="list-item")

    for el in data:
        url_getter = el.find("a", class_="list-item__title color-font-hover-only").get(
            "href"
        )
        yield url_getter
```

- Функции - сборщика информации
```python

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


```

- Функции, которая записывает все в excel-файл
```python
def writer(arr=mr_assembler) -> None:
    print("\n")
    book = xlsxwriter.Workbook("/Users/nazarijbeketov/Desktop/parser-for-a-news-site/articles.xlsx")
    page = book.add_worksheet("Articles")

    row, column = 0, 0

    page.set_column("A:A", 100)
    page.set_column("B:B", 60)

    for item in arr():
        page.write(row, column, item[0])
        page.write(row, column + 1, item[1])
        row += 1
        bar.next()
        time.sleep(1)

    book.close()
    bar.finish()
    print("\n_______________DONE_______________\n")

```