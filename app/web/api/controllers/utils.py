import hashlib


def calc_etag(db_entity):
    return hashlib.sha1(repr(db_entity).encode()).hexdigest()