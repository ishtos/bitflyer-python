## bitflyer-python

```bitdlyer-python``` is a wrapper library for [bitFlyer's HTTP API](https://lightning.bitflyer.com/docs?lang=en#pagination) 


## install 
Using pip
```
$ pip install bitflyer-python
```

## usage
```
# Public API and Private API 
import bitflyer
api = bitflyer.API(api_key=<API_KEY>, api_secret=<API_SECRET>)

# Only Public API
api = bitflyer.API()
```

Public API does not require API Key, while Private API requires API Key authentication.