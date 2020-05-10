# coding: utf-8
import os

import boto3

AWS_ACCESS_KEY_ID = 'AKIASA35FZ4JOMKMPF7Z'
AWS_SECRET_ACCESS_KEY = '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'
BUCKET_NAME = 'we-post'
REGION_NAME = 'ap-southeast-1'
PHOTO_FOLDER = 'media'

BASE_DIR = os.getcwd()
MEDIA_DIR = os.path.join(BASE_DIR, 'media')


def getS3():
    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=REGION_NAME
    )
    s3 = session.resource('s3')
    return s3


def upload_fiel(key):
    bucket = getS3().Bucket(name=BUCKET_NAME)
    file1 = os.path.join(MEDIA_DIR, key)
    bucket.upload_file(file1, 'media/' + key)


file1 = os.path.join(MEDIA_DIR, '1.txt')

with open(file1, 'rb') as  data:
    bucket = getS3().Bucket(name=BUCKET_NAME)
    bucket.put_object(
        ACL='private',
        Body=data,
        Key='1-acl.txt'
    )
# upload_fiel('avatar/2020/05/04/timg.jpg')
