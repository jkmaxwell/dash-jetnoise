import requests


def lambda_handler(event, context):
    url = "https://stop.jetnoise.net/add-complaint"
    payload = {'browser_uuid': 'aecb36a2-2fd7-4e04-a17a-85ea8ef64203',
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
               'cookie': '__cfduid=d1a85e506011a09684efc3296f8a55f881463460892; \
               serfr0=MTQ2ODI1ODI0NHxEdi1oQkFFQ182SUFBUkFCRUFBQUx2LWlBQUVHYzNSeWFXN\
               W5EQWNBQldWdFlXbHNCbk4wY21sdVp3d1JBQTl6YjJOQVkyOWtaVFF3TkM1amIyMD18Y\
               HqtHrhsDAzW6ry0Q_U6o1KGqmmToUXfM6eYuWrkyO0=; \
               ACSID=~AJKiYcFMYyd1fuKd21M3Vk5Ei_AC7p05lfwGUQxmU95laqDyr4UamSCZZ-w0p\
               zaRn7rJ0PN0CibXyUQSMKIZuxo-oWhrs4AqxRr2gEPnY1ZYBj7Pt-m6_vV2fUCemv8Qm\
               hlCASBfvJMMlT6uo47fIWBNjKm3i1G-IBNhZM_SSIxNPrGdn7afpOkCZHuNBbEvY35qX\
               qA-pytPYJ23etGeVyREVM2GnmSmlcf19IdEy9Gtb9V_MWyqjcFit0va3EqMKQo_T9EOP\
               KO6MUR9PMUhQ-GDuPdyHfQ8obehjjX2sLpSZ5cESJei3HQ',
               'dnt': '1',
               'origin': 'https://stop.jetnoise.net',
               'pragma': 'no-cache',
               'referer': 'https://stop.jetnoise.net/',
               'upgrade-insecure-requests': '1',
               'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) \
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 \
               Safari/537.36'}
    res = requests.post(url, data=payload, headers=headers)
    print "URL is %s" % url
    print "payload is %s" % payload
    print "headers are %s" % headers
    print(res.content)
