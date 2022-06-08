#!/usr/bin/env python3
"""
web cache and tracker
"""
import redis
import requests
r = redis.Redis()
count = 0


def get_page(url: str) -> str:
    """
    obtain the HTML content of a particular URL
    """
    r.set(url, count)
    response = requests.get(url)
    r.incr(f"count:{url}")
    r.setex(url, 10, r.get(url))
    return response.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
