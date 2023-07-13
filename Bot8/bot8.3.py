from twelvedata import TDClient
import os
from dotenv import load_dotenv

load_dotenv()
td = TDClient(apikey=os.getenv("TWELVE_API_KEY"))
# limited for free subscriber, so I can not use NG for getting the natural gas price
print(td.price(symbol="AAPL").as_json())
