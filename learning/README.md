# pixiedust_learning

[Pixiedust](https://github.com/ibm-watson-data-lab/pixiedust) plugin that provide tutorial notebook on demand generation  


## Installation

1. Clone the [Github repo](https://github.com/ibm-watson-data-lab/pixiedust_incubator)

2. From with a notebook cell run:
	
	```
	!pip install --user --upgrade --no-deps -e <pixiedust_incubator>/learning
	```
	
	where `<pixiedust_incubator>` is the full path to the directory of cloned `pixiedust_incubator` repo (e.g., `/Users/username/gitrepos/pixiedust_incubator`)  


## Usage

From a notebook cell run:

```
from pixiedust_learning import *
startCourse()
```

## Uninstall

From a notebook cell run: `!pip uninstall -y pixiedust_learning`
