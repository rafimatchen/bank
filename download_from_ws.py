import json

from wsimple.api import Wsimple

import config
from one_time_password import get_one_time_password

config = config.get_config()

ws = Wsimple(
    config["ws_login"],
    config["ws_password"],
    otp_callback=get_one_time_password,
)

if ws.is_operational():
    print(json.dumps(ws.get_positions(), indent=2))
