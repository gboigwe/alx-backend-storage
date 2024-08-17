#!/usr/bin/env python3
"""Module for managing a time-limited web cache
and access tracker"""

from functools import wraps
import redis
import requests
from typing import Callable

client = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """Decorator to track the number of times
    a URL is accessed
    """

    @wraps(method)
    def wrapper(url):
        """Inner function to handle caching and
        counting"""
        client.incr(f"count:{url}")
        cached_html = client.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')

        html = method(url)
        client.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """Retrieves the HTML content of a specified
    web page"""
    req = requests.get(url)
    return req.text
