import boto3
import json


def get_ec2_client(region):
    return boto3.client(
    'ec2',region_name=region,
    aws_access_key_id='AKIAZMO222HBGCPYBRB4',
    aws_secret_access_key='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',
    )

def get_complete_metadata(region):
    ec2_client = get_ec2_client(region)
    try:
        return ec2_client.describe_instances()
    except Exception as err:
        print(f"Exception occured while fetching complete information {err}")
   
def get_complete_metadata_for_an_instance_id(instance_id):
    ec2_data = get_complete_metadata()
    for each in ec2_data.describe_instances()['Reservations']:  
        for each_instance in each['Instances']: 
            if each_instance['InstanceId'] == instance_id:
                return each_instance
    print(f"Instance id {instance_id} not found in ec2 metadata {ec2_data}")

def get_metadata_field_for_an_instance_id(instance_id, key_to_be_retrieved):
    instance_metadata = get_complete_metadata_for_an_instance_id(instance_id)
    if key_to_be_retrieved in instance_metadata.keys():
        return instance_metadata[key_to_be_retrieved]
    else:
        print("Key {key_to_be_retrieved} not present in Instance metadata {instance_metadata}")

def single_function(region, instance_id = None, key_to_be_retrieved=None):
    ec2_client = get_ec2_client(region)
    if instance_id is None or len(instance_id) == 0:
        return ec2_client.describe_instances()
    ec2_instance_data = ec2_client.describe_instances(InstanceIds=[instance_id])
    if key_to_be_retrieved is None:
        return ec2_instance_data
    if key_to_be_retrieved in ec2_instance_data.keys():
        return ec2_instance_data[key_to_be_retrieved]
    print("Key {key_to_be_retrieved} not present in Instance metadata {instance_metadata} with in ec2_metaData {ec2_instance_data} ")



def lambda_handler(event, context):
    #define region of the deployed ec2 instance
    region='ap-northeast-1'

    # Get complete metadata as json
    print(get_complete_metadata(region))

    # Get data for an instance 
    instance_id = "Put you instanceID Here"
    print(get_complete_metadata_for_an_instance_id(instance_id))

    # Get particular field for an instance 
    key_to_be_retrieved = "Key to be retrieved"
    print(get_metadata_field_for_an_instance_id(instance_id, key_to_be_retrieved))


    #Single function to support all 3 use-cases
    print(single_function(region))
    print(single_function(region, instance_id))
    print(single_function(region, instance_id, key_to_be_retrieved))
