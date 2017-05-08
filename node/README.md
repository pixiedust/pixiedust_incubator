# pixiedust_node

PixieDust extension that enable Jupyter Notebook user to invoke node.js commands

## Installation

```python
!pip install -e /Users/glynnb/projects/pixiedust_incubator/node
import pixiedust_node
```

## Running

Use the `%%node` prefix to indicate that a cell's content is JavaScript.

```js
%%node
print(new Date());
```

or you can use npm modules to interact with other external services. To install npm modules:

```py
!npm install -s request request-promise silverlining
```

and then "require" the modules in your Node.js code.

```js
%%node
var silverlining = require('silverlining');
```

## Display/print/store

There are three functions that can be used in JavaScript to interact with the Notebook

- print - print out a variable
- display - use Pixiedust's display function to visualise a JavaScript object
- store - turn a JavaScript array into a Pandas data frame

### print

```js
%%node
// connect to Cloudant using Silverlining
var url = 'https://reader.cloudant.com/cities';
var cities = silverlining(url);

// fetch number of cities per country
cities.count('country').then(print);
```

### display

```js
%%node

// fetch cities called York
cities.query({name: 'York'}).then(display);
```

### store

```js
%%node

// fetch the data and store in Pandas dataframe called 'x'
cities.all({limit: 2500}).then(function(data) {
  store(data, 'x');
});
```
