import requests
import json
from config import *
def loginAndGetProfile(event,context):
    """
        Calls LCS Endpoint to login, mainly used as middle main so we dont directly expose LCS API 
    """
    if "email" not in event or "password" not in event:
        return {"statusCode":400,"body":"Missing Password or Email"}
    else:
        #yeet data for authorize end point
        data_dict = {"email":event["email"], "password":event["password"]}
        resp = requests.post(BASE_URL + "/authorize",json=(data_dict))
        #grab the token and all read endpoint
        resp_parsed = resp.json()
        if resp_parsed["statusCode"] == 200:
            resp_body = json.loads(resp_parsed["body"])
            resp_json = resp_body["auth"]
            
            #make request to read endpoint
            profile_request_data_dict = {"email":resp_json["email"],"token":resp_json["token"], "query":{"email":resp_json["email"]}}
            profile = requests.post(BASE_URL + "/read",json=(profile_request_data_dict))
            #for some reason the query returns a json array?
            profile_json = profile.json()
            profile_body = profile_json["body"][0]
            #if they arent a director yeet them out
            if profile_body['role']['director'] == False:
                return {"statusCode":400,"body":"You are not a director, please contact a director for updates"}
            else:
                return {statusCode:200,"body":json.dumps({"email":resp_json["email"],"token":resp_json["token"]})}
        else:
            return {"statusCode":400,"body":"Invalid Username or Password"}

    
