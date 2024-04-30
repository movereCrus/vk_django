from django.db import models

from tasks.models import Project, Task

PRIORITY_CHOICES = [
        (5, 'Наивысший'),
        (4, 'Высокий'),
        (3, 'Обычный'),
        (2, 'Ниже среднего'),
        (1, 'Несущественный'),
    ]

class BugReport(models.Model):
    BUG_CHOICES = [
        ('New', 'Новая'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершена'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name='bug_report_project',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    task = models.ForeignKey(
        Task,
        related_name='bug_report_tasks',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=50,
        choices=BUG_CHOICES,
        default='New',
    )
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=0,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FeatureRequest(models.Model):
    FEATURE_CHOICES = [
        ('Review', 'Рассмотрение'),
        ('Accepted', 'Принято'),
        ('Rejected', 'Отклонено'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name='feature_request_project',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    task = models.ForeignKey(
        Task,
        related_name='feature_request_task',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=50,
        choices=FEATURE_CHOICES,
        default='Now',
    )
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=0,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
