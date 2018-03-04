import requests
import endpoints
import json
import time
from RequestHelper import RequestHelper

class BitcoinHandler(object):

    def __init__(self,
        _root_url = "bitcoin",
        _bitcoin_endpoints = endpoints.BITCOIN
        ):

        self.root_url = endpoints.URL_ROOT[_root_url]
        self.btc_endpoints = _bitcoin_endpoints

    def buildEndpoint(self,_url):
        return self.root_url + _url

    def addressInfoRequest(self, _addr, _api_key = ""):
        endpoint = self.buildEndpoint(self.btc_endpoints["single_address"].format(
                                          addr = _addr,
                                          api_key = _api_key
                                          ))
        resp = requests.get(endpoint)

        return json.loads(resp.content)


    def getTransactionsFromBlock(self,blockNumber):
        pass


    def getBlocksForDay(self, _day = time.time()):
        _url = self.btc_endpoints["one_day_blocks"].format(time = int(_day) * 1000)
        endpoint = self.buildEndpoint(_url)
        resp = requests.get(endpoint)
        return json.loads(resp.content)

    def getSingleBlockInfo(self,_block_hash):
        _url = self.btc_endpoints["single_block"].format(block_hash = _block_hash)
        endpoint = self.buildEndpoint(_url)
        resp = requests.get(endpoint)
        return json.loads(resp.content)

    def getLatestBlockInfo(self):
        _url = self.btc_endpoints["latest_block"]
        endpoint = self.buildEndpoint(_url)
        resp = requests.get(endpoint)
        print resp.content
        return json.loads(resp.content)



class EthereumHandler(object):

    def __init__(self,
        _root_url = "ethereum",
        _ethereum_endpoints = endpoints.ETHEREUM
        ):

        self.reqHelper = RequestHelper()
        self.root_url = endpoints.URL_ROOT[_root_url]
        self.eth_endpoints = _ethereum_endpoints

    def buildEndpoint(self,_url):
        return self.root_url + _url

    def getLatestBlock(self):
        endpoint = self.eth_endpoints["FULL_chain_info"]
        resp = requests.get(endpoint, headers = self.reqHelper.buildHeader())
        print resp.content
        return json.loads(resp.content)["height"]


    def addressInfoRequest(self, _addr, _api_key = ""):
        endpoint = self.buildEndpoint(self.eth_endpoints.format(
                                          addr = _addr,
                                          ))
        resp = requests.get(endpoint)

        return json.loads(resp.content)

    def getTransactionsFromBlock(self,blockNumber):
        pass


    def getBlocksForDay(self, _day = time.time()):
        _url = self.eth_endpoints["one_day_blocks"].format(time = int(_day) * 1000)
        endpoint = self.buildEndpoint(_url)
        resp = requests.get(endpoint, headers = self.reqHelper.buildHeader())
        return json.loads(resp.content)

    def getSingleBlockInfo(self,_block_hash):
        _url = self.eth_endpoints["single_block"].format(block_hash = _block_hash)
        endpoint = self.buildEndpoint(_url)
        resp = requests.get(endpoint, headers = self.reqHelper.buildHeader())
        return json.loads(resp.content)

    def getTransactionInfo(self,_tx_id):
        endpoint = self.eth_endpoints["FULL_trans_info"].format(tx_id = _tx_id)
        resp = requests.get(endpoint, headers = self.reqHelper.buildHeader())
        return json.loads(resp.content)

    def getLatestBlockInfo(self):
        blhash = self.getLatestBlock()
        _url = self.eth_endpoints["FULL_block_info"].format(blocknum = blhash)
        resp = requests.get(_url,headers = self.reqHelper.buildHeader())
        result = json.loads(resp.content)
        return result

handlers = {
    "bitcoin" : BitcoinHandler,
    "ethereum" : EthereumHandler
}
