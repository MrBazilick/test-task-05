import boto3
import os

def lambda_handler(event, context):
    # Create an S3 client
    s3 = boto3.client('s3')

    # Specify the bucket name
    bucket_name = os.environ.get('test-s3-bucket-03')

    # Get the list of all files in the specified S3 bucket
    response = s3.list_objects_v2(Bucket=bucket_name)

    # Extract file information from the response
    files = [item['Key'] for item in response.get('Contents', [])]

    # Print or process the list of files as needed
    print("List of files in the bucket:")
    for file in files:
        print(file)
        
    # Read the first file if the bucket is not empty
    if files:
        first_file_key = files[0]
        first_file_obj = s3.get_object(Bucket=bucket_name, Key=first_file_key)
        first_file_content = first_file_obj['Body'].read().decode('utf-8')

        print(f"Contents of the first file ({first_file_key}):")
        print(first_file_content)

        return {
            'statusCode': 200,
            'body': {
                'files': files,
                'first_file': first_file_key,
                'first_file_content': first_file_content
            }
        }
    else:
        return {
            'statusCode': 200,
            'body': {
                'message': "The bucket is empty."
            }
        }