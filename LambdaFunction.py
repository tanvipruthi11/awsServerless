import json

def lambda_handler(event, context):
    input_message= event["message"]
    input_email = event["email"]
    if input_email == 'rhawkey@dal.ca':
        output_tier = 3
    elif "account" in input_message or "password" in input_message:
        output_tier = 1
    elif "computer" in input_message or "laptop" in input_message or "printer" in input_message:
        output_tier = 2
    else:
        output_tier = 0

    return {
        'statusCode': 200,
        'tier': output_tier,
        'email': input_email,
        'message': input_message 
    }
