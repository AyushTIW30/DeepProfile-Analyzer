def detect_platform(url):
    if "github.com" in url:
        return "github"
    elif "leetcode.com" in url:
        return "leetcode"
    elif "linkedin.com" in url:
        return "linkedin"
    else:
        return "generic"

