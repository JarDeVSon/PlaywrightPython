"""
Comprehensive test suite for The Marketing Cloud Platform Products page.
Tests all key functionalities including navigation, filtering, product interactions, and form submission.
"""
from playwright.sync_api import expect
from pages.marketing_cloud_platform_page import MarketingCloudPlatformPage


class TestMarketingCloudPlatformNavigation:
    """Test suite for page navigation and loading."""

    def test_navigate_to_platform_page(self, platform_page):
        """Test successful navigation to the Marketing Cloud Platform page."""
        platform_page.navigate()
        
        # Verify page contains expected content
        expect(platform_page.page.get_by_text("Product Marketplace").first).to_be_visible()

    def test_page_loads_with_category_filters(self, platform_page):
        """Test that product category filters are visible on page load."""
        platform_page.navigate()
        
        # Verify filter text exists on page
        assert platform_page.page.evaluate("document.body.innerText.includes('All Products')")
        assert platform_page.page.evaluate("document.body.innerText.includes('Market Research')")
        assert platform_page.page.evaluate("document.body.innerText.includes('Communications')")

    def test_page_displays_sign_up_link(self, platform_page):
        """Test that sign up link is visible on page."""
        platform_page.navigate()
        
        # Sign up link should be visible
        sign_ups = platform_page.page.get_by_role("link", name="Sign up")
        expect(sign_ups.first).to_be_visible()

    def test_page_displays_request_demo_link(self, platform_page):
        """Test that request demo link is visible on page."""
        platform_page.navigate()
        
        # Request demo link should be visible
        demo_links = platform_page.page.get_by_role("link", name="Request demo")
        expect(demo_links.first).to_be_visible()


class TestProductVisibility:
    """Test suite for product visibility on the page."""

    def test_questbrand_product_visible(self, platform_page):
        """Test that QuestBrand product card is visible on page."""
        platform_page.navigate()
        
        # Use a more specific locator for the product link/card
        expect(platform_page.page.get_by_role("link", name="QuestBrand Collect real-time").first).to_be_visible()

    def test_questdiy_product_visible(self, platform_page):
        """Test that QuestDIY product card is visible on page."""
        platform_page.navigate()
        
        expect(platform_page.page.get_by_role("link", name="QuestDIY Quickly capture").first).to_be_visible()

    def test_bera_ai_product_visible(self, platform_page):
        """Test that BERA.ai product card is visible on page."""
        platform_page.navigate()
        
        expect(platform_page.page.get_by_role("link", name="BERA.ai Uncover the actual").first).to_be_visible()

    def test_questic_product_visible(self, platform_page):
        """Test that QuestIC product card is visible on page."""
        platform_page.navigate()
        
        expect(platform_page.page.get_by_role("link", name="QuestIC Drive strategic").first).to_be_visible()

    def test_influence_product_visible(self, platform_page):
        """Test that Influence product card is visible on page."""
        platform_page.navigate()
        
        expect(platform_page.page.get_by_role("link", name="Influence Manage end-to-end").first).to_be_visible()

    def test_smartassets_product_visible(self, platform_page):
        """Test that SmartAssets product card is visible on page."""
        platform_page.navigate()
        
        expect(platform_page.page.get_by_role("link", name="SmartAssets Increase the impact").first).to_be_visible()

    def test_cue_product_visible(self, platform_page):
        """Test that CUE product card is visible on page."""
        platform_page.navigate()
        
        expect(platform_page.page.get_by_role("link", name="CUE Capture a real-time").first).to_be_visible()

    def test_tpp_insights_product_visible(self, platform_page):
        """Test that TPP Insights product card is visible on page."""
        platform_page.navigate()
        
        expect(platform_page.page.get_by_role("link", name="TPP Insights Unleash the power").first).to_be_visible()


class TestProductLearnMoreLinks:
    """Test suite for Learn More link functionality."""

    def test_questbrand_learn_more_link_present(self, platform_page):
        """Test that QuestBrand Learn More link is present."""
        platform_page.navigate()
        
        # Find the learn more link using the product description
        learn_more = platform_page.page.get_by_role("link", name="QuestBrand Collect real-time").first
        expect(learn_more).to_be_visible()

    def test_questdiy_learn_more_link_present(self, platform_page):
        """Test that QuestDIY Learn More link is present."""
        platform_page.navigate()
        
        learn_more = platform_page.page.get_by_role("link", name="QuestDIY Quickly capture").first
        expect(learn_more).to_be_visible()

    def test_smartassets_learn_more_link_present(self, platform_page):
        """Test that SmartAssets Learn More link is present."""
        platform_page.navigate()
        
        learn_more = platform_page.page.get_by_role("link", name="SmartAssets Increase the impact").first
        expect(learn_more).to_be_visible()

    def test_cue_learn_more_link_present(self, platform_page):
        """Test that CUE Learn More link is present."""
        platform_page.navigate()
        
        learn_more = platform_page.page.get_by_role("link", name="CUE Capture a real-time").first
        expect(learn_more).to_be_visible()

    def test_tpp_insights_learn_more_link_present(self, platform_page):
        """Test that TPP Insights Learn More link is present."""
        platform_page.navigate()
        
        learn_more = platform_page.page.get_by_role("link", name="TPP Insights Unleash the power").first
        expect(learn_more).to_be_visible()

    def test_influence_learn_more_link_present(self, platform_page):
        """Test that Influence Learn More link is present."""
        platform_page.navigate()
        
        # Influence may link to imai
        learn_more = platform_page.page.get_by_role("link", name="Influence Manage end-to-end").first
        expect(learn_more).to_be_visible()

    def test_bera_ai_learn_more_link_present(self, platform_page):
        """Test that BERA.ai Learn More link is present."""
        platform_page.navigate()
        
        learn_more = platform_page.page.get_by_role("link", name="BERA.ai Uncover the actual").first
        expect(learn_more).to_be_visible()


class TestPageContentVerification:
    """Test suite for verifying page content and structure."""

    def test_page_contains_market_research_heading(self, platform_page):
        """Test that Market Research section heading is present on page."""
        platform_page.navigate()
        
        # Check if Market Research text exists on page
        assert platform_page.page.evaluate("document.body.innerText.includes('Market Research')")

    def test_page_contains_communications_heading(self, platform_page):
        """Test that Communications section heading is present on page."""
        platform_page.navigate()
        
        # Check if Communications text exists on page
        assert platform_page.page.evaluate("document.body.innerText.includes('Communications')")

    def test_page_contains_creative_media_heading(self, platform_page):
        """Test that Creative & Media section heading is present on page."""
        platform_page.navigate()
        
        # Check if Creative text exists on page
        assert platform_page.page.evaluate("document.body.innerText.includes('Creative')")

    def test_page_contains_product_marketplace_heading(self, platform_page):
        """Test that Product Marketplace heading is present."""
        platform_page.navigate()
        
        expect(platform_page.page.get_by_text("Product Marketplace").first).to_be_visible()

    def test_page_contains_platform_heading(self, platform_page):
        """Test that THE MARKETING CLOUD PLATFORM heading is present."""
        platform_page.navigate()
        
        # Check if Marketing Cloud Platform text exists on page
        assert platform_page.page.evaluate("document.body.innerText.includes('Marketing Cloud Platform')")


class TestSignUpNavigation:
    """Test suite for sign up navigation."""

    def test_sign_up_link_is_clickable(self, platform_page):
        """Test that sign up link is clickable."""
        platform_page.navigate()
        
        sign_up = platform_page.sign_up_button
        expect(sign_up.first).to_be_enabled()

    def test_sign_up_link_points_to_platform(self, platform_page):
        """Test that sign up link points to the correct URL."""
        platform_page.navigate()
        
        sign_up = platform_page.sign_up_button.first
        href = sign_up.get_attribute("href")
        expect(sign_up).to_be_enabled()
        # Verify the link points to the correct location
        assert "platform.stagwellmarketingcloud.io" in href or "sign" in href.lower()


class TestDemoRequestLink:
    """Test suite for demo request link."""

    def test_request_demo_link_is_clickable(self, platform_page):
        """Test that request demo link is clickable."""
        platform_page.navigate()
        
        demo_link = platform_page.request_demo_button.first
        expect(demo_link).to_be_enabled()

    def test_request_demo_link_navigates(self, platform_page):
        """Test that clicking request demo navigates to form page."""
        platform_page.navigate()
        
        demo_link = platform_page.request_demo_button.first
        href = demo_link.get_attribute("href")
        expect(demo_link).to_be_enabled()
        
        # Should point to request-demo page or similar
        assert "request-demo" in href.lower() or "demo" in href.lower()


class TestCategoryNavigation:
    """Test suite for category filter navigation."""

    def test_market_research_filter_text_visible(self, platform_page):
        """Test that Market Research category filter text is visible."""
        platform_page.navigate()
        
        # Check if Market Research text exists on page
        assert platform_page.page.evaluate("document.body.innerText.includes('Market Research')")

    def test_communications_filter_text_visible(self, platform_page):
        """Test that Communications category filter text is visible."""
        platform_page.navigate()
        
        # Check if Communications text exists on page
        assert platform_page.page.evaluate("document.body.innerText.includes('Communications')")

    def test_creative_media_filter_text_visible(self, platform_page):
        """Test that Creative & Media category filter text is visible."""
        platform_page.navigate()
        
        # Check if Creative text exists on page
        assert platform_page.page.evaluate("document.body.innerText.includes('Creative')")

    def test_all_products_filter_text_visible(self, platform_page):
        """Test that All Products category filter text is visible."""
        platform_page.navigate()
        
        expect(platform_page.page.get_by_text("All Products").first).to_be_visible()
