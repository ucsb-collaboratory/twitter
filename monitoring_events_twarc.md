---
layout: page
title: Monitoring Events with Twarc
---

[Back to Home Page](index.md)  

# Monitoring Events Using twarc Filter and Search 

This is a narrative guide outlining how to start a search and a filter and combine the results once the event is over. We're going to running this on a recent news event about the [Governor of Florida](https://www.nbcnews.com/politics/elections/gop-gov-desantis-signs-restrictive-new-voting-florida-dems-fear-n1266415), but any topic will work. 
 

#### Table of Contents
[Before You Start](#before)  
[Filter and Search](#filtersearch)  
[Dehydrate](#dehydrate)   
[Combine](#combine)   
[Rehydrate](#rehydrate)   
[Deduplicate](#deduplicate)   
[Analysis](#analysis)   


<a name="before.py"/>   

## Before You Start

Before starting this guide, make sure you have [twarc](https://github.com/DocNow/twarc) installed and setup. 


<a name="filtersearch.py"/>    

## Filter and Search

Next you're going to want to run _twarc filter_ which collects tweets from the Twitter stream matching the filter criteria, and _twarc search_ which collects tweets made in the past seven days matching the search criteria. There are a couple of ways this can be done, but the most preferable is to run two command line windows.

   
    twarc filter desantis > desantis_filter.jsonl

    twarc search desantis > desantis_search.jsonl


The search command will finish before the filter which will keep running until manually stopped. Once we are finished running the search, we can work on combining the two JSONLs. 


<a name="dehydrate"/>    

## Dehydrate

We will start by dehydrating the two collected datasets.


    twarc dehydrate desantis_filter.jsonl > desantis_filter.txt 
       
    twarc dehydrate desantis_search.jsonl  > desantis_search.txt
     

<a name="combine"/>   
    
## Combine    
   
Now that the datasets have been dehydrated, we can use the python program _combine.py_ [here](https://github.com/ucsb-collaboratory/twitter/blob/main/combine.py) to combine them.
    
    
    python utils/combine.py 
    
And enter the input requests as follows:
   
    Enter the name of your filter txt: desantis_filter.txt
    Enter the name of your search txt: desantis_search.txt
    Enter the name of your output txt: desantis_fs.txt    


<a name="rehydrate"/>      

## Rehydrate

Now that we have our merged dataset, we can rehydrate the dataset. 

    twarc hydrate desantis_fs.txt > desantis_fs.jsonl


<a name="deduplicate"/>         
    
## Deduplicate
    
Then, we can run _deduplicate.py_ to remove any overlap from the merging of the two datasets. 

    
    python utils/deduplicate.py desantis_fs.jsonl > desantis.jsonl
    
    
All of the usage is displayed in the command line here:


![DESANTIS1](/assets/desantis1.png)

![DESANTIS2](/assets/desantis2.png)


<a name="analysis.py"/>   

## Analysis

Now that we have our merged dataset without duplicate ID's, we can perform analysis using the python utilities provided with twarc. See the [twarc](https://ucsb-collaboratory.github.io/twitter/twarc.html) page for more information and links the the repository.    
 
You can download the DeSantis files from the [twitter](https://github.com/ucsb-collaboratory/twitter) repo.    
    
[Back To Top](#monioring-events-using-twarc-filter-and-search)
