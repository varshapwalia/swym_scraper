## SWYM
Swym contains all url endpoints for application

## Setup Guide

1. `sudo pip install virtualenv`
2. `virtualenv venv`
3. `source venv/bin/activate`

## How to use

1. Clone the whole project
2. Install the required packages
3. Follow setup instructions
4. Start creating your application
5. Change `.env` file according to the requirements


Note: Also install the required packages from requirements.txt

## Upgrade
pip install -r requirements.txt --upgrade

## Structure

# Controllers for APIs needed to do ML
# Models for Database structuring
# Scripts for custom jobs and intiating projects.
# Workers for cron and queing based jobs
# requirements.txt keeps the track of required packages.
# Staticd for files, Custom CSS an JS
# Templates for Html pages.
# Procfile and runtime.txt for server enviroment and deployent

## Ways To Improve the Project and learnings

# Integrating it in web framework with cronjobs and webhooks.
# Machine learning used to scrape standard product data
# Error handling and debugging tools speed up the process of writing new crawlers and debugging existing ones
# Requests to each website are throttled to avoid DOS attacks
# Settings are configurable per eCommerce retailer to maximize the requests per second, saving you money on infrastructure costs
# The architecture scales horizontally to accomplish jobs of any size
# RealTime DBs to scale the products.
# Making it more fail safe and general purpose.
# A breadth-first search (BFS) or a Depth-first search (DFS) — based on the situation — to generate all URLs belonging to each eCommerce website
# Jobs are run to in parallel using event loops
# Product URLs should be batch processed
# Concurrent crawling in threaded enviroment.
# Asynchronous
# Seperate error manager to quickly debugged from developers end.
# Start storin crawled data in DB like S3 to store them for future change and references.
# A separate worker / daemon fetches the HTML pages from the data store and extracts the required fields.


## Challanges Faced and Issues

# My limited knowledge on web crawlers, Had to research for some time to find a quick solution respecting time constraints for both parties.
# Anti-Bot Countermeasures and proxy work around.
# Sloppy and Always Changing Website Formats and there is no Magic bullet to it. Big scrapping companies run over 4000 spiders over few thousands of websites and 20-40 scrappers fail each day. (responsible for that is ajax, bad formatted/misspelled xmls)
# For the sake of time i used BeautifulSoup 4, Otherwise i would take a selenium and custome search criteria for more control or Scrapy as web crawler for spiders.
# We need to write better ways to fail safe (e.g. conditions and services of NLP to go through data.)
# Speed of crawling the websites locally

## SAMPLE
