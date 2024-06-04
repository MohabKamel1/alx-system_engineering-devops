import requests

def number_of_subscribers(subreddit):
    # URL for subreddit details in Reddit's JSON format
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Custom User-Agent to avoid Too Many Requests error
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        # Make the GET request
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            # If the status code is not 200, it's likely an invalid subreddit
            return 0
    except requests.RequestException:
        # Catch any requests-related errors
        return 0
