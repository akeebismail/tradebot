"""
Dataprovider
Responsible to provide data to the bot
including Klines, tickers, historic data
Common Interface for bot and strategy to access data.
"""
import logging
from pathlib import Path
from typing import List, Tuple
from pandas import DataFrame

from trade.data.history import load_pair_history
from trade.exchange import Exchange
from trade.state import RunMode