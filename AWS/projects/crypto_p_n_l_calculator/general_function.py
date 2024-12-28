import logging
from datetime import datetime,timedelta

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',level=logging.INFO)
logger = logging.getLogger("General crypto")

class Crypto:
    """This will give you some general methods"""
    def convert_millis_to_datetime(self,milliseconds):
        seconds = milliseconds / 1000.0
        dt = datetime.utcfromtimestamp(seconds)
        ist_dt = dt + timedelta(hours=5, minutes=30)
        formatted_date = ist_dt.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]  
        return formatted_date