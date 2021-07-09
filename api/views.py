from .serializers import ItemSerializer
from .models import Item
from rest_framework.generics import ListAPIView , CreateAPIView, DestroyAPIView

class ItemLists(ListAPIView):
    queryset=Item.objects.all()
    serializer_class= ItemSerializer 


class ItemCreate(CreateAPIView):
    queryset=Item.objects.all()
    serializer_class= ItemSerializer 

class ItemDestroy(DestroyAPIView):
    queryset=Item.objects.all()
    serializer_class= ItemSerializer
    lookup_field ='id' 