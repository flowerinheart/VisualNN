import uuid
from snakebite.client import Client

hdfs_client = Client("localhost", 9000, use_trash=False)

def creat_hdfs_dir(id):
    for res in client.mkdir(["/bdf/deeplearning/" + str(id)], True):
        print(res)

def get_id():
    return str(int(uuid.uuid1()))

