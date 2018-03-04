URL_ROOT = {
    "ethereum" : "https://api.etherscan.io",
    "bitcoin" : "https://blockchain.info",
    "pricing" : "https://api.coinmarketcap.com"
}

BITCOIN = {
    "single_block" : "/rawblock/{block_hash}",
    "single_transaction" : "/rawtx/{tx_hash}",
    "chart_data" : "/charts/{chart-type}?format=json",
    "block_height" : "/block-height/{block_height}?format=json",
    "single_address":"/rawaddr/{addr}",
    "multi_addresses" : "/multiaddr?active={addresses}", #Addresses seperated by |
    "unspent_outputs" : "/unspent?active={address}",
    "balance" : "/balance?active={address}",
    "latest_block" : "/latestblock",
    "unconfirmed_transactions" : "/unconfirmed-transactions?format=json",
    "one_day_blocks" : "/blocks/{time}?format=json", #$time_in_milliseconds
    "pool_blocks" : "/blocks/{pool_name}?format=json"
}

ETHEREUM = {
    "FULL_trans_info" : "https://api.blockcypher.com/v1/eth/main/txs/{tx_id}?token=42ca171d67344303b5bb8db190ba841e",
    "FULL_block_info" : "https://api.blockcypher.com/v1/eth/main/blocks/{blocknum}?token=42ca171d67344303b5bb8db190ba841e",
    "FULL_chain_info" : "https://api.blockcypher.com/v1/eth/main?token=42ca171d67344303b5bb8db190ba841e",
    "acct_raw" : "/api?module={module}&action={action}&{args}",
    "acct_balance_single_address" : "/api?module=account&action=balance&address={addr}&tag=latest&apikey={api_key}",
    "acct_balance_multi_addresses" : "/api?module=account&action=balancemulti&address={addresses}&tag=latest&apikey={api_key}",
    "acct_normal_transactions" : "/api?module=account&action=txlist&address={address}&startblock={start_block}}&endblock={end_block}&sort=asc&apikey={api_key}",
    "acct_internal_transactions_by_addr" : "/api?module=account&action=txlistinternal&address={address}&startblock={start_block}&endblock={end_block}&sort=asc&apikey={api_key}",
    "acct_internal_transactions_by_txhash" : "/api?module=account&action=txlistinternal&txhash={txhash}&apikey={api_key}",
    "acct_internal_transactions_by_addr" : "/api?module=account&action=getminedblocks&address={address}&blocktype=blocks&apikey={api_key}",
    "contracts_contract_abi" : "/api?module=contract&action=getabi&address={address}&apikey={api_key}",
    "trans_contract_ex_stat" : "/api?module=transaction&action=getstatus&txhash={txhash}&apikey={api_key}",
    "trans_trans_receipt_stat" : "/api?module=transaction&action=gettxreceiptstatus&txhash={txhash}&apikey={api_key}",
    "blocks_block_rewards" : "/api?module=block&action=getblockreward&blockno={blocknum}&apikey={api_key}",
}

TOKENS = {
    "ticker" : "/v1/ticker/",
    "ticker_lim" : "/v1/ticker/?limit={lim}",
    "ticker_start_lim" : "/v1/ticker/?start={start}&limit={lim}",
    "ticker_conversion_lim" : "/v1/ticker/?convert={conversion}&limit={lim}",
    "ticker_currency" : "/ticker/{currency_id}/",
    "ticker_currency_conversion" : "/ticker/{currency_id}/?convert={conversion}",
    "global" : "/v1/global/",
    "global_conversion" : "/v1/global/?convert={conversion}"
}
