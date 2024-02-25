def calculate_language_stats(repos: list) -> dict:
    """
    Calculate the statistics of programming languages used in a list of repositories.

    Args:
        repos (list): A list of repositories, where each repository is represented as a dictionary.

    Returns:
        dict: A dictionary containing the statistics of programming languages used in the repositories.
              The keys are the programming languages, and the values are dictionaries with the following keys:
              - 'count': The number of repositories that use the programming language.
              - 'percentage': The percentage of repositories that use the programming language, rounded to 2 decimal places.
    """
    try:
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
    except Exception as e:
        raise ValueError(f"Error: Something went wrong with calculate_language_stats - {e}")


def get_top_n_langs(lang_stats: dict, n: int) -> dict:
    """
    Get the top N programming languages based on the number of repositories that use them.

    Args:
        langs_stats (dict): A dictionary containing the statistics of programming languages used in the repositories.
        n (int): The number of top programming languages to return.

    Returns:
        dict: A dictionary containing the top N programming languages and their statistics.
    """
    try:
        top_langs = list(lang_stats.items())[:n]

        other_percentage = sum(item[1]['percentage'] for item in list(lang_stats.items())[n:])
        
        if other_percentage > 0:
            top_langs.append(("Others", {"percentage": other_percentage}))

        return dict(top_langs)
    
    except Exception as e:
        raise ValueError(f"Error: Something went wrong with get_top_n_langs - {e}")