from checkio_referee import RefereeRank, ENV_NAME, covercodes



import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "say_hi"
    FUNCTION_NAMES = {
        "python_3": "say_hi",
        "js_node": "sayHi"
    }
    ENV_COVERCODE = {
        ENV_NAME.PYTHON: covercodes.py_unwrap_args,
        ENV_NAME.JS_NODE: covercodes.js_unwrap_args
    }