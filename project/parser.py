import requests


def get_urls_to_parse():
    with open('data/sites.txt', 'rt') as file:
        for url in file:
            yield url.strip()


def normalize_url(url: str) -> str:
    if not url:
        raise ValueError("URL is empty")
    if url.startswith('https://'):
        return url
    return f"https://{url}/"


class RequestParser:
    @staticmethod
    def parse(url: str) -> int:
        headers = {
            'Accept-Language': 'en-US,en;q=0.9'
        }
        normalized_url = normalize_url(url)
        response = requests.get(
            url=normalized_url,
            timeout=5,
            headers=headers
        )
        return response.status_code


