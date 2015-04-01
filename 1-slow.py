#!/usr/bin/env python

import requests
import time

# silence warnings about unverified https
try:
    import urllib3
except ImportError:
    from requests.packages import urllib3
urllib3.disable_warnings()

site_list = ["cnn.com", "imdb.com", "chase.com", "nytimes.com", "huffingtonpost.com", "yelp.com", "bankofamerica.com", "wordpress.com", "buzzfeed.com", "weather.com", "stackoverflow.com", "wellsfargo.com", "walmart.com", "msn.com", "microsoft.com", "zillow.com", "etsy.com", "dropbox.com", "wikia.com", "github.com", "comcast.net", "washingtonpost.com", "aol.com", "salesforce.com", "adobe.com",
            "google.com", "facebook.com", "youtube.com", "amazon.com", "yahoo.com", "wikipedia.org", "twitter.com", "ebay.com", "linkedin.com", "reddit.com", "craigslist.org", "imgur.com", "go.com", "tumblr.com", "netflix.com", "t.co", "pinterest.com", "live.com", "espn.go.com", "bing.com", "paypal.com", "blogspot.com", "instagram.com", "diply.com", "apple.com",
            "baidu.com", "foxnews.com", "amazonaws.com", "pandora.com", "bestbuy.com", "target.com", "about.com", "indeed.com", "outbrain.com", "gmail.com", "reference.com", "cnet.com", "googleusercontent.com", "forbes.com", "intuit.com", "hulu.com", "tripadvisor.com", "kickass.to", "groupon.com", "homedepot.com", "microsoftonline.com", "pornhub.com", "xvideos.com", "ups.com",
            "dailymail.co.uk", "americanexpress.com", "slickdeals.net", "businessinsider.com", "capitalone.com", "flickr.com", "office365.com", "deviantart.com", "twitch.tv", "cbssports.com", "usatoday.com", "force.com", "vimeo.com", "googleapis.com", "verizonwireless.com", "bbc.com", "bleacherreport.com", "gfycat.com", "stackexchange.com", "att.com", "fedex.com", "answers.com", "wsj.com", "godaddy.com", "ask.com"]



def fetch_url(url):
    try:
        # print url
        content = requests.get(url)
    except requests.exceptions.RequestException:
        return None
    return (url, content.status_code)

def main():
    start = time.time()
    print "Requesting %s urls" % len(site_list)
    [fetch_url('http://%s' % site) for site in site_list]
    print "Time: %s seconds" % (time.time() - start)



if __name__ == '__main__':
    main()

