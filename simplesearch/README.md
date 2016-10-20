# pixiedust_simplesearch

[Pixiedust](https://github.com/ibm-cds-labs/pixiedust) plugin that launches the [Simple Search Service](https://github.com/ibm-cds-labs/simple-search-service)  


## Installation

1. Clone the [Github repo](https://github.com/ibm-cds-labs/pixiedust_incubator)

2. Run `!pip install` from with a notebook cell:
	
	```
	!pip install --user --upgrade --no-deps -e <pixiedust_incubator>/simplesearch
	```
	
	where `<pixiedust_incubator>` is the full path to the directory of cloned `pixiedust_incubator` repo (e.g., `/Users/username/gitrepos/pixiedust_incubator`)  


## Usage

From a notebook cell run:

```
from pixiedust_simplesearch import *
simpleSearch(<search_query>, <service_url>)
```

where:  

**\<search\_query\>** _(Optional)_ - is the default query to run when launched (e.g., `"gender:Female"`, etc.). Default value is `"*:*"`.  
**\<service\_url\>** _(Optional)_ - is the url to the Simple Search Service. Default value is the _Game of Thrones_ (i.e., `http://sss-got.mybluemix.net`) search service.  

Examples:

```
simpleSearch()
```
```
simpleSearch("culture:Northmen AND gender:Female")
```
```
simpleSearch("http://simple-search-service-digitate-thema.mybluemix.net", "languages:Java")
```


## Uninstall

From a notebook cell run: `!pip uninstall -y pixiedust_simplesearch`
