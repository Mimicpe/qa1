import pytest

BASE_URL = "https:/dnd.su"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture
def page(browser):
    ctx = browser.new_context(locale="ru-RU", viewport={"width": 1366, "height": 800})
    p = ctx.new_page()
    p.set_default_timeout(10_000)
    yield p
    ctx.close()
