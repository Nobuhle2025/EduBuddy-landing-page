from django.db import models
from django.contrib.auth.models import User
from django.db import models





class Assignment(models.Model):
    title = models.CharField(max_length=200)
    deadline = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)  # New field to track completion status

    def __str__(self):
        return self.title






class ClassSchedule(models.Model):
    # Name of the class (e.g., "Mathematics 101")
    class_name = models.CharField(max_length=255)

    # The day of the class (e.g., "Monday", "Tuesday")
    class_day = models.CharField(max_length=50)

    # Start time of the class (e.g., "09:00:00")
    class_time_start = models.TimeField()

    # End time of the class (e.g., "10:30:00")
    class_time_end = models.TimeField()

    # Name of the instructor for the class
    instructor_name = models.CharField(max_length=255)

    # Location where the class takes place (e.g., "Room 101", "Online")
    location = models.CharField(max_length=255)

    # Additional notes related to the class (e.g., "Bring textbooks", "Exam on next Monday")
    notes = models.TextField(blank=True, null=True)

    # ForeignKey to link the class schedule to a specific user (e.g., a student)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.class_name} - {self.class_day}"







