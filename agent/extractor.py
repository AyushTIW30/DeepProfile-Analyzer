import requests
from bs4 import BeautifulSoup
import trafilatura
from playwright.sync_api import sync_playwright


# ==============================
# GITHUB API EXTRACTION
# ==============================

def extract_github_data(username):
    try:
        user_url = f"https://api.github.com/users/{username}"
        repos_url = f"https://api.github.com/users/{username}/repos"

        user_res = requests.get(user_url)
        repos_res = requests.get(repos_url)

        if user_res.status_code != 200:
            print("GITHUB STATUS:", user_res.status_code)
            return None

        return {
            "type": "github",
            "user": user_res.json(),
            "repos": repos_res.json()
        }

    except Exception as e:
        print("GITHUB ERROR:", str(e))
        return None


# ==============================
# STATIC SITE EXTRACTION
# ==============================

def extract_static_data(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=15)

        if response.status_code != 200:
            print("STATIC STATUS:", response.status_code)
            return None

        html_content = response.text
        print("STATIC HTML LENGTH:", len(html_content))

        downloaded = trafilatura.extract(html_content)
        text_content = downloaded if downloaded else ""
        print("STATIC TEXT LENGTH:", len(text_content))

        soup = BeautifulSoup(html_content, "html.parser")
        title = soup.title.string if soup.title else ""

        return {
            "type": "static",
            "title": title,
            "content": text_content
        }

    except Exception as e:
        print("STATIC ERROR:", str(e))
        return None


# ==============================
# DYNAMIC SITE EXTRACTION
# ==============================

def extract_dynamic_data(url):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url, timeout=60000)
            page.wait_for_timeout(5000)

            html_content = page.content()
            browser.close()

        print("DYNAMIC HTML LENGTH:", len(html_content))

        downloaded = trafilatura.extract(html_content)
        text_content = downloaded if downloaded else ""
        print("DYNAMIC TEXT LENGTH:", len(text_content))

        soup = BeautifulSoup(html_content, "html.parser")
        title = soup.title.string if soup.title else ""

        return {
            "type": "dynamic",
            "title": title,
            "content": text_content
        }

    except Exception as e:
        print("DYNAMIC ERROR:", str(e))
        return None
def extract_leetcode_data(username):
    url = "https://leetcode.com/graphql"

    query = """
    query userProfile($username: String!) {
      matchedUser(username: $username) {
        username
        profile {
          realName
          ranking
          userAvatar
          aboutMe
        }
        submitStats {
          acSubmissionNum {
            difficulty
            count
          }
        }
      }
    }
    """

    variables = {"username": username}

    try:
        response = requests.post(
            url,
            json={"query": query, "variables": variables},
            headers={
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0"
            }
        )

        if response.status_code != 200:
            print("LEETCODE STATUS:", response.status_code)
            return None

        data = response.json()

        if "data" not in data or not data["data"]["matchedUser"]:
            print("LEETCODE USER NOT FOUND")
            return None

        return {
            "type": "leetcode",
            "data": data["data"]["matchedUser"]
        }

    except Exception as e:
        print("LEETCODE ERROR:", str(e))
        return None
