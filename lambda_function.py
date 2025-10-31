import boto3
import csv
import io

def lambda_handler(event, context):
    s3 = boto3.client('s3', endpoint_url='http://localhost:4566')
    source_bucket = 'raw-data-bucket'
    target_bucket = 'processed-data-bucket'

    for record in event['Records']:
        key = record['s3']['object']['key']
        obj = s3.get_object(Bucket=source_bucket, Key=key)
        data = obj['Body'].read().decode('utf-8')

        lines = list(csv.reader(io.StringIO(data)))
        unique = [list(x) for x in {tuple(row) for row in lines}]

        out_csv = io.StringIO()
        csv.writer(out_csv).writerows(unique)
        s3.put_object(Bucket=target_bucket, Key=f'processed-{key}', Body=out_csv.getvalue())

    return {'status': 'success'}
