#! /bin/bash
#
# run.sh
scrapy crawl dantri_crawl -o items.json -t json -s LOG_FILE=scrapy.log
