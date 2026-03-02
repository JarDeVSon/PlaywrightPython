# Playwright Python Testing Suite

A comprehensive test automation project using Playwright with Python and Pytest.

## Project Overview

This project provides an automated testing framework for web applications using Playwright's sync API. It includes fixtures for browser and page management, HTML reporting, video/screenshot capture on failures, and distributed test execution capabilities.

## Project Structure

```
.
├── conftest.py                 # Pytest fixtures for browser and page setup
├── pytest.local.ini            # Local test configuration
├── pytest.ci.ini               # CI/CD test configuration
├── requirements.txt            # Python dependencies
├── tests/
│   └── test_example.py         # Example test cases
├── pages/                      # Page Object Model classes (future)
├── utils/                      # Utility functions and helpers
└── test-results/
    └── report.html             # HTML test reports
```

## Requirements

- Python 3.8+
- Playwright 1.58.0+
- Pytest 9.0.2+
- pytest-playwright for Playwright integration
- pytest-xdist for parallel test execution

See [requirements.txt](requirements.txt) for the complete list of dependencies.

## Setup

1. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Playwright browsers:**
   ```bash
   playwright install
   ```

## Running Tests

### Local Environment
Run tests with headed browser, visual debugging, and video/screenshot capture on failure:
```bash
pytest -c pytest.ini
```

**Features:**
- Headed browser mode for visual debugging
- Slow motion (200ms) for easier observation
- Video recording on failure
- Screenshots on failure
- Tracing on failure

### CI/CD Environment
Run tests in headless mode with parallel execution:
```bash
pytest -c pytest.ini
```

**Features:**
- Headless browser mode
- Parallel test execution (auto-detects number of CPU cores)
- HTML reports with self-contained content
- Screenshots on failure
- Optimized for CI/CD pipelines

## Test Configuration

Both configurations generate HTML reports in the `reports/` directory with detailed test results and artifacts.

## Key Dependencies

- **playwright**: Browser automation library
- **pytest**: Test framework
- **pytest-playwright**: Pytest plugin for Playwright integration
- **pytest-xdist**: Parallel test execution
- **requests**: HTTP library for API testing

## Fixtures

The `conftest.py` provides:
- `browser`: Session-scoped Chromium browser instance
- `page`: Function-scoped page for individual tests