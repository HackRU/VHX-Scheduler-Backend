import requests
import config
def callCompute(event,context):

    """
        Calls the compute all endpoint on LCS
    """
    #flat out call the reimburse endpoint
    data = requests.post(config.BASE_URL + "/reimburse")
    return data.json()
