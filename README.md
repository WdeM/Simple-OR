# Check Open Redirects

Simple testing for open redirection with a small python script and a wordlist.

# Requirements
* tld
* requests
* progressbar2

Install requirements
```pip3 install -r requirements.txt``` or install them manually.

# Usage
```python3 openredirect.py [url] [wordlist] ```

# Notes
Still a bit time consuming when attacking a slower target site, one could try to add threading to the mix if one 
can find the time and motivation to do so.

Made it for Open Redirection, but obviously it can be used for other purposes like SSRF or XSS.
