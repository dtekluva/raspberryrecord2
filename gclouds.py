
import os
from google.cloud import storage

"""Credentials and keys already created in google cloud console"""

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/pi/Desktop/app/raspberryrecorder.json'
storage_client = storage.Client()

"""Creates a new Bucket in Google cloud"""

# dir(storage_client)
bucket_name = 'new_data_bucket'
# bucket = storage_client.bucket(bucket_name)
# bucket.location = 'US'
# bucket = storage_client.create_bucket(bucket)
# vars(bucket) #gets bucket info

"""Accessing bucket"""
my_bucket = storage_client.get_bucket(bucket_name)


"""Upload files to bucket"""
def upload_to_bucket(blob_name, file_path,  bucket_name = bucket_name):

    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True
    except Exception as e:
        print(e)
        return False

if '__name__' == '__main__':
    file_path = r'C:\Users\ariel\OneDrive\Documents\500L\project\raspberryrecorder'
    # file_name = 'Recording.m4a'
    upload_to_bucket('voice', os.path.join(file_path, r'C:\Users\ariel\OneDrive\Documents\500L\project\raspberryrecorder\Recording.m4a'), 'new_data_bucket')
