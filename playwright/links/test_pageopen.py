import re
from playwright.sync_api import Page, expect
#нужно проверить, что кнопк ведут на правильные адреса
BASE_URL = "https://dnd.su"

def test_home_opens(page: Page):
    page.goto(BASE_URL)
    expect(page.get_by_role("link", name="Заклинания").first).to_be_visible()
def test_menu_spells_link(page: Page):
    page.goto(BASE_URL)
    page.get_by_role("link", name="Заклинания").first.click()
    expect(page).to_have_url(re.compile("/spells/"))
def test_menu_class_link(page: Page):
    page.goto(BASE_URL)
    page.get_by_role("link", name="Классы").first.click()
    expect(page).to_have_url(re.compile("/class/"))
def test_menu_races_link(page: Page):
    page.goto(BASE_URL)
    page.get_by_role("link", name="Расы и происхождения").first.click()
    expect(page).to_have_url(re.compile("/race/"))
def test_menu_backgrounds_link(page: Page):
    page.goto(BASE_URL)
    page.get_by_role("link", name="Предыстории").first.click()
    expect(page).to_have_url(re.compile("/backgrounds/"))
def test_menu_feats_link(page: Page):
    page.goto(BASE_URL)
    page.get_by_role("link", name="Черты").first.click()
    expect(page).to_have_url(re.compile("/feats/"))
def test_menu_bestiary_link(page: Page):
    page.goto(BASE_URL)
    page.get_by_role("link", name="Бестиарий").first.click()
    expect(page).to_have_url(re.compile("/bestiary/"))
def test_items_links(page: Page):
    page.goto(BASE_URL)
    page.get_by_role("link", name="Магические предметы").first.click()
    expect(page).to_have_url(re.compile("/items/"))

