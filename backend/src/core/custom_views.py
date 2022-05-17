from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


def custom_viewset_response(function):

    def wrapper(*args, **kwargs):
        response = function(*args, **kwargs)

        return Response(data={"status": "success", "data": response.data})

    return wrapper


class BaseViewSet(ModelViewSet):

    @custom_viewset_response
    def create(self, request: Request, *args, **kwargs) -> Response:
        return super().create(request, args, kwargs)

    @custom_viewset_response
    def retrieve(self, request: Request, *args, **kwargs) -> Response:
        return super().retrieve(request, args, kwargs)

    @custom_viewset_response
    def update(self, request: Request, *args, **kwargs) -> Response:
        return super().update(request, args, kwargs)

    def destroy(self, request: Request, *args, **kwargs) -> Response:
        instance = self.get_object()
        instance.archived = True
        instance.save(update_fields=["archived"])

        return Response(data={"status": "success"})
