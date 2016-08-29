# pixiedust_twitterdemo

[Pixiedust](https://github.com/ibm-cds-labs/pixiedust) demo of the [Sentiment Analysis of Twitter Hashtags](https://developer.ibm.com/clouddataservices/sentiment-analysis-of-twitter-hashtags/) and [Real-time Sentiment Analysis of Twitter Hashtags with Spark](https://developer.ibm.com/clouddataservices/2016/01/15/real-time-sentiment-analysis-of-twitter-hashtags-with-spark/) tutorials  


## Installation

1. Clone the [Github repo](https://github.com/ibm-cds-labs/pixiedust_incubator)

2. Run `!pip install` from with a notebook cell:
  
  ```
  !pip install --user --upgrade --no-deps -e <pixiedust_incubator>/twitterdemo
  ```
  
  where `<pixiedust_incubator>` is the full path to the directory of cloned `pixiedust_incubator` repo (e.g., `/Users/username/gitrepos/pixiedust_incubator`)  


## Usage

From a notebook cell run:

```
from pixiedust_twitterdemo import *
twitterDemo()
```

## Uninstall

From a notebook cell run: `!pip uninstall pixiedust_twitterdemo `