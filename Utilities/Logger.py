import sys
import logging.handlers
from colorama import Fore, Style
from logging.handlers import RotatingFileHandler
import os.path
import datetime
from pathlib import Path
import inspect

'''
@Author-Manas Ranjan Mohanty
Logger set up configuration
Logging contains
Log level,
Logging time,current thread accessing function,
Logger Name,log message
mode type set to W to override existing logs and 'a' for append log to existing log
f-handler for logging to Log file and handler for console Log
It will keep only 3 copy of log file
'''

global log_path
global oneui2_dir
now = datetime.datetime.today()
nTime = now.strftime('%d-%m-%Y-%H-%M-%S')
homepath = os.getcwd().split("testCases")
homepath = homepath[0] + "reports"
oneui2_dir = homepath
Path(homepath + "/logs").mkdir(parents=True, exist_ok=True)
log_path = homepath + "/logs/log_" + nTime
Path(log_path).mkdir(parents=True, exist_ok=True)
logger = logging.getLogger('DDNI_Automation')
logger.setLevel(logging.DEBUG)
log_file = log_path + r"\TestExecution.log"
f_handler = RotatingFileHandler(log_file, mode='a', maxBytes=5 * 1024 * 1024,
                                backupCount=3, encoding="utf-8", delay=0)
f_handler = logging.FileHandler(filename=log_file, encoding="utf-8", mode="a")
handler = logging.StreamHandler(sys.stdout)
log_format = "%(asctime)s.%(msecs)03d  %(levelname)-06s: %(message)s"
log_datefmt = "%Y-%m-%d %H:%M:%S"
log_formatter = logging.Formatter(log_format, datefmt=log_datefmt)
handler.setFormatter(log_formatter)
f_handler.setFormatter(log_formatter)
logger.addHandler(handler)
logger.addHandler(f_handler)

LOG_LVL_CMD = 60
LOG_LVL_RC = 61
LOG_LVL_STDERR = 62
LOG_LVL_STDOUT = 63

logging.addLevelName(LOG_LVL_CMD, "CMD")
logging.addLevelName(LOG_LVL_RC, "RC")
logging.addLevelName(LOG_LVL_STDERR, "STDERR")
logging.addLevelName(LOG_LVL_STDOUT, "STDOUT")


def debug(msg, classname=None, methodname=None):
    message = ""
    if classname:
        message = message + classname + " -> "
    if methodname:
        message = message + methodname + " -> "
    message = message + msg
    message = "{}::{}::{}: {}".format(*get_call_info(), message)
    logger.debug(message)


def get_call_info():
    stack = inspect.stack()
    # stack[1] gives previous function ('info' in our case)
    # stack[2] gives before previous function and so on
    module = stack[2][1].split("\\")[-1].split('.')[0]
    lineno = stack[2][2]
    funcName = stack[2][3]
    return module, funcName, lineno


def get_cmd_call_info():
    stack = inspect.stack()
    # stack[4] gives info of methods which call cmd execute method
    module = stack[4][1].split("\\")[-1].split('.')[0]
    lineno = stack[4][2]
    funcName = stack[4][3]
    return module, funcName, lineno


def info(msg):
    msg = "{}::{}::{}: {}".format(*get_call_info(), msg)
    logger.info(msg)


def error(msg):
    msg = "{}::{}::{}: {}".format(*get_call_info(), msg)
    logger.error(msg)


def warn(msg):
    msg = "{}::{}::{}: {}".format(*get_call_info(), msg)
    logger.warning(msg)


def _print(msg):
    msg = "{}::{}::{}: {}".format(*get_call_info(), msg)
    logger.debug(msg)


def cmd(msg):
    msg = "{}::{}::{}: CMD: {}".format(*get_cmd_call_info(), msg)
    logger.log(LOG_LVL_CMD, msg)


def stdout(msg):
    msg = "{}::{}::{}: STDOUT: {}".format(*get_cmd_call_info(), msg)
    logger.log(LOG_LVL_STDOUT, msg)


def stderr(msg):
    msg = "{}::{}::{}: STDERR: {}".format(*get_cmd_call_info(), msg)
    logger.log(LOG_LVL_STDERR, msg)


def set_level(level):
    """
    :param level: logging.DEBUG, logging.INFO, logging.WARN, logging.ERROR
    :return:
    """
    logger.setLevel(level)


def set_level_to_debug():
    logger.setLevel(logging.DEBUG)


def set_level_to_info():
    logger.setLevel(logging.INFO)


def set_level_to_warn():
    logger.setLevel(logging.WARN)


def set_level_to_error():
    logger.setLevel(logging.ERROR)
