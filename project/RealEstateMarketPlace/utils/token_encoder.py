import jwt


def encode_reset_token(email):
    # this may throw an exception if file doesn't exist
    key = read_key_from_file()

    try:
        payload = {
            'em': email,
            'reset': 1
        }
        return jwt.encode(payload,
                          key,
                          algorithm='HS256'
                          )
    except Exception as e:
        return e


def read_key_from_file():
    f = open('/var/www/server.conf', 'r')
    key = f.readline()
    f.close()
    return key
