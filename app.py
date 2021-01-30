from google.cloud import storage

import os
import sys

# validate arguments 
number_of_args = len(sys.argv)
print("Arguments: ", str(sys.argv))
if number_of_args != 2:
    raise Exception('Pass one module name. Number of arguments:', number_of_args, 'arguments.', str(sys.argv))

# create modules directory and load model into it
if not os.path.exists('modules'):
    os.makedirs('modules')
f = open("modules/__init__.py", "w")

bucket_name = "<bucket_name>" # your bucket name here
source_blob_name = str(sys.argv[1])+".py" # extracting the file name from command line
destination_file_name = "modules/model.py" # 

storage_client = storage.Client()

bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(source_blob_name)
blob.download_to_filename(destination_file_name)

from modules import model

# interface expects model.py to implement Model class with run method.
Model = model.Model()
Model.run()


