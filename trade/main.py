#!/usr/bin/env python3
"""
Main Kibbtrade bot script.
Read the documentation to know what cli arguments you need.
"""
import logging
import sys
from argparse import Namespace
from typing import List

logger = logging.getLogger("kibbtrade")

def main(sysargv: List[str]) -> None:
    """
    This function will initiate the bot and start the trading loop.
    :return: None
    """
    arguments = Arguments(sysargv, 'Free, Open source crypto trading bot')