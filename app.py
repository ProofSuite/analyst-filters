from src.Filter import filters
import web
from src import messages
import json

urls = (
    "/","INDEX",
    "/btc_recent_big_trans", "BTC_RECENT_BIG_TRANS",
    "/eth_recent_big_trans","ETH_RECENT_BIG_TRANS",
    "/lib/(.*)","LIB"
)

render = web.template.render("templates/")
app = web.application(urls, globals())


class INDEX(object):

    def GET(self):
        return render.index()


class ETH_RECENT_BIG_TRANS(object):

    def __init__(self):
        self.my_filters = filters
        self.eth_filter = self.my_filters["ethereum"]()


    def GET(self):
        eth_chain_info = self.eth_filter.getLargeTransactionsFromLatestBlock()
        return json.dumps({"response" : eth_chain_info})


class BTC_RECENT_BIG_TRANS(object):

    def __init__(self):
        self.my_filters = filters
        self.btc_filter = self.my_filters["bitcoin"]()

    def GET(self):
        btc_chain_info = self.btc_filter.getLargeTransactionsFromLatestBlock()
        return json.dumps({"response" : btc_chain_info})


class LIB(object):
    def GET(self,file):
        try:
            f = open('./lib/' + file, 'r')
            return f.read()
        except:
            return messages.ERR_404


if __name__ == "__main__":
    app.run()
