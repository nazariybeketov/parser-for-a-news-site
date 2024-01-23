import time
from progress.bar import IncrementalBar
import xlsxwriter
from main import mr_assembler, PROGRESS_BAR_FOR

mylist = [i for i in range(1, PROGRESS_BAR_FOR - 1)]
bar = IncrementalBar("PROGRESS", max=len(mylist))


def writer(arr=mr_assembler) -> None:
    print("\n")
    book = xlsxwriter.Workbook("/Users/nazarijbeketov/Desktop/www/articles.xlsx")
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


writer()
