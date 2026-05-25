import json
import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):

    print(json.dumps(event))

    try:
        group_id = event['detail']['requestParameters']['groupId']

        response = ec2.describe_security_groups(
            GroupIds=[group_id]
        )

        for sg in response['SecurityGroups']:

            for permission in sg['IpPermissions']:

                # IPv4 validation
                for ip_range in permission.get('IpRanges', []):

                    if ip_range.get('CidrIp') == '0.0.0.0/0':

                        ec2.revoke_security_group_ingress(
                            GroupId=group_id,
                            IpPermissions=[permission]
                        )

                        print("Removed IPv4 open rule")

                # IPv6 validation
                for ipv6_range in permission.get('Ipv6Ranges', []):

                    if ipv6_range.get('CidrIpv6') == '::/0':

                        ec2.revoke_security_group_ingress(
                            GroupId=group_id,
                            IpPermissions=[permission]
                        )

                        print("Removed IPv6 open rule")

        return {
            'statusCode': 200,
            'body': 'Compliance check completed'
        }

    except Exception as e:
        print(str(e))
        raise e
