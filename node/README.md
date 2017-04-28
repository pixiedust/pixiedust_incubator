# pixiedust_node

PixieDust extension that enable Jupyter Notebook user to invoke node.js commands

## Installation

```python
!pip install -e /Users/glynnb/projects/pixiedust_incubator/node
import sys
sys.path.append('/Users/glynnb/projects/pixiedust_incubator/node')
import pixiedust_node
```

## Running

Use the `%%node` prefix to indicate that a cell's content is JavaScript.

```js
%%node
// connect to Cloudant using Silverlining
var url = 'https://hipecieksoomarepacearest:badb86e98a57bfe1701a628df6151e7039c4d802@reader.cloudant.com/cities';
var cities = silverlining(url);

// fetch number of cities per country
cities.count('country').then(print);
```