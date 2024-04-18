from django.db import models
from django.contrib.auth.models import User
from tasks.models import Project, Task


# Create your models here.
class BugReport(models.Model):

    STATUS_CHOICES = [
        ("New", "Новая"),
        ("In_progress", "В работе"),
        ("Completed", "Завершена"),
    ]

    PRIORITY_CHANGE = [("1", "Первый"),
                       ("2","Второй"),
                       ("3","Третий"),
                       ("4","Четвертый"),
                       ("5","Пятый"),
                       ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="New",
    )

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHANGE,
        default="1",
    )
    #priority = models.IntegerField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class FeatureRequest(models.Model):

    STATUS_CHOICES = [
        ("Consideration", "Рассмотрение"),
        ("Accepted", "Принято"),
        ("Rejected", "Отклонено"),
    ]

    PRIORITY_CHANGE = [("1", "Первый"),
                       ("2","Второй"),
                       ("3","Третий"),
                       ("4","Четвертый"),
                       ("5","Пятый"),
                       ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="New",
    )

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHANGE,
        default="1",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
