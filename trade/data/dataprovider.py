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

logger = logging.getLogger(__name__)


class DataProvider(object):

    def __init__(self, config: dict, exchange: Exchange) -> None:
        self._config = config
        self._exchange = exchange

    def refresh(self, pairlist: List[Tuple[str, str]],
                helping_pairs: List[Tuple[str, str]] = None) -> None:
        """
        Refresh data, called with each cycle
        :param pairlist:
        :param helping_pairs:
        :return:
        """
        if helping_pairs:
            self._exchange.refresh_latest_ohlcv(pairlist + helping_pairs)
        else:
            self._exchange.refresh_latest_ohlcv(pairlist)


    @property
    def available_pairs(self) -> List[Tuple[str, str]]:
        """
        Return a list of tuples containing pair, tick_interval for which data is currently cached.
        Should be whitelist + open trades.
        :return:
        """

        return list(self._exchange.klines.keys())

    def ohlcv(self, pair: str, tick_interval: str = None, copy: bool = True) -> DataFrame:
        """
        get ohlcv data for the data given pair as DataFrame
        Please check `available_pairs` to verify which pairs are currently cached.

        :param pair:
        :param tick_interval:
        :param copy:
        :return:
        """
        if self.runmode in (RunMode.DRY_RUN, RunMode.LIVE):
            if tick_interval:
                pairtick = (pair, tick_interval)
            else:
                pairtick = (pair, self._config['tick_interval'])

            return self._exchange.klines(pairtick, copy=copy)
        else:
            return DataFrame()

    def historic_ohlcv(self, pair: str, ticker_interval: str) -> DataFrame:
        """
        get stored historic ohlcv data
        :param pair:
        :param ticker_interval:
        :return:
        """
        return load_pair_history(pair=pair, ticker_interval=ticker_interval,
                                 refresh_pairs= False,
                                 datadir=Path(self._config['datadir']) if self._config.get(
                                     'datadir'
                                 ) else None)
    def ticker(self, pair: str):
        """
        Return last ticker data
        :param pair:
        :return:
        """
        pass

    def orderbook(self, pair: str, max: int):
        """
        Return latest orderbook data
        :param pair:
        :param max:
        :return:
        """
        pass

    @property
    def runmode(self) -> RunMode:
        """
        Get runmode of the bot
        can be "live", "dry-run", "backtest", "edgecli", "hyperopt" or "other".
        """
        return RunMode(self._config.get('runmode', RunMode.OTHER))

