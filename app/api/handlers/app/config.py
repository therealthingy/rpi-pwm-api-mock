'''
Operation handlers for endpoint `/app/config`
    Local dev server URL: http://127.0.0.1:8080/api/v1/app/config
'''


from connexion import NoContent



def search(self):
    '''
    Handler for GET /app/config
    '''
    return NoContent



