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

        # Category filter buttons
        self.all_products_filter = page.locator("button:has-text('All Products')")
        self.market_research_filter = page.locator("button:has-text('Market Research')")
        self.communications_filter = page.locator("button:has-text('Communications')")
        self.creative_media_filter = page.locator("button:has-text('Creative & Media')")

        # Sign up and demo buttons
        self.sign_up_button = page.get_by_role("link", name="Sign up")
        self.request_demo_button = page.get_by_role("link", name="Request demo")

        # Form fields for demo request
        self.first_name_input = page.locator('input[placeholder*="First name"], input[name*="first"]')
        self.last_name_input = page.locator('input[placeholder*="Last name"], input[name*="last"]')
        self.email_input = page.locator('input[type="email"], input[placeholder*="Email"]')
        self.job_title_input = page.locator('input[placeholder*="Job title"], input[name*="job"]')
        self.company_name_input = page.locator('input[placeholder*="Company"], input[name*="company"]')
        self.product_interest_dropdown = page.locator('select, input[placeholder*="products"]')
        self.submit_button = page.locator('button:has-text("Submit")')

        # Form error message
        self.form_error_message = page.locator('[role="alert"]')

    # Navigation methods
    def navigate(self) -> None:
        """Navigate to the Marketing Cloud Platform page."""
        self.page.goto(self.url)
        self.page.wait_for_load_state("domcontentloaded")

    # Product cards (dynamic methods that take parameters)
    def get_product_card(self, product_name: str) -> Locator:
        """Get a specific product card by name."""
        return self.page.locator(f"text={product_name}").first

    def get_product_learn_more_link(self, product_name: str) -> Locator:
        """Get the 'Learn More' link for a specific product."""
        return self.page.locator(f"a:has-text('{product_name}')").first

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

    def verify_product_visible(self, product_name: str) -> bool:
        """Verify if a product is visible on the page."""
        try:
            return self.get_product_card(product_name).is_visible(timeout=5000)
        except:
            return False
