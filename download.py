import requests
import argparse
import json

def get_dir(dir, passwd="null"):
    res = requests.post(dir, json={'password': passwd})
    res_data = json.loads(res.text)
    ret = []
    for item in res_data['files']:
        if item['mimeType'] != 'application/vnd.google-apps.folder':
            ret.append(dir + item['name'])
    return ret

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str)
    parser.add_argument('--passwd', type=str, default='null')
    args = parser.parse_args()
    download_list = get_dir(args.path, args.passwd)
    for url in download_list:
        print(url)