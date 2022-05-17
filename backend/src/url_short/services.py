import shortuuid

def get_short_url() -> str:
    return shortuuid.uuid()[:15]
