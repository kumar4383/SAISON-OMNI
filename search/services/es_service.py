import random
from globals.services.elastic.elastic_service import ElasticService as es
import json
import uuid
from datetime import datetime

class ESService:
    @classmethod
    def get_applicant_by_name(cls, payload):
        query = {
            "from": payload["page_no"]*payload["page_size"],
            "size": payload["page_size"],
            "query": {
                "function_score": {
                "query": {
                    "bool": {
                    "must": [
                        {
                        "multi_match": {
                            "query": payload["query"],
                            "fields": [
                            "applicant.raw^500",
                            "applicant.exact^450",
                            "applicant.shingle_phrases^400",
                            "applicant.shingles^350",
                            "applicant.edge_ngram^10"
                            ],
                            "fuzziness": 0,
                            "prefix_length": 2,
                            "type": "best_fields",
                            "boost": 2
                        }
                        }
                    ],
                    "should": []
                    }
                },
                "functions": []
                }
            },
            "sort": [
                "_score"
            ]
            }

        el_service = es()
        data = el_service.search_data(index="applicant", query=query)
        to_return = []
        for item in data:
            obj = {
                "id": item["_id"],
                "applicant": item["applicant"],
                "address": item["address"],
                "locationDescription": item["locationDescription"],
                "expirationDate": item["expirationDate"],
                "location": item["location"],
            }
            to_return.append(obj)

        return to_return
        
    @classmethod
    def get_applicant_by_street(cls, payload):
        query = {
            "from": payload["page_no"]*payload["page_size"],
            "size": payload["page_size"],
            "query": {
                "function_score": {
                "query": {
                    "bool": {
                    "must": [
                        {
                        "multi_match": {
                            "query": payload["query"],
                            "fields": [
                            "address.raw^500",
                            "address.exact^450",
                            "address.shingle_phrases^400",
                            "address.shingles^350",
                            "address.edge_ngram^10"
                            ],
                            "fuzziness": 0,
                            "prefix_length": 2,
                            "type": "best_fields",
                            "boost": 2
                        }
                        }
                    ],
                    "should": []
                    }
                },
                "functions": []
                }
            },
            "sort": [
                "_score"
            ]
            }

        el_service = es()
        data = el_service.search_data(index="applicant", query=query)
        to_return = []
        for item in data:
            obj = {
                "id": item["_id"],
                "applicant": item["applicant"],
                "address": item["address"],
                "locationDescription": item["locationDescription"],
                "expirationDate": item["expirationDate"],
                "location": item["location"],
            }
            to_return.append(obj)

        return to_return

    @classmethod
    def get_applicant_by_expiration_date(cls, payload):
        query = {
            "from": payload["page_no"]*payload["page_size"],
            "size": payload["page_size"],
            "query": {
                "range": {
                    "expirationDate": {
                        "lte": datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
                    }
                }
            },
            "sort": [
                { "expirationDate" : {"order" : "asc", "format": "strict_date_optional_time_nanos"}},
                "_score"
            ]
            }

        print(query, "query")    

        el_service = es()
        data = el_service.search_data(index="applicant", query=query) or []
        to_return = []
        for item in data:
            obj = {
                "id": item["_id"],
                "applicant": item["applicant"],
                "address": item["address"],
                "locationDescription": item["locationDescription"],
                "expirationDate": item["expirationDate"],
                "location": item["location"],
            }
            to_return.append(obj)

        return to_return

    @classmethod
    def add_applicant(cls, payload):
        id = uuid.uuid4()
        doc = {
            "id": str(id),
            "applicant": payload["applicant"],
            "address": payload["address"],
            "locationDescription": payload["locationDescription"],
            "expirationDate": payload["expirationDate"],
            "location": payload["location"]
        }

        el_service = es()

        resp = el_service.create_doc_by_id(index="applicant", doc_id=str(id), doc=doc)
        obj = el_service.search_by_id(index="applicant", doc_id=resp["_id"])
        to_return = {
            "id" : obj["_id"],
            "applicant" : obj["applicant"],
            "address" : obj["address"],
            "locationDescription" : obj["locationDescription"],
            "expirationDate" : obj["expirationDate"],
            "location" : obj["location"],
        }
        return to_return

    @classmethod
    def get_nearby_truck(cls, payload):
        el_service = es()

        query = {
            "from": payload["page_no"]*payload["page_size"],
            "size": payload["page_size"],
            "query": {
                "match_all": {}
            },
            "sort": [
                {
                    "_geo_distance": {
                        "location-field": payload["location"],
                        "order": "asc",
                        "unit": "km",
                        "mode": "min",
                        "distance_type": "arc",
                        "ignore_unmapped": True
                    }
                }
            ]
        }

        resp = el_service.search_data(index="applicant", query=query)
        to_return = []
        for item in resp:
            item = {
                "id": item["_id"],
                "applicant": item["applicant"],
                "address": item["address"],
                "locationDescription": item["locationDescription"],
                "expirationDate": item["expirationDate"],
                "location": item["location"],
            }
            to_return.append(item)

        return to_return