import logging
"""
The logging module provides a flexible framework for emitting log messages 
from Python programs. It's essential for debugging, monitoring, and auditing applications.
"""

"""
Logging Levels
Level	    Numeric Value	Usage
DEBUG	    10	            Detailed info for diagnostics
INFO	    20	            Confirmation that things work
WARNING	    30	            Indication of potential issues
ERROR	    40	            Serious problems
CRITICAL	50	            Fatal errors
"""

# Simple setup (outputs to console)
logging.basicConfig(level=logging.INFO)
logging.warning('This is a warning')  # Will be displayed
logging.debug('This is debug info')   # Will NOT be displayed


logging.basicConfig(
    filename='app.log',
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

logger = logging.getLogger('my_app')
logger.info('Application started')