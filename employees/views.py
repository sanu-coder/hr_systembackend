

from rest_framework import generics
from .models import Employee, Attendance
from .serializers import EmployeeSerializer, AttendanceSerializer


# Add Employee & View Employees
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# Delete Employee
class EmployeeDeleteView(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'


# Mark Attendance
class AttendanceCreateView(generics.CreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


# View Attendance of Employee
class EmployeeAttendanceView(generics.ListAPIView):
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        employee_id = self.kwargs['employee_id']
        return Attendance.objects.filter(employee_id=employee_id)