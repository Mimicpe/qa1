import re
import pytest 
from playwright.sync_api import Page, expect

BASE_URL = "https://dnd.su"

@pytest.mark.parametrize("query", ["Изобретатель"])
def test_search_results(page: Page, query: str):
    #Позитивный сценарий: поиск по известному слову возвращает результаты
    page.goto(BASE_URL)
    search = page.get_by_role("searchbox", name ="Поиск по сайту")
    search.fill(query)
    search.press("Enter")

    expect(page.get_by_role("link", name=re.compile(query))).to_be_visible()


@pytest.mark.parametrize("query", [
    "",
    "   ",
    "<b>x</b>",
    "'\"%_;--",
    "a" * 500,
])

def test_search_empty(page: Page, query: str):
    page.goto(BASE_URL)
    search = page.get_by_role("searchbox", name ="Поиск по сайту")
    search.fill(query)
    search.press("Enter")

    expect(search).to_be_visible()
