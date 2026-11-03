import re
import pytest
from playwright.sync_api import Page, expect

SITE = "https://dnd.su"

SECTIONS = [
    pytest.param("/spells/", "Уровень", "2", ".cards_list__item-name", id="spells"),
    pytest.param("/backgrounds/", "Навыки", "Акробатика", ".list-item-title", id="backgrounds"),
    pytest.param("/feats/", "Характеристики", "Сила", ".list-item-title", id="feats"),
    pytest.param("/bestiary/", "Размер", "Средний", ".list-item-title", id="bestiarity"),
    pytest.param("/items/", "Тип", "Доспех", ".list-item-title", id="items"),
]

@pytest.mark.parametrize("path, filter_name, option, locator", SECTIONS)
def test_filter_survive_back(page: Page, path, filter_name, option, locator):
    page.goto(SITE + path)
    links = page.locator(locator)
    expect(links.first).to_be_visible()
    visible_links = links.filter(visible=True)
    total = links.count()

    fit = page.get_by_placeholder(filter_name)
    print("До фильтра:", total)
    fit.click() 

    dropdown = page.locator(".if-dropdown-block.active")
    option_locator = dropdown.get_by_text(option, exact=True)

    print("Активных списков:", dropdown.count())
    print("Найдено вариантов:", option_locator.count())

    option_locator.click()

    chosen = fit.input_value()
    filtered_links = links.filter(visible=True)
    filtered = filtered_links.count()

    print("Выбранное значение:", chosen)
    print("Видимых записей после фильтра:", filtered)
    print("Первые записи:", links.all_text_contents()[:10])
    visible_links = page.locator(locator).filter(visible=True)
    print("Видимых записей:", visible_links.count())
    expect(links).not_to_have_count(total)

    filtered = links.count()
    
    chosen = fit.input_value()

    assert chosen not in ("", "[]"), "Фильтр не выбрался"

    url_before = page.url
    
    filtered_links.first.click()

    expect(page).not_to_have_url(url_before)
    
    page.go_back()

    expect(fit).to_have_value(chosen)
    expect(links.filter(visible=True)).to_have_count(filtred)
