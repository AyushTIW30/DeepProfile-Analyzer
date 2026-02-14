def classify_github_profile(data):
    user = data["user"]
    repos = data["repos"]

    languages = []
    for repo in repos:
        if repo.get("language"):
            languages.append(repo["language"])

    primary_language = max(set(languages), key=languages.count) if languages else "Unknown"

    activity_level = "Active" if user.get("public_repos", 0) > 10 else "Moderate"

    return {
        "name": user.get("name"),
        "username": user.get("login"),
        "bio": user.get("bio"),
        "location": user.get("location"),
        "public_repos": user.get("public_repos"),
        "followers": user.get("followers"),
        "primary_language": primary_language,
        "activity_level": activity_level
    }
