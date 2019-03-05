import requests
import config
def callCompute(event,context):

    """
        Calls the compute all endpoint on LCS
    """
    
    #flat out call the reimburse endpoint
    req_data = {
            "email":event["email"],
            "token":event["token"]
    }
    data = requests.post(config.BASE_URL + "/reimburse",json = (req_data))

    return (data.json())


