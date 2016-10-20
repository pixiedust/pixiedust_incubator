# pixiedust_codegen

[Pixiedust](https://github.com/ibm-cds-labs/pixiedust) plugin that generates code snippets for common tasks  


## Installation

1. Clone the [Github repo](https://github.com/ibm-cds-labs/pixiedust_incubator)

2. Run `!pip install` from with a notebook cell:
	
	```
	!pip install --user --upgrade --no-deps -e <pixiedust_incubator>/codegenerator
	```
	
	where `<pixiedust_incubator>` is the full path to the directory of cloned `pixiedust_incubator` repo (e.g., `/Users/username/gitrepos/pixiedust_incubator`)  


## Usage

From a notebook cell run:

```
from pixiedust_codegenerator import *
codeGenerator()
```

## Uninstall

From a notebook cell run: `!pip uninstall -y pixiedust_codegenerator`
