from rest_framework import mixins, viewsets
from rest_framework.response import Response

from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
