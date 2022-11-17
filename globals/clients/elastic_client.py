from elasticsearch import Elasticsearch

from saison_omni.settings import ELASTIC_CONN

"""
Creating Elastic Client
"""


class ElasticClient:
    """Elastic Client Class."""

    logger = None
    _client = None

    @property
    def client(self):
        print("Giving Elastic Client")
        return ElasticClient._client

    @client.setter
    def client(self, value: Elasticsearch):
        print("Trying to set Elastic client")
        if type(value) == Elasticsearch and not ElasticClient._client:
            ElasticClient._client = value
        else:
            raise Exception(message="Elastic Configuration Issue")

    def __init__(self):
        """Constructor Function."""
        print("--------1-1-1-1-1-1-1-1-1-1-")
        if not ElasticClient._client:
            print("Initialization Elastic Client")
            ElasticClient._client = Elasticsearch(ELASTIC_CONN["URLS"], timeout=1000)
            print(
                f"Elastic Connected: {ElasticClient._client.ping()}",
            )
        else:
            print("Elastic client Already Configured")
