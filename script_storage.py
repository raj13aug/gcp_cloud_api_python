from google.cloud import storage

# This  module allows you to interact with the system-specific parameters and functions
import sys

# assigning the value of the first command-line argument to the variable 
key = sys.argv[1]

# Initialize a client
storage_client = storage.Client.from_service_account_json(key)

def createBucket():
    
    bucket_name = 'bucket-create-with-python'
    region = 'us-central1'

    # Create the bucket with the specified name and region
    bucket = storage_client.create_bucket(bucket_name, location=region)

    print(f'Bucket {bucket.name} created in {region}.')

def listAllBuckets():

    # Lista Cloud Storage Buckets
    buckets = list(storage_client.list_buckets())
    print(buckets)

def delete_all_buckets():
    buckets = list(storage_client.list_buckets())

    for bucket in buckets:
        print(f"Deleting bucket {bucket.name}")
        bucket.delete(force=True)

    print("All buckets deleted")

# Call the functions
createBucket()
listAllBuckets
#https://medium.com/@ozieldesouza/automation-using-python-on-google-cloud-iam-service-accounts-a1fc5ebd3ee7