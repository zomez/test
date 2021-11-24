from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import DepPay, RayPay
from .serializers import DepPaySerializer, RayPaySerializer


class DepPayView1(APIView):
    """Сериализация Выплаты"""

    def get(self, request):
        serializer = DepPaySerializer()
        obj = {serializer}
        return Response(serializer.data)

    def post(self, request):
        serializer = DepPaySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepPayList(generics.ListAPIView):
    queryset = DepPay.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = DepPaySerializer(queryset, many=True)
        return Response(serializer.data)


class DepPayView(generics.ListCreateAPIView):
    serializer_class = DepPaySerializer
    queryset = DepPay.objects.all()

    def get(self, request, *args, **kwargs):

        serializer = DepPaySerializer
        ray_all = RayPay.objects.all()
        ray = RayPaySerializer(ray_all, many=True)
        print(ray.data)

        return Response({'ray': ray.data})

    def post(self, request, *args, **kwargs):
        print(request.data, request.user)

        return Response(status=200)


class DepPayUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = DepPaySerializer
    queryset = DepPay.objects.all()
