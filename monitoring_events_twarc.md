---
date: 2021-05-05
output: html
---

[Back to Home Page](index.md)   

#### Table of Contents


# Monioring Events Using Twarc's Filter and Search 

This is a narrative guide outlining how to start a search and a filter and combine the results once the event is over. We're going to running this on a recent news event above a [Florida Senator](https://www.nbcnews.com/politics/elections/gop-gov-desantis-signs-restrictive-new-voting-florida-dems-fear-n1266415), but any topic will work. 


## Before You Start

Before starting this guide, make sure you have [twarc](https://github.com/DocNow/twarc) installed and setup. 


Next you're going to want to run _twarc filter_ and _twarc search_. There are a couple of ways this can be done, but the most preferable is to run two command line windows.

    twarc filter desantis > desantis_filter.jsonl

![FILTER](/assets/desantis_filter.png)

    twarc search desantis > desantis_search.jsonl

![SEARCH](/assets/desantis_search.png)


The filter command will finish before the search which will keep running until manually stopped. Once we are finished running the search, we can work on combining the two JSONLs. 

We will start by dehydrating the two collected datasets, then we will use the python program _ _ [here]() to combine them.

    twarc dehydrate desantis_filter.jsonl   
       
    twarc dehydrate desantis_search.jsonl  

Now that we have one dataset, we can rehydrate and run _deduplicate.py_ to remove any overlap from the two datasets. 

    twarc hydrate desantis_fs.jsonl
    
    python utils/deduplicate.py desantis_fs.jsonl > desantis.jsonl
