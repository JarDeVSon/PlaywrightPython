def highlight(locator):
    """Highlight the element located by the given locator."""
    locator.evaluate(
        """el => {
            el.style.border='3px solid red';
            el.style.backgroundColor='yellow';
        }"""
    )