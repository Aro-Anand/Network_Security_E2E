import os
import sys
import json

from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
# print(MONGO_DB_URL)


import certifi # That provides set root certificates and secure http connection
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo

from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException


class NetworkDataExtract():
    def __init__(self):

        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def cv_to_json_converter(self, file_path):
        try:
            data = pd.read_csv(file_path)
            # data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records

        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def insert_data_mongodb(self, database, collection, records):   #[Tables -> Collection, Values-> Document(key-value pair)]
        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)   # Connect to MongoDB
            self.database = self.mongo_client[self.database]        # Connect to Database
            self.collection = self.database[self.collection]        # Connect to (Table)Collection[list of jsons[{},{},{}]]
            self.collection.insert_many(self.records)               # This line insert the values to json format [{"A"":1"}, {"B"":2"}]

            return (len(self.records))
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        

if __name__ == "__main__":
    FILE_PATH = "Network_Data\\PhisingData.csv"
    DATABASE = "Anand_updated_database"
    Collection = "NetworkDATA"  ##It's similar to table name
    network_obj = NetworkDataExtract()
    records = network_obj.cv_to_json_converter(file_path=FILE_PATH)
    no_of_records = network_obj.insert_data_mongodb(DATABASE, Collection, records)

    print(no_of_records)