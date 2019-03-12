""" Kraken exchange subclass """
import logging
from typing import Dict

from trade.exchange import Exchange

logger = logging.getLogger(__name__)


class Kraken(Exchange):

    _params = {"trading_agreement": "agree"}

