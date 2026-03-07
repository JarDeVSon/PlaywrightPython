import pytest_html
import pytest
import base64
from playwright.sync_api import sync_playwright
from pages.marketing_cloud_platform_page import MarketingCloudPlatformPage
from pytest_metadata.plugin import metadata

@pytest.fixture(scope="session")
def browser():
    """Provide a browser instance for the test session."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    """Provide a new page for each test."""
    page = browser.new_page()
    yield page
    page.close()


@pytest.fixture
def platform_page(page):
    """Fixture to provide MarketingCloudPlatformPage instance."""
    return MarketingCloudPlatformPage(page)

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.clear()
    metadata["Base URL"] = config.getoption("--base-url") if hasattr(config.option, "base_url") else "N/A"
    
def pytest_html_report_title(report):
    report.title = "Automation Report - Playwright Python"

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    metadata.pop("Packages", None)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    page = item.funcargs.get("page", None)

    if page:
        screenshot_bytes = page.screenshot(full_page=True)
        screenshot_base64 = base64.b64encode(screenshot_bytes).decode("utf-8")

        status_color = "#28a745" if report.passed else "#dc3545"
        status_text = "SUCCESS" if report.passed else "FAILURE"

        html = f"""
        <div style="border:2px solid {status_color}; padding:10px; margin-top:10px;">
            <h3 style="color:{status_color};">
                {status_text} - {item.name}
            </h3>
            <img src="data:image/png;base64,{screenshot_base64}"
                 style="width:600px; border-radius:8px;"
                 onclick="window.open(this.src)"
            />
        </div>
        """

        extra = getattr(report, "extras", [])
        extra.append(pytest_html.extras.html(html))
        report.extras = extra

