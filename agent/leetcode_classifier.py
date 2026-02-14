def classify_leetcode_profile(data):
    profile = data["data"]["profile"]
    stats = data["data"]["submitStats"]["acSubmissionNum"]

    total = 0
    easy = medium = hard = 0

    for item in stats:
        if item["difficulty"] == "All":
            total = item["count"]
        elif item["difficulty"] == "Easy":
            easy = item["count"]
        elif item["difficulty"] == "Medium":
            medium = item["count"]
        elif item["difficulty"] == "Hard":
            hard = item["count"]

    if total > 500:
        level = "Advanced Competitive Programmer"
    elif total > 200:
        level = "Intermediate Problem Solver"
    else:
        level = "Beginner Programmer"

    return {
        "name": profile.get("realName"),
        "username": data["data"]["username"],
        "ranking": profile.get("ranking"),
        "total_solved": total,
        "easy": easy,
        "medium": medium,
        "hard": hard,
        "level": level,
        "about": profile.get("aboutMe")
    }
