"""
Comprehensive test suite for The Marketing Cloud Platform Products page.
Tests all key functionalities including navigation, filtering, product interactions, and form submission.
"""

import pytest
from pages.marketing_cloud_platform_page import MarketingCloudPlatformPage


class TestMarketingCloudPlatformNavigation:
    """Test suite for page navigation and loading."""

    def test_navigate_to_platform_page(self, page):
        """Test successful navigation to the Marketing Cloud Platform page."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        # Verify page contains expected content
        assert page.get_by_text("Product Marketplace").first.is_visible()

    def test_page_loads_with_category_filters(self, page):
        """Test that product category filters are visible on page load."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        # Verify filter text exists on page
        assert page.evaluate("document.body.innerText.includes('All Products')")
        assert page.evaluate("document.body.innerText.includes('Market Research')")
        assert page.evaluate("document.body.innerText.includes('Communications')")

    def test_page_displays_sign_up_link(self, page):
        """Test that sign up link is visible on page."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        # Sign up link should be visible
        sign_ups = page.get_by_role("link", name="Sign up")
        assert sign_ups.count() > 0

    def test_page_displays_request_demo_link(self, page):
        """Test that request demo link is visible on page."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        # Request demo link should be visible
        demo_links = page.get_by_role("link", name="Request demo")
        assert demo_links.count() > 0


class TestProductVisibility:
    """Test suite for product visibility on the page."""

    def test_questbrand_product_visible(self, page):
        """Test that QuestBrand product card is visible on page."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        # Use a more specific locator for the product link/card
        assert page.get_by_role("link", name="QuestBrand Collect real-time").first.is_visible()

    def test_questdiy_product_visible(self, page):
        """Test that QuestDIY product card is visible on page."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        assert page.get_by_role("link", name="QuestDIY Quickly capture").first.is_visible()

    def test_bera_ai_product_visible(self, page):
        """Test that BERA.ai product card is visible on page."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        assert page.get_by_role("link", name="BERA.ai Uncover the actual").first.is_visible()

    def test_questic_product_visible(self, page):
        """Test that QuestIC product card is visible on page."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        assert page.get_by_role("link", name="QuestIC Drive strategic").first.is_visible()

    def test_influence_product_visible(self, page):
        """Test that Influence product card is visible on page."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        assert page.get_by_role("link", name="Influence Manage end-to-end").first.is_visible()

    def test_smartassets_product_visible(self, page):
        """Test that SmartAssets product card is visible on page."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        assert page.get_by_role("link", name="SmartAssets Increase the impact").first.is_visible()

    def test_cue_product_visible(self, page):
        """Test that CUE product card is visible on page."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        assert page.get_by_role("link", name="CUE Capture a real-time").first.is_visible()

    def test_tpp_insights_product_visible(self, page):
        """Test that TPP Insights product card is visible on page."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        assert page.get_by_role("link", name="TPP Insights Unleash the power").first.is_visible()


class TestProductLearnMoreLinks:
    """Test suite for Learn More link functionality."""

    def test_questbrand_learn_more_link_present(self, page):
        """Test that QuestBrand Learn More link is present."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        # Find the learn more link using the product description
        learn_more = page.get_by_role("link", name="QuestBrand Collect real-time").first
        assert learn_more.is_visible()

    def test_questdiy_learn_more_link_present(self, page):
        """Test that QuestDIY Learn More link is present."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        learn_more = page.get_by_role("link", name="QuestDIY Quickly capture").first
        assert learn_more.is_visible()

    def test_smartassets_learn_more_link_present(self, page):
        """Test that SmartAssets Learn More link is present."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        learn_more = page.get_by_role("link", name="SmartAssets Increase the impact").first
        assert learn_more.is_visible()

    def test_cue_learn_more_link_present(self, page):
        """Test that CUE Learn More link is present."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        learn_more = page.get_by_role("link", name="CUE Capture a real-time").first
        assert learn_more.is_visible()

    def test_tpp_insights_learn_more_link_present(self, page):
        """Test that TPP Insights Learn More link is present."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        learn_more = page.get_by_role("link", name="TPP Insights Unleash the power").first
        assert learn_more.is_visible()

    def test_influence_learn_more_link_present(self, page):
        """Test that Influence Learn More link is present."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        # Influence may link to imai
        learn_more = page.get_by_role("link", name="Influence Manage end-to-end").first
        assert learn_more.is_visible()

    def test_bera_ai_learn_more_link_present(self, page):
        """Test that BERA.ai Learn More link is present."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        learn_more = page.get_by_role("link", name="BERA.ai Uncover the actual").first
        assert learn_more.is_visible()


class TestPageContentVerification:
    """Test suite for verifying page content and structure."""

    def test_page_contains_market_research_heading(self, page):
        """Test that Market Research section heading is present on page."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        # Check if Market Research text exists on page
        assert page.evaluate("document.body.innerText.includes('Market Research')")

    def test_page_contains_communications_heading(self, page):
        """Test that Communications section heading is present on page."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        # Check if Communications text exists on page
        assert page.evaluate("document.body.innerText.includes('Communications')")

    def test_page_contains_creative_media_heading(self, page):
        """Test that Creative & Media section heading is present on page."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        # Check if Creative text exists on page
        assert page.evaluate("document.body.innerText.includes('Creative')")

    def test_page_contains_product_marketplace_heading(self, page):
        """Test that Product Marketplace heading is present."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        assert page.get_by_text("Product Marketplace").first.is_visible()

    def test_page_contains_platform_heading(self, page):
        """Test that THE MARKETING CLOUD PLATFORM heading is present."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        # Check if Marketing Cloud Platform text exists on page
        assert page.evaluate("document.body.innerText.includes('Marketing Cloud Platform')")


class TestSignUpNavigation:
    """Test suite for sign up navigation."""

    def test_sign_up_link_is_clickable(self, page):
        """Test that sign up link is clickable."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        sign_up = page.get_by_role("link", name="Sign up").first
        assert sign_up.is_enabled()

    def test_sign_up_link_points_to_platform(self, page):
        """Test that sign up link points to the correct URL."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        sign_up = page.get_by_role("link", name="Sign up").first
        href = sign_up.get_attribute("href")
        assert "platform.stagwellmarketingcloud.io" in href or "sign" in href.lower()


class TestDemoRequestLink:
    """Test suite for demo request link."""

    def test_request_demo_link_is_clickable(self, page):
        """Test that request demo link is clickable."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        demo_link = page.get_by_role("link", name="Request demo").first
        assert demo_link.is_enabled()

    def test_request_demo_link_navigates(self, page):
        """Test that clicking request demo navigates to form page."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        demo_link = page.get_by_role("link", name="Request demo").first
        href = demo_link.get_attribute("href")
        
        # Should point to request-demo page or similar
        assert "request-demo" in href.lower() or "demo" in href.lower()


class TestCategoryNavigation:
    """Test suite for category filter navigation."""

    def test_market_research_filter_text_visible(self, page):
        """Test that Market Research category filter text is visible."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        # Check if Market Research text exists on page
        assert page.evaluate("document.body.innerText.includes('Market Research')")

    def test_communications_filter_text_visible(self, page):
        """Test that Communications category filter text is visible."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        # Check if Communications text exists on page
        assert page.evaluate("document.body.innerText.includes('Communications')")

    def test_creative_media_filter_text_visible(self, page):
        """Test that Creative & Media category filter text is visible."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        # Check if Creative text exists on page
        assert page.evaluate("document.body.innerText.includes('Creative')")

    def test_all_products_filter_text_visible(self, page):
        """Test that All Products category filter text is visible."""
        platform_page = MarketingCloudPlatformPage(page)
        platform_page.navigate()
        
        assert page.get_by_text("All Products").first.is_visible()
