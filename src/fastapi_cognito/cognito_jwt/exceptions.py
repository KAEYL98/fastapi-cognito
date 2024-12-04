class CognitoJWTException(Exception):
    pass

class ExpiredJWTException(CognitoJWTException):
    pass