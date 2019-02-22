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

1. Controllers for APIs needed and handling requests.
2. Models for Database structuring
3. Scripts for custom jobs and intiating projects.
4. Workers for cron and queing based jobs
5. requirements.txt keeps the track of required packages.
6. Staticd for files, Custom CSS an JS
7. Templates for Html pages.
8. Procfile and runtime.txt for server enviroment and deployent

## Ways To Improve the Project and learnings

1. Integrating it in web framework with cronjobs and webhooks.
2. Machine learning used to scrape standard product data
3. Error handling and debugging tools speed up the process of writing new crawlers and debugging existing ones
4. Requests to each website are throttled to avoid DOS attacks
5. Settings are configurable per eCommerce retailer to maximize the requests per second, saving you money on infrastructure costs
6. The architecture scales horizontally to accomplish jobs of any size
7. RealTime DBs to scale the products.
8. Making it more fail safe and general purpose.
9. A breadth-first search (BFS) or a Depth-first search (DFS) — based on the situation — to generate all URLs belonging to each eCommerce website
10. Jobs are run to in parallel using event loops
11. Product URLs should be batch processed
12. Concurrent crawling in threaded enviroment.
13. Asynchronous
14. Seperate error manager to quickly debugged from developers end.
15. Start storin crawled data in DB like S3 to store them for future change and references.
16. A separate worker / daemon fetches the HTML pages from the data store and extracts the required fields.


## Challanges Faced and Issues

1. My limited knowledge on web crawlers, Had to research for some time to find a quick solution respecting time constraints for both parties.
2. Anti-Bot Countermeasures and proxy work around.
3. Sloppy and Always Changing Website Formats and there is no Magic bullet to it. Big scrapping companies run over 4000 spiders over few thousands of websites and 20-40 scrappers fail each day. (responsible for that is ajax, bad formatted/misspelled xmls)
4. For the sake of time i used BeautifulSoup 4, Otherwise i would take a selenium and custome search criteria for more control or Scrapy as web crawler for spiders.
5. We need to write better ways to fail safe (e.g. conditions and services of NLP to go through data.)
6. Speed of crawling the websites locally

## SAMPLE
INPUT

https://pinkblue.in/

Outpu
https://pinkblue.in/brand/3m-espe 3M ESPE
https://pinkblue.in/brand/dentsply  DENTSPLY
https://pinkblue.in/brand/gc  GC
https://pinkblue.in/brand/gdc GDC
https://pinkblue.in/brand/axiostat  AXIOSTAT
https://pinkblue.in/brand/neoendo NEOENDO
https://pinkblue.in/brand/woodpecker  WOODPECKER
https://pinkblue.in/brand/zhermack  ZHERMACK
https://pinkblue.in/zhermack-zetaplus-putty-and-kit.html  Zhermack Zetaplus Putty And Kit
https://pinkblue.in/ramsons-powdered-latex-exam-gloves.html Ramsons Powdered Latex Exam Gloves
https://pinkblue.in/max-piezo-scalers.html  Max Piezo Scalers
https://pinkblue.in/gc-gold-label-9-posterior-restorative.html  GC Gold Label 9 Posterior Restorative
https://pinkblue.in/bombay-dental-em100-cordless-endomotor-with-led.html  Bombay Dental EM100 Cordless Endomotor with LED
https://pinkblue.in/dental-avenue-xpress-dental-x-ray-film.html Dental Avenue Xpress Dental X-Ray Film
https://pinkblue.in/dentex-stainless-steel-k-hand-file.html Dentex Stainless Steel K Hand File
https://pinkblue.in/speedendo-super-gold-flex-rotary-files.html SpeedEndo Super Gold Flex Rotary Files
https://pinkblue.in/e-connect-pro-endo-motor-with-e-pex-pro-apex-locator.html E-Connect Pro Endo Motor With E-Pex Pro Apex Locator
https://pinkblue.in/gc-gold-label-1-luting-lining.html  GC Gold Label 1 Luting & Lining
https://pinkblue.in/neoendo-flex-files-rotary.html  Neoendo Flex Rotary Files
https://pinkblue.in/crystal-intraoral-sensor.html Crystal Intraoral Sensor
https://pinkblue.in/neelkanth-lead-apron.html Neelkanth Lead Apron
https://pinkblue.in/meta-etchant.html Meta Etchant
https://pinkblue.in/avueprep.html Dental Avenue Avueprep
https://pinkblue.in/ramsons-medi-safe-nitrile-exam-gloves-premium.html  Ramsons Medi Safe Nitrile Exam Gloves Premium
https://pinkblue.in/heraeus-gluma-bond5.html  Kulzer Gluma Bond5
https://pinkblue.in/meta-ad-seal-resin-sealer.html  Meta AD Seal
https://pinkblue.in/trikasafe-powdered-latex-exam-gloves.html Trikasafe Powdered Latex Exam Gloves
https://pinkblue.in/medicept-dental-xtracem-p-posterior-restorative-cement.html Medicept Dental Xtracem P (Posterior Restorative Cement)