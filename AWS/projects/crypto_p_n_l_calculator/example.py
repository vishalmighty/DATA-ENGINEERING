# python/python3 -m pip install python-binance,kucoin-python
import general_function
import kucoin_function
import binance_function
from kucoin.client import User, Trade
from binance.client import Client

# Replace with your KuCoin API credentials
API_KEY = ""
API_SECRET = ""
API_PASSPHRASE = ""

# Initialize KuCoin Clients
user_client = User(key=API_KEY, secret=API_SECRET, passphrase=API_PASSPHRASE)
trade_client = Trade(key=API_KEY, secret=API_SECRET, passphrase=API_PASSPHRASE)

crypto = general_function.Crypto()
kucoin = kucoin_function.Kucoin(user_client,trade_client,crypto)

# kucoin.fetch_to_csv(days=20)

# Initialize Binance Client
BINANCE_API_KEY = ''
BINANCE_API_SECRET = ''
client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)
binance = binance_function.Binance(client,crypto)
binance.fetch_to_csv()