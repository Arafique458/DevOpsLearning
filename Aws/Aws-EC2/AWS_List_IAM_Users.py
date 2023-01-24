# The purpose of this script is to automate the process of showing list of users in IAM console.
#we must import the boto3
import boto3

# aws_console is a variable (It can be anything you desire).
# boto3 is SDK for which amazon uses
# profile name is what we defined in the Terminal when we did "AWS Configure". We entered the Access ID, Secret Key, region and nothing for the formate or enter json
aws_console = boto3.session.Session(profile_name="default")

#iam_management_console is also a variable, it can be anything for this demo we chose iam_management_console
#aws_iam_console.client is define a sevice we need to access though cli. For this demo we are using iam
iam_management_console = aws_console.resource('iam')

# we used for loop here to find out the users we have in our aws IAM.
for each_user_objects in iam_management_console.users.all():
    print(each_user_objects.name)
