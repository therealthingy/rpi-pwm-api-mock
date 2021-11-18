#!/usr/bin/env python3


# import app


from time import sleep
from app.envflags import api_enabled


if __name__ == '__main__':
    import core.backend as backend
    api = backend.new_launchable_backend()
    api()

    # TODO
    # # - API -
    # if api_enabled:
    #     import core.backend as backend
    #     backend.launch_as_new_thread()
    #
    #
    # # - PWM (controls fan) -
    # while True:
    #     print("I'm scheduling API")
    #     sleep(3)