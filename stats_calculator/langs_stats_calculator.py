def calculate_language_stats(repos: list) -> dict:
    """
    Calculate the statistics of programming languages used in a list of repositories.

    Args:
        repos (list): A list of repositories, where each repository is represented as a dictionary.

    Returns:
        dict: A dictionary containing the statistics of programming languages used in the repositories

    Raises:
        ValueError: If an error occurs during the calculation of language statistics.
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


def get_top_n_languages(sorted_langs: dict, n: int) -> dict:
    """
    Returns a dictionary containing the top n languages based on the given sorted_langs dictionary.

    Args:
        sorted_langs (dict): A dictionary containing the languages and their corresponding statistics.
        n (int): The number of top languages to retrieve.

    Returns:
        dict: A dictionary containing the top n languages and their statistics.

    Raises:
        ValueError: If an error occurs while retrieving the top n languages.
    """
    try:
        top_langs = dict(list(sorted_langs.items())[:n])
        other_percentage = round(sum([stats['percentage'] for lang, stats in list(sorted_langs.items())[n:]]), 2)

        if other_percentage > 0:
            top_langs['Others'] = {'percentage': other_percentage}

        return top_langs
    except Exception as e:
        raise ValueError(f"Error: Something went wrong with get_top_n_languages - {e}")