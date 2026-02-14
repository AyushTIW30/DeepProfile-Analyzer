from utils.validators import extract_github_username
from agent.platform_detector import detect_platform
from agent.intelligence import format_leetcode_report, generate_leetcode_intelligence
from agent.leetcode_classifier import classify_leetcode_profile
from agent.extractor import (
    extract_github_data,
    extract_static_data,
    extract_leetcode_data
)
from agent.classifier import classify_github_profile
from agent.summarizer import summarize_generic


def process_url(url):
    platform = detect_platform(url)

    if platform == "github":
        username = extract_github_username(url)
        data = extract_github_data(username)

        if not data:
            return {"error": "Unable to fetch GitHub data"}

        classified = classify_github_profile(data)
        return classified

    elif platform == "leetcode":
        username = url.rstrip("/").split("/")[-1]
        data = extract_leetcode_data(username)

        if not data:
            return {"error": "Unable to fetch LeetCode data"}

        classified = classify_leetcode_profile(data)

        intelligence = generate_leetcode_intelligence(classified)

        formatted = format_leetcode_report(classified, intelligence)

        return {"report": formatted}

    else:
        data = extract_static_data(url)

        if not data:
            return {"error": "Unable to fetch public content"}

        summary = summarize_generic(data)
        return summary
