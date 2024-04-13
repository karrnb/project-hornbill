import logging

from libs.mongodb.client import MongoConnector


class RecipeHandler:
    """TODO"""

    def __init__(self):
        """TODO"""

        self.mongo_connector = MongoConnector()

    def get_all_recipes(self) -> dict:
        """TODO"""

        results = self.mongo_connector.read_records()

        return {"results": results, "statusCode": 200}

    def get_recipe(self, filter) -> dict:
        """TODO"""

        result = self.mongo_connector.read_records(filter)

        return {"result": result}

    def create_recipe(self, record: dict) -> dict:
        """TODO"""

        result = self.mongo_connector.create_record(record)

        return {"result_id": result, "statusCode": 200}

    def update_recipe(self, record: dict) -> dict:
        """TODO"""

        if '_id' in record:
            record_id = record['_id']
            
        elif 'recipe_id' in record:
            record = self.mongo_connector.read_records({"recipe_id": record.get('recipe_id')})
            record_id = record.get('_id')
        
        else:
            record_id = None
            
        if record_id:
            result = self.mongo_connector.update_record(
                                                doc_id=record_id, 
                                                update_data=record
                                            )
        else:
            logging.error(f"Could not find a match for {record} to update, "
                           "as it does not contain _id or recipe_id")
            raise

        return {"updated_count": result, "statusCode": 200}

    def delete_recipe(self, record_id: str) -> dict:
        """TODO"""

        result = self.mongo_connector.delete_record(record_id)

        return {"deleted_count": result, "statusCode": 200}
