# The purpose of this script is to automate the stop process and termination of ec2 instance.

#we must import the boto3
import boto3

# aws_iam_console is a variable (It can be anything you desire).
# boto3 is SDK for which amazon uses
# profile name is what we defined in the Terminal when we did "AWS Configure". We entered the Access ID, Secret Key, region and nothing for the formate or enter json
aws_iam_console = boto3.session.Session(profile_name='default')

#ec2_instance is also a variable, it can be anything for this demo we chose ec2_instance
#aws_iam_console.client is define a sevice we need to access though cli. For this demo we are using ec2
ec2_instance = aws_iam_console.client(service_name='ec2')

# This part tells instance what to do
# If instance needs to be Change Stop_Instances.
reponse = ec2_instance.stop_instances(
#
# If you want to start the instances
#response = ec2_instance.start_instances
#
#If you want to terminate the instance
#response = ec2_instance.terminate_instances


# EC2 instance id or Ids go here if there are more than one.
    InstanceIds=[]
)
