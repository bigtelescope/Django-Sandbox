from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Poll(models.Model):
    id = models.AutoField(primary_key=True)
    poll_name = models.CharField(max_length=40)
    start_data = models.DateField("Start Data")
    end_data = models.DateField("Start Data")
    description = models.TextField("Description")

    def __str__(self):
        return self.poll_name


QUESTION_TYPES = (
    ('TF', 'Ответ текстом'),
    ('SV', 'Один вариант'),
    ('FV', 'Выбор нескольких вариантов'),
)


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question_text = models.TextField("Description")
    question_type = models.CharField(max_length=2, choices=QUESTION_TYPES)
    parent_poll = models.ForeignKey(Poll, editable=False, on_delete=models.CASCADE, related_name="questions")


class Choice(models.Model):
    id = models.AutoField(primary_key=True)
    choice_variant = models.TextField("Possible Answer")
    parent_question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="choices",
        editable=False,
    )
