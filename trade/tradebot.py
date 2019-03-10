import copy
import logging
import time
import traceback
from datetime import datetime
from typing import Any, Callable, Dict, List, Optional, Tuple

import arrow
from requests.exceptions import RequestException

from trade import (DependencyException, OperationalException, TemporaryError, __version__, constant, persistence)
from trade.state import State
logger = logging.getLogger(__name__)


class Tradebot(object):
    """
    Freqtrade is the main class of the bot.
    This is from here the bot start its logic.
    """

    def __init__(self, config: Dict[str, Any]) -> None:
        """
        Init all variables and objects the bot needs to work
        :param config: configuration dict, you can use Configuration.get_config()
        to get the config dict.
        """
        logger.info('Starting trade %s',__version__)

        # Init bot states
        self.state = State.STOPPED

        # Init bot objects
        self.config = config
        self.strategy: IStrategy =