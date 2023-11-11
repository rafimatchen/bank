import pyotp

import config_loader

config = config_loader.get_config()

totp = pyotp.TOTP(config["otp_secret"])


def get_one_time_password() -> str:
    return totp.now()


def get_one_time_password_from_input() -> str:
    return input("Enter password\n>>>")
