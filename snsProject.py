import boto3

"""
class boto3.session.Session(aws_access_key_id=None, aws_secret_access_key=None, aws_session_token=None, region_name=None, botocore_session=None, profile_name=None)[source]
A session stores configuration state and allows you to create service clients and resources.
"""

client = boto3.client(
        "sns",
        aws_access_key_id="xxxxx",
        aws_secret_access_key="xxxxx",
        region_name="us-east-1")



response = client.create_topic(Name="topic_name")
topic_arn = response["TopicArn"]

#response = client.subscribe(TopicArn=topic_arn, Protocol="Email", Endpoint="example@wcsu.edu")
#subscription_arn = response["SubscriptionArn"]


jFile = open("jokeOfTheHour.txt", "r")
msg = str(jFile.read())
jFile.close()

# Publish to topic
client.publish(TopicArn=topic_arn,
            Message= msg,
            Subject="Joke of the hour")
