def calculate_profile_stats(events: list, repos: list) -> dict:
    try:
        profile_stats = {
            "total_repos": len(repos),
            "total_pull_requests": 0,
            "total_commits": 0,
            "total_issues": 0
        }

        # TODO: Calculate the total pull requests, commits, and issues

        return profile_stats 
    except Exception as e:
        raise ValueError(f"Error: Something went wrong with calculate_profile_stats - {e}")
    

def calculate_social_stats(events: list) -> dict:
    try:
        social_stats = {
            "total_followers": 0,
            "total_following": 0,
            "total_watchers": 0,
            "total_forks": 0,
            "total_stars": 0,
        }

        # TODO: Calculate the total pull following, followers, stars, watchers, and forks
    
    except Exception as e:
        raise ValueError(f"Error: Something went wrong with calculate_social_stats - {e}")