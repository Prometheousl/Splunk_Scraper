#!/usr/bin/python
import sys
import requests
import time

# Pings github events api every 43 seconds for json data
#   json data is then written to results.txt where Splunk
#   is continously monitoring and collects the data
#   can specify a different website if you would like.
# Use case: ./curl-webservice.py [website name]
def main():
    if len(sys.argv) >= 2:
        website = sys.argv[1]
    else:
        #website = 'http://services.swpc.noaa.gov/products/hepad.json'
        #website = 'http://services.swpc.noaa.gov/products/alerts.json'
        #website = 'https://www.time.gov'
        website = 'https://api.github.com/events'
    print('Website is',website)

    r = requests.get(website) # initial response
    while True:
        print('Getting response from website')
        prev_r = r
        r = requests.get(website) # Response object from website
        #print(r.json())
        if r.json() != prev_r.json(): # if json has changed
            print('Writing response to file')
            writeToFile(r)
        # 5000 requests to github API allowed per hour
        # So, about one request/43 seconds is optimal:
        # 43/60 = .716666   .716666 * 5000 = about 3600 seconds
        time.sleep(43)

# Writes a response's binary content to the file 'results.txt'
def writeToFile(response):
    # Write data to file
    file_name = 'results.txt'
    try:
        file = open(file_name,"wb") # open as byte
    except IOError:
        print('Could not write to',file_name)
        sys.exit()

    file.write(response.content) # write bytes to file

    file.close()

main()
