from django.db import models


class Data(models.Model):
    collected = models.CharField(max_length=255)
    add_file = models.CharField(max_length=255)
    finish_button_pressed = models.BooleanField(default=False)

    def __str__(self):
        return self.collected

    class Meta:
        db_table = 'data'


class Task(models.Model):
    name_task = models.CharField(max_length=255)
    field_size = models.CharField(max_length=255)
    max_deadlines = models.CharField(max_length=255)

    def __str__(self):
        return self.name_task

    class Meta:
        db_table = 'tasks'


class TaskToAuthor(models.Model):
    author_id = models.IntegerField()
    deadline_date = models.DateField()
    progress = models.IntegerField()

    def __str__(self):
        return f"TaskToAuthor {self.id}"
