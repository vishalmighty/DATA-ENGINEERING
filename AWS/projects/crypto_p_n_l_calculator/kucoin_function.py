import logging
from datetime import datetime,timedelta
import pandas as pd
import os

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',level=logging.INFO)
logger = logging.getLogger("Kucoin")

class Kucoin:
    """This will give you some interesting methods to get your P&L of Kucoin portfolio"""
    def __init__(self,user_client,trade_client,crypto):
        self.user_client = user_client
        self.trade_client = trade_client
        self.crypto = crypto
        
    def fetch_done_orders(self,symbol,days=30):
        trade_client = self.trade_client
        logger.info(f"Fetching orders for {symbol}...")
        orders = []
        current_page = 1
        
        end_time = datetime.utcnow()
        end_time = end_time + timedelta(hours=5, minutes=30)
        start_time = end_time - timedelta(days=days)

        while start_time < end_time:
            # Limit range to 7 days as Kucoin supports API call only for 7 days of this script development date
            range_end_time = min(start_time + timedelta(days=7), end_time)
            # Convert times to milliseconds
            start_at = int(start_time.timestamp() * 1000)
            end_at = int(range_end_time.timestamp() * 1000)
            
            while True:
                response = trade_client.get_order_list(
                    status='done',
                    symbol=symbol,
                    currentPage=current_page,
                    pageSize=500,
                    startAt=start_at,
                    endAt=end_at,
                )
                data = response.get('items', [])
                if not data:
                    break
                orders.extend(data)
                current_page += 1
            
            # Move the time range forward
            start_time = range_end_time
            current_page = 1  # Reset page counter for new time range

        logger.info(f"Total orders fetched: {len(orders)}")
        return orders
    
    # This function is used to get only my desired columns in output, This can be customized
    def transform_orders(self,symbol,orders):
        required_columns = {
            'createdAt': 'Date',
            'symbol': 'symbol',
            'side': 'side',
            'price': 'price',
            'size': 'Amount(in_coin)',
            'dealFunds': 'Amount(in_usdt)',
            'price': 'AveragePrice',
            'fee': 'fee',
            'tax': 'tax',
        }
        # Filter, rename, and transform the fields
        transformed_orders = []
        for order in orders:
            transformed_order = {}
            for old_key, new_key in required_columns.items():
                if old_key in order:
                    value = order[old_key]
                    # Convert `createdAt` field
                    if old_key == 'createdAt':
                        value = self.crypto.convert_millis_to_datetime(value)
                    transformed_order[new_key] = value
            transformed_order['AveragePrice'] = transformed_order.get('price', 0)
            transformed_orders.append(transformed_order)
        return transformed_orders
    
    def fetch_to_csv(self,days=30):
        # get the list of coins
        accounts = self.user_client.get_account_list()
        symbols = [account['currency'] for account in accounts if account['type'] == 'trade']
        all_orders = []
        
        for symbol in symbols:
            if symbol.upper() == "USDT":  # Skip USDT-USDT
                logger.info(f"Skipping symbol: {symbol}-USDT")
                continue
            try:
                full_symbol = symbol + '-USDT'
                symbol_orders = self.fetch_done_orders(full_symbol,days)
                successful_orders = [order for order in symbol_orders if order['cancelExist'] == False]
                transformed_orders = self.transform_orders(full_symbol,successful_orders)
                all_orders.extend(transformed_orders)
            except Exception as e:
                logger.error(f"Error fetching data for {symbol}: {e}")
        df = pd.DataFrame(all_orders)
        output_dir = "csv_files"
        os.makedirs(output_dir, exist_ok=True)
        df.to_csv("csv_files/kucoin_all_orders.csv", index=False)