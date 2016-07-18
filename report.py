import requests


def lambda_handler(event, context):
    url = "https://stop.jetnoise.net/add-complaint"
    payload = {'browser_uuid': 'aecb36a2-2fd7-4e04-a17a-85ea8ef64203',
               'browser_name': 'Chrome',
               'browser_version': '51',
               'browser_vendor': 'Google Inc.',
               'browser_platform': 'MacIntel',
               'content': '',
               'activity': 'Quality of Life',
               'loudness': '2'}
    headers = {'accept': 'text/html,application/xhtml+xml,application/xml;\
q=0.9,image/webp,*/*;q=0.8',
               'accept-encoding': 'gzip, deflate, br',
               'accept-language': 'en-US,en;q=0.8',
               'cache-control': 'no-cache',
               'content-length': '171',
               'content-type': 'application/x-www-form-urlencoded',
               'dnt': '1',
               'origin': 'https://stop.jetnoise.net',
               'pragma': 'no-cache',
               'referer': 'https://stop.jetnoise.net/',
               'upgrade-insecure-requests': '1',
               'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 \
Safari/537.36'}
    cookies = dict(__cfduid='d1a85e506011a09684efc3296f8a55f881463460892',
                   serfr0='MTQ2ODI1ODI0NHxEdi1oQkFFQ182SUFBUkFCRUFBQUx2LWlBQUVH\
YzNSeWFXNW5EQWNBQldWdFlXbHNCbk4wY21sdVp3d1JBQTl6YjJOQVkyOWta\
VFF3TkM1amIyMD18YHqtHrhsDAzW6ry0Q_U6o1KGqmmToUXfM6eYuWrkyO0=\
',
                   ACSID='~AJKiYcFaRyjFbHepLyFho9f6txXsf6iX6cqf9cz1T5x1z4Fcujef\
9PPJvU3gnjgq7HCYaLFHn2Ecr0O5J4Rnb7dLi6GKqjZonjG_lKOqVYJkI3DB\
il0ZHxAnvZo8FX-eauyftYGFmNtuuOKHMaEZ00Ripl51-LlRr6S0RhGbE8Yf\
LVFBRMoY7pxPkdTA8E1iFz896KxHxtk_d3x2GHWdOlld6OPCwRO9Pnc8LBbO\
x5r1gsMKuhcddmo79fNah1BxTtuEddtT10joEPU0dCL_JVoIUgm6RB8GA_N0\
Zoyyv6d0g59UJDMrbqOiQjF84GKNO5pURUnK5PPM')
    res = requests.post(url, data=payload, headers=headers, cookies=cookies)
    print "URL is %s" % url
    print "payload is %s" % payload
    print "headers are %s" % headers
    print "cookies are %s" % cookies
    print "-------"
    print(res.content)
