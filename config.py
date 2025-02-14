from typing import Dict, Any

SCRAPING_CONFIG: Dict[str, Any] = {
    'days_threshold': 15,
    'base_url': 'https://retrododo.com/category/news/',
    'data_directory': 'data',
    'request_timeout': 30,  # Add timeout for requests
    'max_retries': 3  # Add retry attempts
}

LOGGING_CONFIG: Dict[str, str] = {
    'log_file': 'retropost.log',  # More specific name
    'console_level': 'INFO',
    'file_level': 'ERROR',
    'log_format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
}

MISTRAL_CONFIG: Dict[str, Any] = {
    'model': 'mistral-tiny',
    'max_tokens': 300,
    'temperature': 0.7
}
