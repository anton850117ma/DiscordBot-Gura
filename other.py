import requests
import json
import io
import aiohttp

def get_quote():
    ''' get quote '''
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)
