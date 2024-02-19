import boto3
from datetime import datetime, timedelta, timezone

def delete_old_objects(bucket_name, max_age_hours):
    # Initialize S3 client
    s3 = boto3.client('s3')

    # Get list of objects in the bucket
    response = s3.list_objects_v2(Bucket=bucket_name)
    
    # Current time
    current_time = datetime.now(timezone.utc)

    # Define the maximum age for objects in hours
    max_age = timedelta(hours=max_age_hours)

    # Iterate through objects and delete those older than max_age
    for obj in response.get('Contents', []):
        last_modified_time = obj.get('LastModified')
        if last_modified_time:
            last_modified_time = last_modified_time.replace(tzinfo=timezone.utc)
            age = current_time - last_modified_time
            if age > max_age:
                key = obj['Key']
                print(f"Deleting object: {key}")
                s3.delete_object(Bucket=bucket_name, Key=key)

if __name__ == "__main__":
    # Specify your S3 bucket name and maximum age for objects in hours
    bucket_name = "subhajits3bucket"
    max_age_hours = 1  # Change this value as needed

    delete_old_objects(bucket_name, max_age_hours)
