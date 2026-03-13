# Playwright Python Test Automation - The Heroku App The Internet. Login Demo

A comprehensive Playwright test automation suite for """Test suite for the Login Page of The Internet.""" using Python and Pytest.

## 📋 Project Overview

This project is a complete end-to-end test automation framework using Playwright's sync API with Python. It tests """Test suite for the Login Page of The Internet.""" and includes modern testing practices such as Page Object Model, parallel execution, multi-browser testing, and detailed HTML reporting with screenshots and videos.

## 📁 Project Structure

```
.
├── conftest.py                          # Pytest fixtures and hooks for browser/page setup
├── pytest.ini                           # Pytest configuration (multi-browser, parallel, reporting)
├── requirements.txt                     # Python dependencies
├── README.md                            # This file
├── pages/
│   └── feature_login_page.py            # Page Object Model for Login 
├── tests/
│   ├── __pycache__/
│   └── test_feature_login.py            # """Test suite for the Login Page of The Internet."""
├── utils/
|   |___ highlight.py                    # Utility functions (All Expected Validations In Highlight)
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

**Total Tests: 26 (All Passing ✅)**

### Test Suites[DEMO]:

1. **"""Test suite for the Login Page of The Internet."""** (1 tests)
   - Login into Secure Area with valid credentials.


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
pytest tests/test_feature_login.py -v
```

Run tests with specific browser:
```bash
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit
```

Run a single test:
```bash
pytest tests/test_feature_login.py::test_login_page_object -v
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

### LoginPage
Location: `pages/feature_login_page.py`

**Key Features:**
- Encapsulates all element locators
- Provides reusable methods for page interactions
- Separates test logic from locator management

**Main Methods:**
- `login()` - Perform login action with given credentials. 

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
# Run all tests
pytest pytest tests/test_feature_login.py -v

# Run specific tests
pytest pytest tests/test_feature_login.py::test_login_page_object -v
```

### Debugging Tests
```bash
# Run with verbose output
pytest -vv

# Run with print statements captured
pytest -s

# Run single test with detailed output
pytest pytest tests/test_feature_login.py::test_login_page_object -vv -s

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

**Last Updated**: March 13, 2026  
**Test Status**: ✅ 1/1 Passing  
**Python Version**: 3.14.3  
**Playwright Version**: 1.58.0+
