import config
import requests

def sendMagicLink(event,context):
    """
        Allows Directors to send magic links to people with X permission
    """
    if 'email' not in event or 'token' not in event or 'emailsToSend' not in event or 'permissions' not in event:
        ret = {"statusCode":400, "body":"Invalid input"}
        return config.add_cors_headers(ret)
    #extract out the email, auth token and just forward to the lcs api
    auth_email = event['email']
    #build the lists to send the magic links
    emails_unparsed = event['emailsToSend']
    #parse out comma seperated list if any
    emails_parsed = emails_unparsed.split(",")
    permissions = event['permissions'].split(",")
    request_info = {
        "email":auth_email,
        "token":event['token'],
        "emailsTo":emails_parsed,
        "permissions":permissions
    }
    responseFromRequest = requests.post(config.BASE_URL + "/magiclink", json = (request_info))
    return responseFromRequest.json()

