from django.shortcuts import redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from .repos import URLShortRepo
from .serializers import InURLShortSerializer, OutURLShortSerializer

from core.custom_api_exception import CustomApiException, Exception


# /url-shorts/
class URLShortAPIView(APIView):
    def get(self, request):
        qs = URLShortRepo.list()
        data = OutURLShortSerializer(qs, many=True).data

        return Response(
            data={
                'status': 'success',
                'data': data
            },
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = InURLShortSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            data={
                'status': 'success',
                'data': serializer.data
            },
            status=status.HTTP_201_CREATED
        )


# /url-shorts/{id}/
class URLShortListAPIView(APIView):
    def get_object(self, pk: int):
        instance = URLShortRepo.retrieve({'pk': pk})

        if not instance:
            raise CustomApiException(
                status_code=status.HTTP_404_NOT_FOUND,
                message=Exception.NOT_FOUND['message'],
                err_type=Exception.NOT_FOUND['type']
            )

        return instance

    def get(self, request, pk):
        instance = self.get_object(pk=pk)
        data = OutURLShortSerializer(instance=instance).data

        return Response(
            data={
                'status': 'success',
                'data': data
            },
            status=status.HTTP_200_OK
        )

    def patch(self, request, pk):
        instance = self.get_object(pk=pk)
        serializer = InURLShortSerializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            data={
                'status': 'success',
                'data': serializer.data
            },
            status=status.HTTP_202_ACCEPTED
        )

    def delete(self, request, pk):
        instance = self.get_object(pk=pk)
        instance.archived = True
        instance.save(update_fields=['archived'])

        return Response(
            data={
                'status': 'success'
            },
            status=status.HTTP_204_NO_CONTENT
        )

@api_view(["GET"])
def redirect_view(request, short_url):
    instance = URLShortRepo.retrieve({'short_url': short_url})

    return redirect(instance.url)
