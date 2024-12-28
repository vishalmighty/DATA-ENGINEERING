import general_function
import kucoin_function
from kucoin.client import User, Trade

# Replace with your KuCoin API credentials
API_KEY = ""
API_SECRET = ""
API_PASSPHRASE = ""

# Initialize KuCoin Clients
user_client = User(key=API_KEY, secret=API_SECRET, passphrase=API_PASSPHRASE)
trade_client = Trade(key=API_KEY, secret=API_SECRET, passphrase=API_PASSPHRASE)

crypto = general_function.Crypto()
kucoin = kucoin_function.Kucoin(user_client,trade_client,crypto)

kucoin.fetch_to_csv(days=20)