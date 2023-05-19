def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    response = ec2.stop_instances(InstanceIds=['i-*ID-GOES-HERE*'])  
    return response
