def calculate_language_stats(repos: list) -> dict:
    langs_stats = {}

    for repo in repos:
        language = repo['language'] or 'Unknown'
        if language in langs_stats:
            langs_stats[language]["count"] += 1
        else:
            langs_stats[language] = {"count": 1, "percentage": 0}

    total_repos = len(repos)
    for lang in langs_stats:
        langs_stats[lang]['percentage'] = round((langs_stats[lang]['count'] / total_repos) * 100, 2) if total_repos > 0 else 0
    
    return langs_stats
