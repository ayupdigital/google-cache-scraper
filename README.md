# Google Cache Scraper

## Introduction

A very quick and dirty scraper built to extract HTML content from the Google Cache

`data.txt` provides a list of URLs to visit. Each visited URL will be saved to the local disk under the same path structure as the original URL. E.g. http://example.com/about/the-team/joe-bloggs will be saved to `data_store` / about / the-team / joe-bloggs.html

Simple, quick and hacky and likely to break.

## Requirements
Python 2.7+

Twill ([twill.idyll.org](http://twill.idyll.org))

BeautifulSoup ([http://crummy.com/software/BeautifulSoup/](http://crummy.com/software/BeautifulSoup/))

lxml ([http://lxml.de](http://lxml.de/))


## Usage
There are 4 variables that can be changed to customise the output

`sleep_time = 5`

The number of seconds to sleep between page crawls


`domain_name = 'http://www.example.com`

The URL to fetch from the Google Cache


`data_store = 'pages/'`

The local path to the folder where you wish to store the extracted data (must end with a trailing slash '/')


`url_source = 'data.txt'`

The data source of all the URLs to crawl (txt file, each URL on a new line)



## License
Do What The Fuck You Want To Public License ([WTFPL](http://www.wtfpl.net/txt/copying/))