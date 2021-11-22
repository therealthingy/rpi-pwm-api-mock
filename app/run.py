#!/usr/bin/env python3


# import app


if __name__ == '__main__':
    import app.web.backend as backend
    api = backend.new_runnable_backend()
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