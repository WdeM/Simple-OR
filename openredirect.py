#!/usr/bin/python3
import sys
import requests
import progressbar
from tld import get_tld

def request(url):
    try:
        response = requests.get(url, verify=False, allow_redirects=False, timeout=3)
        return response
    except Exception as e:
        print(e)

def read_wordlist(wordlist):
    _list = []
    f = open(wordlist)
    for payload in f.readlines():
        payload = payload.replace("\n", "")
        if payload not in _list:
            _list.append(payload)
    return _list


if __name__ == "__main__":
    try:
        url_given = sys.argv[1]
        wordlist_given = sys.argv[2]
    except Exception as e:
        print("\n### Syntax being openredirect.py [url] [wordlist] \n")
        exit(0)

    redirecting_status_codes = [301,302,303,304]
    payloads = read_wordlist(wordlist_given)
    bar = progressbar.ProgressBar(max_value=len(payloads))
    for index, payload in enumerate(payloads):
        response = request(url_given+payload)
        if response.status_code in redirecting_status_codes:
            if "Location" in response.headers:
                queried_url = get_tld(url_given, as_object=True)
                old_domain = queried_url.domain+"."+queried_url.tld
                if old_domain not in response.headers["Location"]:
                    print("### Found something ###")
                    print("Location header : ")
                    print(response.headers["Location"])
                    print("Queried url :")
                    print(url_given+payload)
        bar.update(index)