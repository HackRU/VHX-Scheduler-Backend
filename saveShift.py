import boto3
import config
def saveShift(event,context):
    """
        Saves a shift for a voluneer
    """
    dynamodb = boto3.resource('dynamodb',region_name='us-east-1') 
    table = dynamodb.Table('VolunteerActions')
    table.update_item(
            Key={
                    "email":event["user_email"]
                },
            UpdateExpression="SET shifts = list_append(if_not_exists(shifts, :empty_list), :s)",
            ExpressionAttributeValues={
                ":s":  [event["event"]],
                ":empty_list":[]
                }
            )
    return config.add_cors_headers({"statusCode":200,"body":"saved"})
