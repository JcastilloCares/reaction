import pytest
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    parser.addoption(
        '--headless',
        action='store_true',
        default=False,
        help='Run the browser in headless mode'
    )


@pytest.fixture
def browser(request):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()


def test_dark_mode_toggle(browser):
    page = browser.new_page()

    page.goto('http://localhost:3000')

    toggle_button = page.wait_for_selector('.App button')

    assert toggle_button.text_content() == 'Switch to Night Mode'

    toggle_button.click()
    page.wait_for_timeout(1000)  # Wait for 1 second
    assert toggle_button.text_content() == 'Switch to Day Mode'

    toggle_button.click()
    page.wait_for_timeout(1000)  # Wait for 1 second
    assert toggle_button.text_content() == 'Switch to Night Mode'
