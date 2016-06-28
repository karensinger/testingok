import boto.sns
from boto.sns import connect_to_region


def publishsns(aws_access_key, aws_secret_access_key, region, topicArn, msg, subject):
    c = connect_to_region(region, aws_access_key_id = AWS_ACCESS_KEY, aws_secret_access_key = AWS_SECRET_ACCESS_KEY)
        c.publish(message = msg,subject = subject, target_arn = topicArn)
    return;
