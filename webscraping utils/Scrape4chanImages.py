#!/usr/bin/env python3
import re,requests,sys,json,threading,os

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

def scrape(posts, board, minwidth, minheight, requiredaspect, foldername):
    for x in posts:
        if 'ext' in x.keys():
            if 'filedeleted' in x.keys() and int(x['filedeleted']) == 1:
                continue
            width = int(x['w'])
            height = int(x['h'])
            aspectratio = width/height
            if requiredaspect == 0:
                if width >= minwidth and height >= minheight:
                    downloadAll(board, x, foldername)
            else:
                if width >= minwidth and height >= minheight and aspectratio == requiredaspect:
                    downloadAll(board, x, foldername)
    return 1

def downloadAll(board, x, foldername):
    tim = str(x['tim'])
    ext = x['ext']
    filename = tim + ext
    imageURL = 'https://i.4cdn.org/'+board+'/'+filename

    try:
        image = requests.get(imageURL, timeout=10)
        print(image.status_code)
    except requests.exceptions.Timeout:
        print('Request timed out: %s' % (filename))

    try:
        image.raise_for_status()
    except Exception as exc:
        print('Failed to get Image: %s' % (filename))

    fp = open(os.path.join(foldername, os.path.basename(filename)), 'wb')
    for chunk in image.iter_content(100000):
        fp.write(chunk)
    fp.close()

def aspecthelper(txt):
    arr = txt.split('/')
    numer = int(arr[0])
    denom = int(arr[1])
    return numer/denom

def main():
    # Take and prepare command line arguments
    # - Little to no error check for the base functionality
    minwidth = 0
    minheight = 0
    requiredaspect = 0.0
    helpMessage = """Required:
    \t-url\t- Url of thread
    Optional:
    \t--w\t- Minimum required width of image
    \t--h\t- Minimum required height of image
    \t--aspect\t- Required aspect ratio for image download"""

    if '--help' in sys.argv:
        print(helpMessage)
        return None
    
    if '-url' not in sys.argv:
        raise Exception('No url')

    inURL = sys.argv[sys.argv.index('-url') + 1]

    if '--w' in sys.argv:
        minwidth = int(sys.argv[sys.argv.index('--w') + 1])
    if '--h' in sys.argv:
        minheight = int(sys.argv[sys.argv.index('--h') + 1])
    if '--aspect' in sys.argv:
        requiredaspect = aspecthelper(sys.argv[sys.argv.index('--aspect') + 1])
    if '--location' in sys.argv:
        print('Not yet implemented.')
    if '--help' in sys.argv:
        print(helpMessage)

    # Parse the provided url using regex
    # Access the 4chan API to get thread information in form of JSON
    # Create a folder to place the downloaded images
    b, t = parseurl(inURL)
    url = 'https://a.4cdn.org/'+b+'/thread/'+t+'.json'
    raw = get(url)
    res = json.loads(raw.content)
    posts = res['posts']
    length = len(posts)
    it = round(length/10)
    foldername = ''
    if 'sub' in posts[0].keys():
        foldername = posts[0]['sub']
    else:
        foldername = str(posts[0]['no'])

    os.makedirs(foldername, exist_ok=True)

    # Multithread/Concurrency to not let the program hang while waiting for each download
    downloadThreads = []
    for index in range(0,length,it):
        if index+it <= length:
            downloadThread = threading.Thread(target=scrape, args=(posts[index:index+it], b, minwidth, minheight, requiredaspect, foldername))
        else:
            downloadThread = threading.Thread(target=scrape, args=(posts[index:length], b, minwidth, minheight, requiredaspect, foldername))
        downloadThreads.append(downloadThread)
        downloadThread.start()

    for downloadThread in downloadThreads:
        downloadThread.join()

    print('Done')

main()
