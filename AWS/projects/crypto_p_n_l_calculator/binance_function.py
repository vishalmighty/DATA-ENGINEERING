import logging
from datetime import datetime,timedelta
import pandas as pd
import os

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',level=logging.INFO)
logger = logging.getLogger("Kucoin")

class Binance:
    """This will give you some interesting methods to get your P&L of Binance portfolio"""
    def __init__(self,client,crypto):
        self.client = client
        self.crypto = crypto
        
    def fetch_filled_orders(self,symbol):
        logger.info(f"Fetching orders for {symbol}...")
        orders = []
        try:
            raw_orders = self.client.get_all_orders(symbol=symbol)
            for order in raw_orders:
                if order['status'] == 'FILLED':  # Only include completed orders
                    orders.append({
                        'symbol': symbol if '-' in symbol else symbol.replace("USDT","-USDT"),
                        'side': order['side'].lower(),
                        'size': float(order['executedQty']),
                        'price': float(order['price']),
                        'AveragePrice': float(order['price']),
                        'fee': float(order.get('commission', 0)),
                        'tax': float(order.get('tax', 0)),
                        'Amount(in_coin)': float(order.get('executedQty', 0)),
                        'Amount(in_usdt)': float(order['price']) * float(order.get('executedQty', 0)),
                        'Date':  self.crypto.convert_millis_to_datetime(order.get('time'))
                    })
        except Exception as e:
            logger.error(f"Error fetching orders for {symbol}: {e}")
        return orders
    
    def fetch_to_csv(self):
        valid_symbols = [ticker['symbol'] for ticker in self.client.get_all_tickers()]
        accounts = self.client.get_account()['balances']
        symbols = [account['asset'] for account in accounts if float(account['free']) > 0 or float(account['locked']) > 0]
        
        all_orders = []
        for asset in symbols:
            if asset.upper() == "LDUSDT":
                logger.info(f"Skipping symbol: {asset}")
                continue
            try:
                asset = asset[2:] if asset.startswith("LD") else asset
                valid_pair = f"{asset}USDT"
                orders = self.fetch_filled_orders(valid_pair)
                all_orders.extend(orders)
                if not orders:
                    logger.info(f"No orders found for {valid_pair}")
                    continue
            except Exception as e:
                logger.error(f"Error processing {asset}: {e}")

        if all_orders:
            df = pd.DataFrame(all_orders)
            output_dir = "csv_files"
            os.makedirs(output_dir, exist_ok=True)
            df.to_csv("csv_files/binance_all_orders.csv", index=False)
            logger.info("Orders saved to binance_all_orders.csv")
        else:
            logger.info("No orders to save.")
