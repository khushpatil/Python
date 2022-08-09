from lxml import html
from urllib.parse import urlparse
import requests

def get_urls_from_string(page_content, base_url):
    arr = []
    tree = html.fromstring(page_content)
    tree.make_links_absolute(base_url)
    for elem in tree.iter():
        if elem.tag == 'a':
            arr.append(elem.get('href'))
    return arr

def normalize_url(url):
    obj = urlparse(url)
    normalized_url = f"{obj.netloc}{obj.path}"
    lowercased = normalized_url.lower()
    if len(lowercased) < 1:
        return lowercased
    last_slash_removed = lowercased if lowercased[:-1] != '/' else lowercased[:-1]
    return last_slash_removed

def crawl_page(base_url, current_url, pages):
    normalized_url = normalize_url(current_url)

    if normalized_url not in pages:
        pages[normalized_url] = 0

    parsed_base = urlparse(base_url)
    parsed_curr = urlparse(current_url)

    if parsed_curr.netloc != parsed_base.netloc:
        pages[normalized_url] = None
        return pages

    if pages[normalized_url] is None:
        return pages

    if pages[normalized_url] > 0:
        pages[normalized_url] += 1

    o = requests.get(current_url)

    try:
        validate_response(o)
    except Exception as e:
        print(e)
        pages[current_url] = None
        return pages

    pages[normalized_url] += 1

    url_arr = get_urls_from_string(o.content, base_url)
    for url in url_arr:
        crawl_page(base_url, url, pages)
    return pages

def validate_response(resp):
    if resp.status_code != 200:
        raise Exception('The response object is not called successfully')

    if "text/html" not in resp.headers["content-type"].lower():
        raise Exception('The object called is not of the type html')
