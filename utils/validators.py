from urllib.parse import urlparse

def validate_url(url: str) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def extract_github_username(url: str):
    parts = url.rstrip("/").split("/")
    if "github.com" in url and len(parts) >= 4:
        return parts[3]
    return None
