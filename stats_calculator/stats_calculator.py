def calculate_language_stats(repos: list) -> dict:
    langs_stats = {}

    unknown_count = 0

    for repo in repos:
        language = repo['language'] or 'Unknown'

        if language == 'Unknown':
            unknown_count += 1
            continue

        if language in langs_stats:
            langs_stats[language]["count"] += 1
        else:
            langs_stats[language] = {"count": 1, "percentage": 0}

    total_valid_repos = len(repos) - unknown_count

    for lang in langs_stats:
        langs_stats[lang]['percentage'] = round((langs_stats[lang]['count'] / total_valid_repos) * 100, 2) if total_valid_repos > 0 else 0

    return dict(sorted(langs_stats.items(), key=lambda item: item[1]['percentage'], reverse=True))


def calculate_profile_stats(events: list, repos: list) -> dict:
    profile_stats = {
        "total_repos": len(repos),
        "total_pull_requests": 0,
        "total_commits": 0,
        "total_stars": 0,
        "total_forks": 0,
        "total_watchers": 0,
        "total_issues": 0
    }

    # Calculate the total pull requests, commits, stars, forks, watchers, and issues

    return profile_stats    
