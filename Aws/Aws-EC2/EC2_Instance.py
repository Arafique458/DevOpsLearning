# The purpose of this script is to automate the creation of ec2 instance.

#we must import the boto3
import boto3

# aws_iam_console is a variable (It can be anything you desire).
# boto3 is SDK for which amazon uses
# profile name is what we defined in the Terminal when we did "AWS Configure". We entered the Access ID, Secret Key, region and nothing for the formate or enter json. 
aws_iam_console = boto3.session.Session(profile_name='default')

#ec2_instance is also a variable, it can be anything for this demo we chose ec2_instance
#aws_iam_console.client is define a sevice we need to access though cli. For this demo we are using ec2
ec2_instance = aws_iam_console.client('ec2')

# This part tells instance what to do
reponse = ec2_instance.run_instances(
#
#ImageID can be found in the AWS console. For the demo we are using ubuntu 20 AMI.
    ImageId='ami-0778521d914d23bc1',
#
#InstacneType we are using is 't2.micro' because we are using Free Tier for this demo
    InstanceType='t2.micro',
#MaxCount and MinCount is for the amount of instance we want AWS to create for us.
    MaxCount=1,
    MinCount=1

)