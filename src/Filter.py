from RequestMaker import handlers
import time

#5000000000

class BitcoinFilter(object):
    def __init__(self, _handler = "bitcoin", _track_amnt = 5000000000):
        self.my_handler = handlers[_handler]()
        self.linkroot = "https://blockchain.info/tx/{tx}"
        self.track_amnt = _track_amnt

    def getBigTransactions(self,_trans_list):
        bigTrans = []
        for trans in _trans_list:
            trans_hash = trans["hash"]
            trans_cumulative = sum([int(output["value"]) for output in trans["out"]])
            if trans_cumulative >= self.track_amnt:
                bigTrans.append({"inputs": trans["inputs"],
                                 "outputs" : trans["out"],
                                 "txHash": trans_hash,
                                 "link": self.linkroot.format(tx = trans_hash)})

        return bigTrans

    def getLargeTransactionsFromAddr(self, _addr):
        # returns OUTPUT SU
        resp = self.my_handler.addressInfoRequest(_addr)
        transactions = resp["txs"]
        return self.getBigTransactions(transactions)


    def getLargeTransactionsFromBlock(self,_day = time.time()):
        blocks_for_day = self.my_handler.getBlocksForDay(_day)

        # [u'nonce', u'received_time', u'fee', u'ver', u'tx', u'prev_block', u'relayed_by', u'height', u'block_index', u'mrkl_root', u'time', u'hash', u'main_chain', u'bits', u'n_tx', u'size']
        bigTransList = []

        for block in blocks_for_day["blocks"]:
            block_info = self.my_handler.getSingleBlockInfo(block["hash"])
            bigTransList.extend(self.getBigTransactions(block_info["tx"]))

        return bigTransList


    def getLargeTransactionsFromLatestBlock(self,_day = time.time()):
        blocks_for_day = self.my_handler.getBlocksForDay(_day)
        bigTransList = []
        block_info = self.my_handler.getLatestBlockInfo()
        transactions = self.my_handler.getSingleBlockInfo(block_info["hash"])["tx"]
        bigTransList.extend(self.getBigTransactions(transactions))

        return bigTransList


#625000000000000000000
#1000000000000000000
class EthereumFilter(object):
    def __init__(self, _handler = "ethereum", _track_amnt = 625000000000000000000):
        self.my_handler = handlers[_handler]()
        self.linkroot = "https://etherscan.io/tx/0x{tx}"
        self.track_amnt = _track_amnt

    def getBigTransactions(self,_trans_list):
        bigTrans = []
        for trans in _trans_list:
            trans_hash = trans["hash"]
            trans_value = int(trans["total"])

            print "%s ::: %s" % (self.track_amnt,trans_value)
            
            if trans_value >= self.track_amnt:
                bigTrans.append({"inputs": trans.get("inputs"),
                                 "outputs" : trans.get("out"),
                                 "txHash": trans_hash,
                                 "link": self.linkroot.format(tx = trans_hash)})

        return bigTrans

    def getLargeTransactionsFromLatestBlock(self):
        block = self.my_handler.getLatestBlockInfo()
        #print "BLOCK ::: %s" % block
        internal_txids = block["internal_txids"]
        normal_txids = block["txids"]
        #print len(internal_txids)
        print len(normal_txids)
        #inner_txs = [self.my_handler.getTransactionInfo(tx) for tx in internal_txids[0:9]]
        txs = [self.my_handler.getTransactionInfo(tx) for tx in normal_txids]
#        return {"internal_txs": self.getBigTransactions(inner_txs) ,"txs":self.getBigTransactions(txs)}
        final_transactions = []
        final_transactions.extend(txs)
        return self.getBigTransactions(final_transactions)

filters = {
    "bitcoin": BitcoinFilter,
    "ethereum" : EthereumFilter
}
