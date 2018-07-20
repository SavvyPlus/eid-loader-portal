import boto3


s3 = boto3.client('s3')


def put_file(bucket, key, body):
    """Upload file to a bucket.
    Args:
        bucket (string): bucket name.
        key (string): key in bucket.
        body (byte): file content in byte type.
    Returns:
        no return
    """
    print("Put file [%s] to [%s]" % (key, bucket))
    return s3.put_object(Bucket=bucket, Key=key, Body=body)


def get_folder_listing(bucket, prefix, delimiter="/"):
    """Get list of folders on a bucket with prefix
    Args:
        bucket (string): bucket name
        key (string): prefix of keys
    Returns:
        list of string
    """
    folders = []
    try:
        result = s3.list_objects(Bucket=bucket, Prefix=prefix, Delimiter=delimiter)
        for o in result.get('CommonPrefixes'):
            folders.append(o.get('Prefix'))
    except:
        pass
    return folders
