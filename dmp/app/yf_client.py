# Yahoo Finances API client
import requests

class YFClient():

    def __init__(self):
        self.headers = {
            'x-rapidapi-key': "2ece9be9cdmsh739b2749c63dce9p1f2e1fjsn6357a5098c13",
            'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }

    def get_historical(self, symbol, region):
        """
        symbol: like 'AMRN'
        region: like 'US'
        """
        url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-historical-data"
        querystring = {"symbol": symbol,"region":region}
        response=requests.request("GET", url, headers=self.headers, params=querystring)
        return response.text
