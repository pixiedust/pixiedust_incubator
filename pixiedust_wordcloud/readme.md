# pixiedust_wordcloud

[Word Cloud Visualization plugin](https://pypi.python.org/pypi/pixiedust-wordcloud) for [Pixiedust](https://github.com/ibm-cds-labs/pixiedust)

## Installation

1. Clone the [Github repo](https://github.com/ibm-cds-labs/pixiedust_incubator)

2. Run `!pip install` from with a notebook cell:
  
  ```
  !pip install pixiedust --upgrade
  !pip install --upgrade --no-deps -e <pixiedust_incubator>/pixiedust_wordcloud
  ```
  
  > Replace `<pixiedust_incubator>` with the full path to the directory of cloned `pixiedust_incubator` repo (e.g., `/Users/username/gitrepos/pixiedust_incubator`)  


## Running the visualization application

To try out the visualization, from a notebook cell run the following:

```
import pixiedust
import pixiedust_wordcloud

df = pixiedust.sampleData(7)
df2 = df.groupBy("street").count()

display(df2)
```

Select **Simple Word Cloud** from the charts dropdown menu.

## Uninstall

From a notebook cell run: `!pip uninstall -y pixiedust_wordcloud`
