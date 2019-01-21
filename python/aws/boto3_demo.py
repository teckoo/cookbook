"""
Code snippets for aws client boto3 package
"""

import boto3


def s3_copy_buckets():
    """ copy objects between two buckets """
    s3 = boto3.resource('s3')
    copy_source = {
        'Bucket': 'mybucket',
        'Key': 'mykey'
        }
    bucket = s3.Bucket('otherbucket')
    bucket.copy(copy_source, 'otherkey')

    # or
    # notice destination bucket parameters
    s3 = boto3.resource('s3')
    copy_source = {
        'Bucket': 'mybucket',
        'Key': 'mykey'
    }
    s3.meta.client.copy(copy_source, 'otherbucket', 'otherkey')

