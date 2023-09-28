from django_filters import FilterSet
from .models import UserReaction


class ResponseFilter(FilterSet):
    class Meta:
        model = UserReaction
        fields = {
            'text': ['icontains'],
        }