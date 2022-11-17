from globals.clients.elastic_client import ElasticClient

class ElasticService:
    """Elastic Service Class."""

    def __init__(self):
        self._client = ElasticClient()._client

    def search_data(self, index, query):
        data = []
        try:
            res = self._client.search(index=index, body=query)
            for doc in res["hits"]["hits"]:
                source = doc["_source"]
                source["_id"] = doc["_id"]
                data.append(source)
            return data
        except Exception as ex:
            print(f"{query} failed - Exception: {ex}")

    def search_by_id(self, index, doc_id):
        print("searching data by given id")
        try:
            res = self._client.get(index=index, id=doc_id)
            source = res["_source"]
            source["_id"] = res["_id"]
            return source
        except Exception as ex:
            print(f"search_by_id failed - Exception: {ex}")


    def create_doc_by_id(self, index, doc_id, doc, refresh=False):
        print("creating doc by id here")
        try:

            resp = self._client.index(index=index, body=doc, id=doc_id, refresh=refresh)
            print("---doc_created---")
            return resp
        except Exception as ex:
            print(ex)
            return False

    def update_doc(self, index, id, body, refresh=False):
        print("updating doc by id here")
        try:
            resp = self._client.update(
                index=index,
                id=id,
                body=body,
                refresh=refresh,
            )
            return resp
        except Exception as ex:
            print(ex)
            return False
