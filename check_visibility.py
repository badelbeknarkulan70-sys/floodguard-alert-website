import urllib.request, urllib.error
url = 'https://github.com/badelbeknarkulan70-sys/floodguard-alert-website'
try:
    with urllib.request.urlopen(url, timeout=10) as r:
        print('status', r.status)
except urllib.error.HTTPError as e:
    print('status', e.code)
except Exception as e:
    print('error', repr(e))
