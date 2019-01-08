import config
import requests

def promoteRole(event,context):
    """
        Makes request to update endpoint to promote a user to a certain role
    """
    #given an email and a role promote the user to that role
    if 'role' not in event or 'email' not in event or 'auth' not in event:
        ret = {"statusCode":400,"body":"missing email , auth or role"}
        return config.add_cors_headers(ret)
    #check if non emprt string
    if len(event['role'] > 1):
        ret = {"statusCode":400,"body":"Invalid role"}
        return config.add_cors_headers(ret)
    updates = {"$set":{"role."+event['role']:True}}
    request_data = {
        "email":event["email"],
        "auth":event["auth"],
        "updates":updates
    }
    ret = requests.post(config.BASE_URL +'/update', json = (request_data))
    return add_cors_headers(ret.json())


