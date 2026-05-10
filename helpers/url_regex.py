import re

def extract_https_urls(text: str) -> list[str]:
    """
    Extracts all https:// links from the given raw text.
    
    Args:
        text (str): The raw text to extract URLs from.
        
    Returns:
        list[str]: A list of extracted https:// URLs.
    """
    # Regex to match https:// followed by valid URL characters
    # (letters, numbers, and common URL symbols, stopping at whitespace or certain punctuation)
    url_pattern = r'https://[a-zA-Z0-9-._~:/?#[\]@!$&\'()*+,;=]+'
    
    urls = re.findall(url_pattern, text)
    
    # Strip trailing punctuation that often gets accidentally included in raw text parsing
    cleaned_urls = [url.rstrip('.,!?;:)') for url in urls]
    
    return cleaned_urls

