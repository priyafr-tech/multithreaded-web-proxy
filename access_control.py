"""
access_control.py
Handles blocked website filtering
"""

def load_blocked_sites(filename="blocked_sites.txt"):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []

def is_blocked(url, blocked_sites):
    for site in blocked_sites:
        if site in url:
            return True
    return False
