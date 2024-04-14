import logging

from pymongo import MongoClient

URL = "mongodb://localhost:27017/"
DB_NAME = "recipes"
COLLECTION_NAME = "recipes"


class MongoConnector:
    """TODO"""

    def __init__(
        self, 
        url: str = None, 
        db_name: str = None, 
        collection_name: str = None
    ) -> None:
        """TODO"""

        if not url:
            url = URL
        client = MongoClient(url, username="serviceuser", password="your_mongodb_password")

        if not db_name:
            db_name = DB_NAME
        database = client[db_name]

        if not collection_name:
            collection_name = COLLECTION_NAME
        
        self.collection = database[collection_name]

    def create_record(self, doc: dict) -> str:
        """TODO"""

        result = self.collection.insert_one(doc)
        return result.inserted_id

    def read_records(self, filter: dict = None) -> list:
        """TODO"""

        formatted_records =[]
        records = self.collection.find(filter)
        for record in records:
            record.pop('_id')
            formatted_records.append(record)
        return formatted_records

    def read_record_by_id(self, record_id: str) -> dict:
        """TODO"""

        record = self.collection.find_one({"_id": record_id})
        return record.pop('_id')

    def update_record(self, doc_id: str, update_data: dict) -> str:
        """TODO"""

        record = self.collection.update_one({"_id": doc_id}, {"$set": update_data})

        return record.modified_count

    def delete_record(self, doc_id: str) -> str:
        """TODO"""

        result = self.collection.delete_one({"_id": doc_id})

        return result.deleted_count
