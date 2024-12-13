import boto3
import sys

if len(sys.argv) < 4:
    print("Usage: python3 ins-new.py <region> <accesskey> <secretkey>")
    sys.exit(1)

region = sys.argv[1]
accesskey = sys.argv[2]
secretkey = sys.argv[3]

try:
    client = boto3.client(
        'ec2',
        region_name=region,
        aws_access_key_id=accesskey,
        aws_secret_access_key=secretkey
    )

    data1 = client.describe_instances()

    for reservation in data1.get("Reservations", []):
        for instance in reservation.get("Instances", []):
            print(f"Instance ID: {instance.get('InstanceId')}")
            print(f"State: {instance.get('State', {}).get('Name')}")
            print(f"Public DNS: {instance.get('PublicDnsName')}")
            print(f"Private IP: {instance.get('PrivateIpAddress')}")
            print("-" * 40)

except Exception as e:
    print(f"Error: {e}")
