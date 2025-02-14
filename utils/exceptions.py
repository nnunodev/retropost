class RetroPostError(Exception):
    """Base exception for RetroPost application."""
    pass

class APIError(RetroPostError):
    """Raised when API calls fail."""
    pass

class ScrapingError(RetroPostError):
    """Raised when web scraping fails."""
    pass

class BlueSkyError(RetroPostError):
    """Raised when BlueSky operations fail."""
    pass
