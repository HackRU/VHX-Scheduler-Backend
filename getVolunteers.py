import requests
import config
import boto3
def getVolunteers(event,context):

    """
        Gets list of volunteers
    """

    profile_request_data_dict = {"email":event["email"],"token":event["token"], "query":{"role.volunteer":True}}
    dat = requests.post(config.BASE_URL + "/read", json = (profile_request_data_dict))
    response = dat.json()
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    tableToCheck = dynamodb.Table('VolunteerActions')
    if response.statusCode == 200:
        for i in range(len(response.body()))
            resp = table.query(
                KeyConditionExpression=Key('email').eq(resp.body[i]['email'])
            )
            if resp:
                response[i]['current_action'] = resp['current_action']
    return response
