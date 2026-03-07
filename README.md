# Playwright Python Test Automation - Marketing Cloud Platform

A comprehensive Playwright test automation suite for The Marketing Cloud Platform using Python and Pytest.

## 📋 Project Overview

This project is a complete end-to-end test automation framework using Playwright's sync API with Python. It tests https://www.themarketingcloud.com/platform#products and includes modern testing practices such as Page Object Model, parallel execution, multi-browser testing, and detailed HTML reporting with screenshots and videos.

## 📁 Project Structure

```
.
├── conftest.py                          # Pytest fixtures and hooks for browser/page setup
├── pytest.ini                           # Pytest configuration (multi-browser, parallel, reporting)
├── requirements.txt                     # Python dependencies
├── README.md                            # This file
├── pages/
│   └── marketing_cloud_platform_page.py # Page Object Model for Marketing Cloud Platform
├── tests/
│   ├── __pycache__/
│   └── test_marketing_cloud_platform.py # 35 comprehensive test cases
├── utils/                               # Utility functions (future expansion)
├── report/
│   └── index.html                       # Generated HTML test report
├── .github/workflows/
│   ├── generate_tests.prompt.md         # Test generation guidelines
│   └── playwright.yml                   # GitHub Actions CI/CD pipeline
└── .gitignore                           # Git ignore rules
```

## ✨ Key Features

- **Multi-Browser Testing**: Runs tests on Chromium, Firefox, and WebKit
- **Parallel Execution**: Uses pytest-xdist for auto-detected parallel test runs
- **Page Object Model**: Clean separation of locators and test logic
- **Comprehensive Reporting**: Self-contained HTML reports with full-page screenshots
- **Visual Debugging**: Slow motion (200ms), video on failure, and trace recording
- **CI/CD Ready**: GitHub Actions workflow configured and ready to deploy
- **Auto-Retrying**: Built-in Playwright waits with no manual timeouts

## 📊 Test Coverage

**Total Tests: 35 (All Passing ✅)**

### Test Suites:
1. **Navigation & Loading** (4 tests)
   - Page navigation verification
   - Category filters visibility
   - Sign up and demo links

2. **Product Visibility** (8 tests)
   - QuestBrand, QuestDIY, BERA.ai, QuestIC
   - Influence, SmartAssets, CUE, TPP Insights

3. **Learn More Links** (6 tests)
   - Product marketplace link verification
   - Navigation to product detail pages

4. **Content & Structure** (5 tests)
   - Section headers (Market Research, Communications, Creative & Media)
   - Product Marketplace and Platform headings

5. **Navigation Controls** (4 tests)
   - Category filter visibility

6. **User Actions** (4 tests)
   - Sign up button functionality
   - Demo request link behavior

7. **Legacy Tests** (test_example.py - 3 tests)
   - Basic Playwright examples

## 🛠️ Tech Stack

- **Playwright**: 1.58.0+ - Browser automation
- **Python**: 3.14.3
- **Pytest**: 8.2.2 - Test framework
- **pytest-playwright**: 0.7.2 - Playwright plugin
- **pytest-xdist**: 3.8.0 - Parallel execution
- **pytest-html**: 4.1.1 - HTML reporting
- **pytest-base-url**: 2.1.0 - Base URL configuration

See [requirements.txt](requirements.txt) for the complete dependency list.

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.8 or higher
- Git

### 2. Setup

Clone and setup the project:
```bash
# Clone the repository
git clone <repository-url>
cd PlaywrightPython

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install
```

### 3. Run Tests

Run all tests with parallel execution:
```bash
pytest
```

Run tests for a specific module:
```bash
pytest tests/test_marketing_cloud_platform.py -v
```

Run tests with specific browser:
```bash
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit
```

Run a single test:
```bash
pytest tests/test_marketing_cloud_platform.py::TestProductVisibility::test_questbrand_product_visible -v
```

Run in headed mode (see browser):
```bash
pytest --headed
```

## 📋 Test Configuration

The `pytest.ini` file configures:

- **Multi-browser Testing**: Chromium, Firefox, WebKit
- **Parallel Execution**: `-n auto` (auto-detects CPU cores)
- **Visual Debugging**:
  - Slow motion: 200ms delay
  - Screenshot: on failure only
  - Video: on failure only
  - Tracing: on failure only
- **Reporting**:
  - Self-contained HTML report
  - Full-page screenshots embedded
  - Report location: `report/index.html`
- **Test Discovery**: 
  - Test paths: `tests/`
  - Test files: `test_*.py`

## 📖 Page Object Model

### MarketingCloudPlatformPage
Location: `pages/marketing_cloud_platform_page.py`

**Key Features:**
- Encapsulates all element locators
- Provides reusable methods for page interactions
- Separates test logic from locator management

**Main Methods:**
- `navigate()` - Navigate to the platform page
- `filter_by_category(category)` - Filter products by category
- `verify_product_visible(product_name)` - Check product visibility
- `submit_demo_request(...)` - Fill and submit demo form
- Various property accessors for elements

## 📈 Execution Details

### Local Testing
```bash
pytest
```
- Runs on all three browsers (Chromium, Firefox, WebKit)
- 8 parallel workers (auto-detected)
- Videos and screenshots on failure
- Slow motion enabled
- Full HTML report generated

### Continuous Integration
The GitHub Actions workflow runs:
- Headless mode
- Optimized for CI/CD
- Parallel execution
- HTML reports as artifacts

## 📊 HTML Reports

After test execution, detailed HTML reports are generated at:
- **Local**: `report/index.html`
- **CI/CD**: Download from GitHub Actions artifacts

**Report Includes:**
- Test summary (passed/failed/skipped)
- Test execution time
- Full-page screenshots for each test
- Browser and platform information
- Test metadata

## 🔍 Best Practices Implemented

✅ **Page Object Model** - Clean separation of concerns  
✅ **No Hard Timeouts** - Relies on Playwright's built-in waits  
✅ **Role-Based Locators** - Uses accessible selectors (get_by_role)  
✅ **Auto-Retrying Assertions** - Playwright handles automatic retries  
✅ **Descriptive Test Names** - Clear test intent  
✅ **Comprehensive Documentation** - Comments and docstrings  
✅ **Parallel Execution** - Tests run efficiently  
✅ **Visual Debugging** - Screenshots and videos for failed tests  

## 🐛 Troubleshooting

### Playwright Not Found
```bash
playwright install
```

### Permission Denied on .venv
```bash
chmod +x .venv/bin/activate
```

### Tests Failing with Timeout
- Increase wait time in code (if needed)
- Check network connectivity
- Verify target website is accessible

### Report Not Generated
- Check `report/` directory exists
- Verify pytest-html is installed: `pip install pytest-html`

## 📝 Test Examples

### Running Specific Test Classes
```bash
# Run all product visibility tests
pytest tests/test_marketing_cloud_platform.py::TestProductVisibility -v

# Run all navigation tests
pytest tests/test_marketing_cloud_platform.py::TestMarketingCloudPlatformNavigation -v
```

### Debugging Tests
```bash
# Run with verbose output
pytest -vv

# Run with print statements captured
pytest -s

# Run single test with detailed output
pytest tests/test_marketing_cloud_platform.py::TestProductVisibility::test_questbrand_product_visible -vv -s

# Run in debbug mode (see browser):
PWDEBUG=1 pytest -s

# Run in Browser Developer Tools debbug mode (see browser):
PWDEBUG=console pytest -s
```

## 🔐 Fixtures

The `conftest.py` provides:
- **`browser`**: Session-scoped Chromium browser instance
- **`page`**: Function-scoped page for each test
- **Screenshot hooks**: Automatic full-page screenshots on test completion
- **HTML report enhancements**: Custom styling and formatting

## 📦 Dependencies Management

Update dependencies:
```bash
pip install -r requirements.txt --upgrade
```

Check for outdated packages:
```bash
pip list --outdated
```

## 🔄 CI/CD Integration

The project includes a GitHub Actions workflow (`playwright.yml`) that:
- Runs on push to main/develop branches
- Executes tests in headless mode
- Generates and uploads HTML reports
- Supports multiple Python versions

## 📚 Resources

- [Playwright Documentation](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [pytest-xdist Parallel Execution](https://pytest-xdist.readthedocs.io/)

## 📝 License

This project is provided as-is for testing automation purposes.

---

**Last Updated**: March 5, 2026  
**Test Status**: ✅ 35/35 Passing  
**Python Version**: 3.14.3  
**Playwright Version**: 1.58.0+
