from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import JobApplication
from .serializers import JobApplicationSerializer

class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(f"Error: {e}")  # Log error
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
