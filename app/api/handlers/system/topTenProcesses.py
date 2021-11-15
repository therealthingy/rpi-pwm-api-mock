'''
Operation handlers for endpoint `/system/topTenProcesses`
    Local dev server URL: http://127.0.0.1:8080/api/v1/app/system/topTenProcesses
'''
from connexion import NoContent

def search():
    '''
    Handler for GET /system/topTenProcesses
    '''
    return NoContent                        # TODO
