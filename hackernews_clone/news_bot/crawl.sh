#!/bin/bash

cd ~/hackernews_clone_code/news_bot
source ../env1/bin/activate
PATH=$PATH:/usr/local/bin
export PATH
scrapy crawl example
