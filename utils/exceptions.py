class RetroPostException(Exception):
    """Base exception for RetroPost application"""
    pass

class APIError(RetroPostException):
    """Raised when API calls fail"""
    pass

class ScrapingError(RetroPostException):
    """Raised when web scraping fails"""
    pass
