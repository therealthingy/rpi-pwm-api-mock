'''
Operation handlers for endpoint `/app/logs`
    Local dev server URL: http://127.0.0.1:8080/api/v1/app/logs
'''
from connexion import NoContent

def search():
    '''
    Handler for GET /app/logs
    '''
    return NoContent                        # TODO
