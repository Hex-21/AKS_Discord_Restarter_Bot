# MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# (c) 2024 Hex https://github.com/Hex-21/
import datetime
import json
import inspect
import os
from os import mkdir

LOG_LEVELS = {
    "DEBUG": 0,
    "INFO": 1,
    "WARNING": 2,
    "EXCEPTION": 3,
    "ERROR": 4,
    "CRITICAL": 5,
}


def format_log(level, message, logger=__name__, extra=None):
    frame = inspect.currentframe()
    while frame.f_globals['__name__'] == __name__:
        frame = frame.f_back

    module = os.path.basename(frame.f_globals['__file__'])
    function = frame.f_code.co_name
    line = frame.f_lineno

    log_record = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d#%H:%M:%S.%f")[:-3],
        "level": level,
        "message": message,
        "logger": __name__,
        "module": module,
        "function": function,
        "line": line,
    }

    # Add extra information if present
    if logger:
        log_record.update({"logger": f"{logger}"})
    if extra:
        log_record.update({"x": f"{extra}"})

    return json.dumps(log_record)


class CustomLogger:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def log(self, level, message, logger=None, extra=None):
        if not logger:
            logger = self.name
        log_entry = format_log(level, message, logger, extra)

        if LOG_LEVELS[level] >= self.level:
            print(log_entry)

        if not os.path.exists("logs"):
            mkdir("logs")

        with open(file=f"./logs/{datetime.datetime.now().strftime('%Y-%m-%d')}.json", mode="a") as f:
            f.write(f"{log_entry}\n")

    def debug(self, message, logger=None, extra=None):
        self.log("DEBUG", message, logger, extra)

    def info(self, message, logger=None, extra=None):
        self.log("INFO", message, logger, extra)

    def warn(self, message, logger=None, extra=None):
        self.log("WARNING", message, logger, extra)

    def exception(self, message, logger=None, extra=None):
        self.log("EXCEPTION", message, logger, extra)

    def error(self, message, logger=None, extra=None):
        self.log("ERROR", message, logger, extra)

    def crit(self, message, logger=None, extra=None):
        self.log("CRITICAL", message, logger, extra)


def get_logger(name: str, level: int = 2):
    """``name:`` Name of the logger

    ``level:`` Level of the logger. Default ``2``

    "DEBUG": 0,

    "INFO": 1,

    "WARNING": 2,

    "EXCEPTION": 3,

    "ERROR": 4,

    "CRITICAL": 5,
    """
    return CustomLogger(name, level)
