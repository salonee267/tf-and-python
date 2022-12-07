import boto3
import json


def instance_metadata(region):
    ec2 = boto3.client(
    'ec2',region_name=region,
    aws_access_key_id='AKIAZMO222HBGCPYBRB4',
    aws_secret_access_key='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',
    )

    try:
        ec2_data = ec2.describe_instances(
        # FOR SINGLE EC2 Instance
        InstanceIds=['i-0649b6ab402da21e6'],

        # #FOR MULTIPLE EC2 Instances
        # InstanceIds=['id1','id2','id3'],
        DryRun=False,
        )

        print(ec2_data)

        #FOR SINGLE EC2INSTANCE

        # instance_type=ec2_data['Reservations'][0]['Instances'][0]['InstanceType']
        # instance_dns=ec2_data['Reservations'][0]['Instances'][0]['PrivateDnsName']
        # print("\n\n",instance_type,instance_dns )

        # # IF YOU HAVE MULTIPLE EC2 instances

        # for i in range(0,len(ec2_data['Reservations'])):
        #     instance_type=ec2_data['Reservations'][i]['Instances'][0]['InstanceType']
        #     instance_dns=ec2_data['Reservations'][i]['Instances'][0]['PrivateDnsName']
        #     print("\n\n",instance_type,instance_dns )

    except Exception as err:
        print(err)
   

def lambda_handler(event, context):
    #define region of the deployed ec2 instance
    region='ap-northeast-1'
    instance_metadata(region)
