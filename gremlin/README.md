#gremlin magic
This is a pixiedust magic that allows users to enter gremlin in a Jupyter notebook. It's designed to work with [IBM Graph](http://ibm.biz/ibm-graph), a Graph database as a service that's provided through [Bluemix](http://bluemix.net).

##Setup
###Clone the repo and install the gremlin magic

```
git clone git@github.com:ibm-cds-labs/pixiedust_incubator.git

cd pixiedust_incubator/gremlin
pip install -e .
```
###Import Pixiedust and the gremlin magic

```
import pixiedust
import pixiedust_gremlin
```

###Add your service credentials
```
graphUsername="<Your service instance user name>"
graphPassword="<Your service instance user password>"
graphUrl="<Your service instance apiURL>"
```

###Run your gremlin query
in a cell use the `%%gremlin` cell magic keyword to enter your gremlin query

```
%%gremlin var=results

def gt=graph.traversal();
gt.V().hasLabel("attendee").has("gender","female")
```
`var=results` will return the results of the query as a pandas data frame in the variable named `results`

The gremlin magic will automatically display the results using pixiedust's `display` method
