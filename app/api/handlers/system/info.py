'''
Operation handlers for endpoint `/system/info`
    Local dev server URL: http://127.0.0.1:8080/api/v1/app/system/info
'''
from connexion import NoContent

def search():
    '''
    Handler for GET /system/info
    '''
    return NoContent                        # TODO
