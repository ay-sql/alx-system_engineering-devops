#!/usr/bin/python3
"""Module to count occurrences of keywords in hot post titles"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """Prints sorted count of keywords in hot post titles"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'My User Agent 1.0'}
    params = {'after': after} if after else {}
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        return
    
    data = response.json()
    posts = data['data']['children']
    
    for post in posts:
        title = post['data']['title'].lower()
        for word in word_list:
            word = word.lower()
            if f' {word} ' in f' {title} ':
                word_count[word] = word_count.get(word, 0) + 1
    
    after = data['data']['after']
    if after:
        count_words(subreddit, word_list, after, word_count)
    else:
        sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")