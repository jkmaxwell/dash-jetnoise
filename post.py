import requests
url = "https://stop.jetnoise.net/add-complaint"
payload = {'browser_uuid': 'ENTER_UUID',
           'browser_name': 'Chrome',
           'browser_version': '51',
           'browser_vendor': 'Google Inc.',
           'browser_platform': 'MacIntel',
           'content': '',
           'activity': 'Quality+of+Life',
           'loudness': '2'}
headers = {'accept': 'text/html,application/xhtml+xml,application/xml;\
            q=0.9,image/webp,*/*;q=0.8',
           'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'en-US,en;q=0.8',
           'cache-control': 'no-cache',
           'content-length': '171',
           'content-type': 'application/x-www-form-urlencoded',
           'cookie': 'ENTER_COOKIE',
           'dnt': '1',
           'origin': 'https://stop.jetnoise.net',
           'pragma': 'no-cache',
           'referer': 'https://stop.jetnoise.net/',
           'upgrade-insecure-requests': '1',
           'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) \
           AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 \
           Safari/537.36'}
res = requests.post(url, data=payload, headers=headers)
