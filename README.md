# Google Cache Scraper

## Introduction

A very quick and dirty scraper built to extract HTML

The original intended use for this script is to extract all links that Google has indexed for a specific site (e.g. all those pages that can be found by querying Google using the `site:` prefix. For example `site:example.com`)

The scraper will then extract links from the page that start with `query_url` and save them to a file called `search_results`.

Simple, quick and hacky and likely to break.

## Requirements
Python 2.7+

Twill ([twill.idyll.org](http://twill.idyll.org))

## Usage
There are 4 variables that can be changed to customise the output

`start_page = 1`

The page that the scraper will start at


`end_page = 5`

The page that the scraper will stop at


`sleep_time = 5`

The number of seconds to sleep between page crawls


`query = 'site:www.example.com'`

The query that will be searched for


`query_url = 'http://www.example.com'`

## License
Do What The Fuck You Want To Public License ([WTFPL](http://www.wtfpl.net/txt/copying/))