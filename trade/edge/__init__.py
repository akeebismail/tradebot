# pragma pylint: disable=W0603
""" Edge positioning package """
import logging
from pathlib import Path
from typing import Any, Dict, NamedTuple

import arrow
import numpy as np
import utils_find_1st as utfirst
from pandas import DataFrame

from trade import constant, OperationalException
from trade.arguments import Arguments
from trade.arguments import TimeRange
from trade.data import history
