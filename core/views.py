from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
# this are third party imports
from .models import Product
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductSerializer


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Product.objects.all()
        p = qs.first()
        serializer = ProductSerializer(p, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# def test_view(request):
#     data = {
#         'name': 'jhon',
#         'age':  23,
#     }
#     return JsonResponse(data)
