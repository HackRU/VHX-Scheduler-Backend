import config
import requests

def promoteRole(event,context):
    """
        Makes request to update endpoint to promote a user to a certain role
    """
    #given an email and a role promote the user to that role
    if 'role' not in event or 'auth_email' not in event or 'auth' not in event or 'user_email' not in event or 'roleValue' not in event:
        ret = {"statusCode":400,"body":"missing email , auth or role"}
        return config.add_cors_headers(ret)
    #check if non emprt string
    if(type(event['roleValue']) != bool):
        ret = {"statusCode":400,"body":"Inavalid value for role"}
        return config.add_cors_headers(ret)
    if len(event['role']) < 1:
        ret = {"statusCode":400,"body":"Invalid role"}
        return config.add_cors_headers(ret)
    updates = {"$set":{"role."+event['role']:event['roleValue']}}
    request_data = {
        "auth_email":event["auth_email"],
        "user_email":event["user_email"],
        "auth":event["auth"],
        "updates":updates
    }
    ret = requests.post(config.BASE_URL +'/update', json = (request_data))
    return config.add_cors_headers(ret.json())


