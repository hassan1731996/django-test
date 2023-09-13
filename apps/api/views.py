from django.urls import reverse
from rest_framework import generics, viewsets, permissions
from rest_framework.response import Response

from apps.api.models import Product
from apps.api.pagination import CustomPagination
from apps.api.serializers import ProductSerializer


class APIRootView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        return Response(
            {
                "products": reverse("product-list")
                # Add more resources/endpoints as needed
            }
        )


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = CustomPagination
