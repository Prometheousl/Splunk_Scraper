# Splunk_Scraper
Takes in data from the GitHub events API and writes it to a file for Splunk to monitor

## How-To
evoked with python3 ```curl-webservice.py```

Runs continously; writes to file only if the events api has changed; only writes every 43 seconds because the Github events API only allows 5000 requests per hour.
