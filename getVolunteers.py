import requests
import config
def getVolunteers(event,context):

    """
        Gets list of volunteers
    """

    profile_request_data_dict = {"email":event["email"],"token":event["token"], "query":{"role.volunteer":True}}
    dat = requests.post(config.BASE_URL + "/read", json = (profile_request_data_dict))
    return data.json()
