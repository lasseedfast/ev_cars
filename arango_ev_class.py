from arango import ArangoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv() # Install with pip install python-dotenv


class ArangoDB:
    def __init__(self):
        """
        Initializes an instance of the ArangoEVClass.

        Args:
            db_name (str): The name of the database.
            username (str): The username for authentication.
            password (str): The password for authentication.
        """
        password = os.getenv("PASSWORD_ARANGO")
        self.client = ArangoClient(hosts='https://arango.lasseedfast.se')
        self.db = self.client.db('ev_dataharvest', username='dataharvest', password=password)


    def all_ev_speeches(self):
            """
            Retrieves all speeches from the 'ev_speeches' collection.

            Returns:
                A list of all speeches in the 'ev_speeches' collection.
            """
            return list(self.db.collection('ev_speeches').all())

    def update_ev_document(self, document):
        """
        Updates an EV document in the 'ev_speeches' collection.

        Args:
            document: The document to be updated.

        Returns:
            None
        """
        self.db.collection('ev_speeches').update(document, merge=False)

    def get_document_by_id(self, document_id):
            """
            Retrieves a document from the 'ev_speeches' collection by its ID.

            Args:
                document_id (str): The ID of the document to retrieve.

            Returns:
                dict: The retrieved document.

            """
            if '/' in document_id:
                document_id = document_id.split('/')[-1]
            return self.db.collection('ev_speeches').get(document_id)
