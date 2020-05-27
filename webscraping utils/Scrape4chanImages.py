#!/usr/bin/env python3
import re,requests,sys,json

urlRegex = re.compile(r'([a-z]+)/thread/([0-9]+)')

def parseurl(text):
    temp = urlRegex.search(text)
    board = temp.group(1)
    thread = temp.group(2)
    return board, thread

def get(url):
    json = requests.get(url)
    try:
        json.raise_for_status()
        return json
    except Exception as exc:
        print('Failed to get JSON: %s' % (exc))
    return -1

def scrape(raw, board):
    res = json.loads(raw.content)
    for x in res['posts']:
        if 'ext' in x.keys():
            tim = str(res['posts'][4]['tim'])
            ext = res['posts'][4]['ext']
            filename = tim + ext
            imageURL = 'https://i.4cdn.org/'+board+'/'+filename
            image = requests.get(imageURL)
            try:
                image.raise_for_status()
            except Exception as exc:
                print('Failed to get Image: %s' % (x))
            fp = open(filename, 'wb')
            for chunk in image.iter_content(100000):
                fp.write(chunk)
            fp.close()

def main():
    if '-url' not in sys.argv:
        raise Exception('No url')
    inURL = sys.argv[sys.argv.index('-url') + 1]
    b, t = parseurl(inURL)
    url = 'https://a.4cdn.org/'+b+'/thread/'+t+'.json'
    raw = get(url)
    scrape(raw, b)

# main()
