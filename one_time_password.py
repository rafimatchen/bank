import pyotp

import config

config = config.get_config()

totp = pyotp.TOTP(config["otp_secret"])


def get_one_time_password() -> str:
    return totp.now()
