#!/usr/bin/env python3


# import app


from time import sleep
from app.envflags import api_enabled


if __name__ == '__main__':

    # - API -
    if api_enabled:
        import core.backend as backend
        backend.launch_as_new_thread()


    # - PWM (controls fan) -
    while True:
        print("I'm scheduling API")
        sleep(3)