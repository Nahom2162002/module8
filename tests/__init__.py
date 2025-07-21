#tests/playwright_tests.py

import re 
from playwright.sync_api import Page, expect 
from main import * 

def test_has_title(page: Page):
    page.goto("http://127.0.0.1:8000/")

    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("http://127.0.0.1:8000/")

    page.get_by_role("link", name="Get started").click()

    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

def test_number_input(page: Page):
    page.goto("http://127.0.0.1:8000/")

    page.get_by_role("textbox").fill("2")
    expect(page.get_by_role("textbox")).to_be_visible()

    page.get_by_role("textbox").fill("3")
    expect(page.get_by_role("textbox")).to_be_visible()

def test_operation_buttons(page: Page):
    page.goto("http://127.0.0.1:8000/")

    page.get_by_role("textbox").press("Left Click")