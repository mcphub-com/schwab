import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/apidojo/api/schwab'

mcp = FastMCP('schwab')

@mcp.tool()
def auto_complete(MatchChars: Annotated[str, Field(description='')]) -> dict: 
    '''Get suggestion by word or phase'''
    url = 'https://schwab.p.rapidapi.com/auto-complete'
    headers = {'x-rapidapi-host': 'schwab.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'MatchChars': MatchChars,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_get_movers(rankType: Annotated[str, Field(description='One of the following : MostActive|PctChgGainers|PctChgLosers|NetGainers|NetLosers|High52Wk|Low52Wk')]) -> dict: 
    '''List recent movers in the market'''
    url = 'https://schwab.p.rapidapi.com/market/v2/get-movers'
    headers = {'x-rapidapi-host': 'schwab.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'rankType': rankType,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_get_indices() -> dict: 
    '''List all available market indices'''
    url = 'https://schwab.p.rapidapi.com/market/v2/get-indices'
    headers = {'x-rapidapi-host': 'schwab.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def market_get_futures() -> dict: 
    '''Get future reports about the market * There are response images in encoded base 64 string, you need to decode to get the images yourself'''
    url = 'https://schwab.p.rapidapi.com/market/get-futures'
    headers = {'x-rapidapi-host': 'schwab.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def market_get_top_mentions() -> dict: 
    '''List top mentions stock quotes'''
    url = 'https://schwab.p.rapidapi.com/market/get-top-mentions'
    headers = {'x-rapidapi-host': 'schwab.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def market_get_sectors() -> dict: 
    '''Get brief information about all sectors'''
    url = 'https://schwab.p.rapidapi.com/market/get-sectors'
    headers = {'x-rapidapi-host': 'schwab.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def market_get_reports() -> dict: 
    '''Get reports about the market * You need to use .../content/decrypt endpoint to decrypt content returned by Url fields.'''
    url = 'https://schwab.p.rapidapi.com/market/get-reports'
    headers = {'x-rapidapi-host': 'schwab.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def market_get_volatility() -> dict: 
    '''Get market volatility * There are response images in encoded base 64 string, you need to decode to get the images yourself'''
    url = 'https://schwab.p.rapidapi.com/market/get-volatility'
    headers = {'x-rapidapi-host': 'schwab.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def market_get_indices() -> dict: 
    '''List all available market indices'''
    url = 'https://schwab.p.rapidapi.com/market/get-indices'
    headers = {'x-rapidapi-host': 'schwab.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def market_get_movers(rankType: Annotated[str, Field(description='One of the following : MostActives|PctChgGainers|PctChgLosers|NetGainers|NetLosers|52WkHigh|52WkLow')],
                      exchange: Annotated[str, Field(description='One of the following : US|USN|USQ|USA')],
                      sectorCusip: Annotated[Union[str, None], Field(description='The value of Sectors/SectorCusip returned right in this endpoint.')] = None) -> dict: 
    '''List recent movers in the market'''
    url = 'https://schwab.p.rapidapi.com/market/get-movers'
    headers = {'x-rapidapi-host': 'schwab.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'rankType': rankType,
        'exchange': exchange,
        'sectorCusip': sectorCusip,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_summary(symbol: Annotated[str, Field(description='The symbol to get information')]) -> dict: 
    '''Get summary information of symbol'''
    url = 'https://schwab.p.rapidapi.com/symbols/get-summary'
    headers = {'x-rapidapi-host': 'schwab.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_quotes(symbol: Annotated[str, Field(description='The symbol to get information')]) -> dict: 
    '''Get quotes of a symbol'''
    url = 'https://schwab.p.rapidapi.com/symbols/get-quotes'
    headers = {'x-rapidapi-host': 'schwab.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_earnings(symbol: Annotated[str, Field(description='The symbol to get information')]) -> dict: 
    '''Get earnings of a symbol'''
    url = 'https://schwab.p.rapidapi.com/symbols/get-earnings'
    headers = {'x-rapidapi-host': 'schwab.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_dividends(symbol: Annotated[str, Field(description='The symbol to get information')]) -> dict: 
    '''Get dividends of a symbol'''
    url = 'https://schwab.p.rapidapi.com/symbols/get-dividends'
    headers = {'x-rapidapi-host': 'schwab.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_share_profile(symbol: Annotated[str, Field(description='The symbol to get information')]) -> dict: 
    '''Get share-profile of a symbol'''
    url = 'https://schwab.p.rapidapi.com/symbols/get-share-profile'
    headers = {'x-rapidapi-host': 'schwab.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_business_summary(symbol: Annotated[str, Field(description='The symbol to get information')]) -> dict: 
    '''Get company information of a symbol'''
    url = 'https://schwab.p.rapidapi.com/symbols/get-business-summary'
    headers = {'x-rapidapi-host': 'schwab.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_margin_requirements(symbol: Annotated[str, Field(description='The symbol to get information')]) -> dict: 
    '''Get margin-requirements of a symbol'''
    url = 'https://schwab.p.rapidapi.com/symbols/get-margin-requirements'
    headers = {'x-rapidapi-host': 'schwab.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_chart(symbol: Annotated[str, Field(description='The symbol to get information')],
                      duration: Annotated[Union[str, None], Field(description='One of the followings : Day|Week|Month|Year')] = None) -> dict: 
    '''Get chart of a symbol'''
    url = 'https://schwab.p.rapidapi.com/symbols/get-chart'
    headers = {'x-rapidapi-host': 'schwab.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'duration': duration,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_advanced_chart(endDate: Annotated[str, Field(description="The format is yyyy-MM-dd'T'HH:mm:ss")],
                               startDate: Annotated[str, Field(description="The format is yyyy-MM-dd'T'HH:mm:ss")],
                               symbol: Annotated[str, Field(description='The symbol to get information')],
                               dataPeriod: Annotated[Union[str, None], Field(description='One of the following : Minute|Hour|Day|Week|Month')] = None) -> dict: 
    '''Get data to draw chart'''
    url = 'https://schwab.p.rapidapi.com/symbols/get-advanced-chart'
    headers = {'x-rapidapi-host': 'schwab.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'endDate': endDate,
        'startDate': startDate,
        'symbol': symbol,
        'dataPeriod': dataPeriod,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()


if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
