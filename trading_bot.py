import ccxt
from config import BINANCE_API_KEY, BINANCE_SECRET_KEY

def place_trade(symbol, order_type="market", side="buy", amount=0.01):
    """ Places a trade on Binance using CCXT """
    exchange = ccxt.binance({
        'apiKey': BINANCE_API_KEY,
        'secret': BINANCE_SECRET_KEY
    })

    order = exchange.create_order(symbol=symbol, type=order_type, side=side, amount=amount)
    return order
