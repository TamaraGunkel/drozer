#!/usr/bin/env python3

import logging
import sys

from mwr.common import logger

from drozer.console import Console

logger.setLevel(logging.DEBUG)
logger.addStreamHandler()

Console().run(sys.argv[2::])
