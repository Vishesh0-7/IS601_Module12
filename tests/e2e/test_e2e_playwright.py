import subprocess, time, os, signal
import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "http://127.0.0.1:8000"

@pytest.fixture(scope="session", autouse=True)
def run_server():
    # Start uvicorn server in background
    proc = subprocess.Popen(
        ["uvicorn", "app.main:app", "--port", "8000"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    # Wait for server to be up
    time.sleep(1.5)
    yield
    # Teardown
    proc.terminate()
    try:
        proc.wait(timeout=3)
    except subprocess.TimeoutExpired:
        os.kill(proc.pid, signal.SIGKILL)

def test_ui_addition():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(BASE_URL, wait_until="domcontentloaded")
        page.fill("#a", "7")
        page.fill("#b", "5")
        page.select_option("#op", "add")
        page.click("#go")
        page.wait_for_selector("#result")
        assert "Result: 12" in page.inner_text("#result")
        browser.close()

def test_ui_div_by_zero():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(BASE_URL, wait_until="domcontentloaded")
        page.fill("#a", "1")
        page.fill("#b", "0")
        page.select_option("#op", "div")
        page.click("#go")
        page.wait_for_selector("#result")
        assert "Error" in page.inner_text("#result")
        browser.close()
