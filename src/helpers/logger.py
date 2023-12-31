"""Main logger"""
import logging
import os

# https://docs.python.org/3/library/logging.html#module-logging
formatter = logging.Formatter(
    "%(asctime)s.%(msecs)03d %(levelname)s "
    "%(filename)s:%(lineno)s: %(message)s",
    "%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("log")

# Root logger: call program like: DEBUG=true pytest
if os.environ.get("DEBUG"):
    log.setLevel(logging.DEBUG)
else:
    log.setLevel(logging.INFO)

# https://docs.python.org/3/library/logging.handlers.html#logging.StreamHandler
# Console output default: sys.stderr
handler = logging.StreamHandler()
handler.setFormatter(formatter)
log.addHandler(handler)


def log_and_report(message=None, trace=None):
    if message:
        log.debug(message)
    if trace:
        log.debug(trace)


# https://docs.python.org/3/library/logging.html#logger-objects
def get_logger():
    """Multiple calls to getLogger() with the same name will always return
    a reference to the same Logger object."""
    return logging.getLogger("log")
