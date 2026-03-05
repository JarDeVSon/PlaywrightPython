"""
Page Object Model for The Marketing Cloud Platform Products Page
https://www.themarketingcloud.com/platform#products
"""

from playwright.sync_api import Page, Locator


class MarketingCloudPlatformPage:
    """Page Object for The Marketing Cloud Platform page with product marketplace."""

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.themarketingcloud.com/platform#products"

    # Category filter buttons - using text locators as they may not be standard buttons
    @property
    def all_products_filter(self) -> Locator:
        """Filter button for all products."""
        return self.page.locator("button:has-text('All Products')").first

    @property
    def market_research_filter(self) -> Locator:
        """Filter button for Market Research category."""
        return self.page.locator("button:has-text('Market Research')").first

    @property
    def communications_filter(self) -> Locator:
        """Filter button for Communications category."""
        return self.page.locator("button:has-text('Communications')").first

    @property
    def creative_media_filter(self) -> Locator:
        """Filter button for Creative & Media category."""
        return self.page.locator("button:has-text('Creative & Media')").first

    # Product cards and their Learn More buttons
    def get_product_card(self, product_name: str) -> Locator:
        """Get a specific product card by name."""
        return self.page.locator(f"text={product_name}").first

    def get_product_learn_more_link(self, product_name: str) -> Locator:
        """Get the 'Learn More' link for a specific product."""
        # Find the product name and then get the Learn More link in that section
        return self.page.locator(f"a:has-text('{product_name}')").first

    # Sign up and demo buttons
    @property
    def sign_up_button(self) -> Locator:
        """Sign up CTA button."""
        return self.page.get_by_role("link", name="Sign up").first

    @property
    def request_demo_button(self) -> Locator:
        """Request demo button."""
        return self.page.get_by_role("link", name="Request demo").first

    # Form fields for demo request
    @property
    def first_name_input(self) -> Locator:
        """First name input field."""
        return self.page.locator('input[placeholder*="First name"], input[name*="first"]').first

    @property
    def last_name_input(self) -> Locator:
        """Last name input field."""
        return self.page.locator('input[placeholder*="Last name"], input[name*="last"]').first

    @property
    def email_input(self) -> Locator:
        """Email input field."""
        return self.page.locator('input[type="email"], input[placeholder*="Email"]').first

    @property
    def job_title_input(self) -> Locator:
        """Job title input field."""
        return self.page.locator('input[placeholder*="Job title"], input[name*="job"]').first

    @property
    def company_name_input(self) -> Locator:
        """Company name input field."""
        return self.page.locator('input[placeholder*="Company"], input[name*="company"]').first

    @property
    def product_interest_dropdown(self) -> Locator:
        """Product interest dropdown field."""
        return self.page.locator('select, input[placeholder*="products"]').first

    @property
    def submit_button(self) -> Locator:
        """Form submit button."""
        return self.page.locator('button:has-text("Submit")').first

    # Navigation methods
    def navigate(self) -> None:
        """Navigate to the Marketing Cloud Platform page."""
        self.page.goto(self.url)
        self.page.wait_for_load_state("domcontentloaded")

    def filter_by_category(self, category: str) -> None:
        """Filter products by category."""
        if category == "All Products":
            self.all_products_filter.click()
        elif category == "Market Research":
            self.market_research_filter.click()
        elif category == "Communications":
            self.communications_filter.click()
        elif category == "Creative & Media":
            self.creative_media_filter.click()
        else:
            raise ValueError(f"Unknown category: {category}")
        # Wait for filtering to complete
        self.page.wait_for_timeout(500)

    def click_learn_more(self, product_name: str) -> None:
        """Click the Learn More link for a specific product."""
        # Find and click the learn more link for this product
        learn_more = self.page.locator(f"a:has-text('{product_name}')").first
        learn_more.click()

    def submit_demo_request(
        self,
        first_name: str,
        last_name: str,
        email: str,
        job_title: str,
        company_name: str,
    ) -> None:
        """Fill and submit the demo request form."""
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.email_input.fill(email)
        self.job_title_input.fill(job_title)
        self.company_name_input.fill(company_name)
        self.submit_button.click()

    def get_form_error_message(self) -> Locator:
        """Get form error message if present."""
        return self.page.locator('[role="alert"]')

    def verify_product_visible(self, product_name: str) -> bool:
        """Verify if a product is visible on the page."""
        try:
            return self.get_product_card(product_name).is_visible(timeout=5000)
        except:
            return False
