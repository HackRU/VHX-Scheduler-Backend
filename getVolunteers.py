import requests
import config
import boto3
from boto3.dynamodb.conditions import Key, Attr
def getVolunteers(event,context):

    """
        Gets list of volunteers
    """

    profile_request_data_dict = {"email":event["email"],"token":event["token"], "query":{"role.volunteer":True}}
    dat = requests.post(config.BASE_URL + "/read", json = (profile_request_data_dict))
    response = dat.json()
    #now we join with out specifc data and get all the volunteers shifts and current actions
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    tableToCheck = dynamodb.Table('VolunteerActions')
    if response['statusCode'] == 200:
        for i in range(len(response['body'])):
            resp = tableToCheck.query(
                KeyConditionExpression=Key('email').eq(response['body'][i]['email'])
            )
            if len(resp['Items']) > 0:
                #only one item per email so get 0th element
                if('current_action' in resp['Items'][0]):
                    response['body'][i]['current_action'] = resp['Items'][0]['current_action']
                #set shifts
                if ('shift' in resp['Items'][0]:
                    response['body'][i]['shift'] = resp['Items'][0]['shift']
                
    return response

def insertVolunteerAction(event,context):
    """
        Inserts a current volunteer action into the DB
    """
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    tableToCheck = dynamodb.Table('VolunteerActions')
    tableToCheck.update_item(
        Key={
            'email': event['user_email']
        },
        UpdateExpression="set current_action = :val",
        ExpressionAttributeValues={
            ':val': event['current_action']
         }
    ) 
    #save the data after they type
    return config.add_cors_headers({'statusCode':200,"body":"saved"})

