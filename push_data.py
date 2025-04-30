import os
import sys
import json
from dotenv import load_dotenv
import pymongo.client_options
load_dotenv()

MONGO_DB_URL =  os.getenv("MONGO_DB_URL")


import certifi
ca = certifi.where()  ### Secure the Http connection. 


## Read the Dataset

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


class NetworkDataExtract():
    """This is ETL Pipeline which is responsible for extract data from database and transform it then load into other database"""

    def __init__(self):

        try:
            pass

        except Exception as e:
            raise NetworkSecurityException(e, sys)
        

    def csv_to_json(self, file_path):
        """This funtion converts the data from csv into json format"""

        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)
 
    def insert_data_into_mongodb(self, records, database, collection):
        """This function load json format data into the MongoDB Atlas."""

        try:
            self.database = database
            self.records = records
            self.collection = collection

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]

            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)

            return(len(self.records))

        except Exception as e:
            raise NetworkSecurityException(e, sys)
        

if __name__ == "__main__":
    FILE_PATH = "Network_Data\\PhisingData.csv"
    DATABASE = "PROJECTDB"
    Collection = "NetworkData"
    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json(FILE_PATH)
    print(records)
    no_of_records = networkobj.insert_data_into_mongodb(records, DATABASE, Collection)
    print(no_of_records)