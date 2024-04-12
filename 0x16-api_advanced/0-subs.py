#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check for a 404 status code (subreddit not found)
    if response.status_code == 404:
        return 0
    
    results = response.json().get("data")
    return results.get("subscribers")
