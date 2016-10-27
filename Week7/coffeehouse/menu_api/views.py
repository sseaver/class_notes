from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from menu_api.models import Special, Ingredient
from menu_api.serializers import SpecialSerializer, IngredientSerializer
from menu_api.permissions import IsCreatedByOrReadOnly


class SpecialListCreateAPIView(ListCreateAPIView):
    queryset = Special.objects.all()
    serializer_class = SpecialSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        return super().perform_create(serializer)


class SpecialDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Special.objects.all()
    serializer_class = SpecialSerializer
    permission_classes = (IsCreatedByOrReadOnly, )


class IngredientListCreateAPIView(ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
        queryset = Ingredient.objects.all()
        serializer_class = IngredientSerializer
