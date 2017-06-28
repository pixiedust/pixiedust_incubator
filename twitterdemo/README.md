# pixiedust_twitterdemo

[Pixiedust](https://github.com/ibm-watson-data-lab/pixiedust) demo of the [Sentiment Analysis of Twitter Hashtags](https://developer.ibm.com/clouddataservices/sentiment-analysis-of-twitter-hashtags/) and [Real-time Sentiment Analysis of Twitter Hashtags with Spark](https://developer.ibm.com/clouddataservices/2016/01/15/real-time-sentiment-analysis-of-twitter-hashtags-with-spark/) tutorials  


## Prerequisites

This demo requires
 * a Watson Tone Anlyzer service instance
 * a Twitter application setup

Follow the [tutorial instructions](https://developer.ibm.com/clouddataservices/2016/01/15/real-time-sentiment-analysis-of-twitter-hashtags-with-spark/) in sections _Initiate Watson Tone Analyzer Service_ and _Generate OAuth Credentials for Twitter_ to prepare the prerequisites.

## Installation

1. Clone the [Github repo](https://github.com/ibm-watson-data-lab/pixiedust_incubator)

2. Run `!pip install` from with a notebook cell:
  
  ```
  !pip install pixiedust --upgrade
  !pip install --user --upgrade --no-deps -e <pixiedust_incubator>/twitterdemo
  ```
  
  > Replace `<pixiedust_incubator>` with the full path to the directory of cloned `pixiedust_incubator` repo (e.g., `/Users/username/gitrepos/pixiedust_incubator`)  


## Running the demo application

From a notebook run the following cells:

```
import pixiedust

twitterConsumerKey = "<TODO-replace-with-your-consumer-key>"
twitterConsumerSecret = "<TODO-replace-with-your-consumer-secret>"
twitterAccessToken = "<TODO-replace-with-your-access-token>"
twitterAccessTokenSecret = "<TODO-replace-with-your-access-token-secret>"
toneAnalyzerPassword = "<TODO-replace-with-your-tone-analyzer-password>"
toneAnalyzerUserName = "<TODO-replace-with-your-tone-analyzer-username>"

%%scala
val demo = com.ibm.cds.spark.samples.PixiedustStreamingTwitter
demo.setConfig("twitter4j.oauth.consumerKey",twitterConsumerKey)
demo.setConfig("twitter4j.oauth.consumerSecret",twitterConsumerSecret)
demo.setConfig("twitter4j.oauth.accessToken",twitterAccessToken)
demo.setConfig("twitter4j.oauth.accessTokenSecret",twitterAccessTokenSecret)
demo.setConfig("watson.tone.url","https://gateway.watsonplatform.net/tone-analyzer/api")
demo.setConfig("watson.tone.password",toneAnalyzerPassword)
demo.setConfig("watson.tone.username",toneAnalyzerUserName)
demo.setConfig("checkpointDir", System.getProperty("user.home") + "/pixiedust/ssc")

from pixiedust_twitterdemo import *

twitterDemo()
```

## Uninstall

From a notebook cell run: `!pip uninstall -y pixiedust_twitterdemo `
