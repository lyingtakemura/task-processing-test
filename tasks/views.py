from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from tasks.models import Task
from tasks.serializers import TaskSerializer
from tasks.tasks import add_waiting_time_to_task


class TaskViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        add_waiting_time_to_task.delay(serializer.data["id"])

        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
