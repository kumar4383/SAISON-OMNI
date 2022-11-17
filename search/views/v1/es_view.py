from typing import List

from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from django.http import JsonResponse
from globals.response import PkHttpResponse
import json

from search.services import ESService

class ESViewSet(viewsets.ViewSet):
    
    @action(methods=["GET"], detail=False)
    def applicant_by_name(self, *args, **kwargs):
        data = ESService.get_applicant_by_name(payload = json.loads(self.request.body))
        return PkHttpResponse(
            data=data,
            status=status.HTTP_200_OK,
        )

    @action(methods=["GET"], detail=False)
    def applicant_by_street(self, *args, **kwargs):
        data = ESService.get_applicant_by_street(payload = json.loads(self.request.body))
        return PkHttpResponse(
            data=data,
            status=status.HTTP_200_OK,
        )

    @action(methods=["GET"], detail=False)
    def applicant_by_expiration_date(self, *args, **kwargs):
        data = ESService.get_applicant_by_expiration_date(payload = json.loads(self.request.body))
        return PkHttpResponse(
            data=data,
            status=status.HTTP_200_OK,
        )

    @action(methods=["POST"], detail=False)
    def add_applicant(self, *args, **kwargs):
        data = ESService.add_applicant(payload = json.loads(self.request.body))
        return PkHttpResponse(
            data=data,
            status=status.HTTP_200_OK,
        )

    @action(methods=["GET"], detail=False)
    def get_nearby_truck(self, *args, **kwargs):
        data = ESService.get_nearby_truck(payload = json.loads(self.request.body))
        return PkHttpResponse(
            data=data,
            status=status.HTTP_200_OK,
        )